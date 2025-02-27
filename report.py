import sys
import asyncio
import json
from pyrogram import Client
from pyrogram.raw.functions.account import ReportPeer
from pyrogram.raw.types import *
from pyrogram.errors import PeerIdInvalid

# Option 1: Add sessions directly in the code (leave empty if using config.json)
ACCOUNTS = [
    # {"Session_String": "YOUR_SESSION_STRING_1", "OwnerName": "Account 1"},
    # {"Session_String": "YOUR_SESSION_STRING_2", "OwnerName": "Account 2"}
]

# Option 2: Load from config.json if ACCOUNTS list is empty
CONFIG_FILE = "config.json"

# Function to determine the report reason
def get_reason(text):
    reasons = {
        "child abuse": InputReportReasonChildAbuse(),
        "impersonation": InputReportReasonFake(),
        "copyright": InputReportReasonCopyright(),
        "irrelevant": InputReportReasonGeoIrrelevant(),
        "pornography": InputReportReasonPornography(),
        "illegal drugs": InputReportReasonIllegalDrugs(),
        "offensive personal details": InputReportReasonSpam(),
        "spam": InputReportReasonPersonalDetails(),
        "violence": InputReportReasonViolence()
    }
    return reasons.get(text.lower(), InputReportReasonOther())

# Function to extract post information from the Telegram link
def extract_post_details(link):
    try:
        parts = link.split('/')
        chat_username = parts[-3]  # Telegram username or group/channel name
        message_id = int(parts[-1])  # Post/message ID
        return chat_username, message_id
    except (IndexError, ValueError):
        return None, None

# Report function targeting a specific post
async def report_post(client, link, reason_text, reporter_name):
    chat_username, message_id = extract_post_details(link)
    
    if not chat_username or not message_id:
        print(f"[{reporter_name}] Invalid post link format: {link}")
        return

    try:
        # Resolve chat and message ID
        chat = await client.get_chat(chat_username)
        reason = get_reason(reason_text)

        # Report the specific post
        await client.invoke(
            ReportPeer(
                peer=await client.resolve_peer(chat.id),
                id=[message_id],  # This targets the specific post
                reason=reason,
                message=f"Reported by {reporter_name} for: {reason_text}"
            )
        )
        print(f"[{reporter_name}] Successfully reported post {message_id} in {chat_username} for {reason_text}.")
    except PeerIdInvalid:
        print(f"[{reporter_name}] Invalid chat or user: {chat_username}")
    except Exception as e:
        print(f"[{reporter_name}] Failed to report post: {e}")

# Load accounts from config if ACCOUNTS list is empty
def load_accounts():
    if not ACCOUNTS:
        try:
            with open(CONFIG_FILE, "r") as file:
                config = json.load(file)
                return config["accounts"]
        except Exception as e:
            print(f"Failed to load config.json: {e}")
            sys.exit(1)
    return ACCOUNTS

# Main function for reporting via multiple accounts
async def main(post_link, reason):
    accounts = load_accounts()
    for account in accounts:
        session_string = account["Session_String"]
        reporter_name = account["OwnerName"]

        async with Client(name=reporter_name, session_string=session_string) as app:
            await report_post(app, post_link, reason, reporter_name)

# Entry point for command-line usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your_script.py <post_link> <reason>")
        sys.exit(1)

    post_link = sys.argv[1]
    report_reason = sys.argv[2]

    asyncio.run(main(post_link, report_reason))
