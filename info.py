import os
import time

class Config(object):
    # Pyrogram Client
    API_ID = os.environ.get("API_ID")
    if not API_ID or not API_ID.isdigit():
        raise ValueError(f"Invalid API_ID: {API_ID}. It must be a numeric integer.")
    API_ID = int(API_ID)

    API_HASH = os.environ.get("API_HASH")
    if not API_HASH:
        raise ValueError("API_HASH is missing. Please set it in environment variables.")

    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing. Please set it in environment variables.")

    # Other Configs
    BOT_START_TIME = time.time()

    OWNER = os.environ.get("OWNER")
    if not OWNER or not OWNER.isdigit():
        raise ValueError(f"Invalid OWNER: {OWNER}. It must be a numeric integer.")
    OWNER = int(OWNER)

    SUDO = os.environ.get("SUDO", "")
    try:
        SUDO = list(map(int, SUDO.split())) if SUDO else []
    except ValueError:
        raise ValueError(f"Invalid SUDO list: {SUDO}. All SUDO values must be integers.")

    # Web Response Config
    WEBHOOK = os.environ.get("WEBHOOK", "True").lower() in ("true", "1", "yes")
    PORT = os.environ.get("PORT", "8080")
    if not PORT.isdigit():
        raise ValueError(f"Invalid PORT: {PORT}. It must be a numeric integer.")
    PORT = int(PORT)

class Txt(object):

    SEND_NUMBERS_MSG = """
❪ ENTER THE TOTAL NUMBER ❫

☛ How many numbers do you have?
Let us know, and we'll handle the rest!
"""

    SEND_TARGET_CHANNEL = """
❪ SEND TARGET CHANNEL LINK/USERNAME ❫

☛ Provide the target channel's link or username
For example:
<code>@username</code> or <code>https://t.me/yourtarget</code>
"""

    SEND_SESSION_MSG = """
❪ SEND SESSION STRING ❫

☛ Generate your session string with API ID, API HASH, and mobile number.

API_ID = 14050586
API_HASH = 42a60d9c657b106370c79bb0a8ac560c

🔗 Generate here: [Session String Generator](https://telegram.tools/session-string-generator#pyrogram,user) and send it here.

✅ Safe and easy!

"""

    SEND_API_ID = """
❪ SEND API ID ❫

☛ Api_id Get from my.telegram.org
"""
    SEND_API_HASH = """
❪ SEND API HASH ❫

☛ Api_hash Get from my.telegram.org
"""

    MAKE_CONFIG_DONE_MSG = """
✅ {} Accounts Successfully Added 👥

🔹 All accounts are now logged into the target channel/group to start reporting.

🔍 Tap below to see the total number of Telegram accounts you've added. ⬇️
"""

    ADDED_ACCOUNT = """
✅ Successfully Added: {} Accounts 👥

🔍 Want Details? Tap the button below to view full info on the Telegram accounts you've added. ⬇️
"""

    ACCOUNT_INFO = """
<b> Name :- </b> <code> {0} </code>
<b> User Id :- </b> <code> {1} </code>
"""

    REPORT_CHOICE = """
❪ CHOOSE YOUR STRIKE REASON ⚠️ ❫

🔹 1. Child Abuse 🚨
🔹 2. Copyright Violation 📁
🔹 3. Impersonation 🎭
🔹 4. Irrelevant Geo Group 🌍
🔹 5. Illegal Drugs 💊
🔹 6. Violence & Threats 🔪
🔹 7. Offensive Personal Details ⚠️
🔹 8. Adult Content 🔞
🔹 9. Spam & Scams 🚫

💥 Select a reason (1-9) and let the bot do its work! 👇
"""

    SEND_NO_OF_REPORT_MSG = """
❪ CHOOSE REPORT COUNT 🚀 ❫

📌 Enter the number of reports you want to send to @{}

🔹 The bot will relentlessly strike the target channel/group until it reaches your set report count. 🎯🔥
"""

    START_MSG = """
💥 X-Strike Bot — The ultimate destruction tool.

🔥 Destroy IDs, Groups & Channels 🔥
👑 Admin: @FR_KAIRV
⚙️ Developed by: @aboutitachii
⭐ Feedback: [Soon]
🚀 How It Works: [Soon]
"""

    HELP_MSG = """
🔆 HELP MENU

📌 Available Commands:

⏣ /start — Check if I'm alive ✅
⏣ /make_config — Create a new config ⚙️
⏣ /del_config — Delete existing config ❌
⏣ /target — View the current target 🎯
⏣ /see_accounts — List added accounts 👥
⏣ /add_account — Add new accounts ➕
⏣ /report — Strike the target 🚀
⏣ /restart — Reboot the bot 🔄

⚡ Use the commands wisely!


💢 Features

► Mass Report: Strike a single channel/group with multiple IDs
► Custom Reports: Choose the type of report for every strike
► Target Flexibility: Easily change the target channel or group
► Multiple Accounts: Add as many accounts as you need after configuring
► Automatic Joining: All added accounts join the target automatically
► Easy Setup: No need for phone number, password, or OTP—just send the session string
► Server Monitoring: Track server status and resource usage in real-time

⚡ Unleash the power!
"""

    ABOUT_MSG = """
- 𝖬𝗒 𝖭𝖺𝗆𝖾 : <a href=https://t.me/{}>{}</a>
- 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href=@aboutitachii</a>
- 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : Pyrogram
- 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇 𝟥
- 𝖣𝖺𝗍𝖺𝖡𝖺𝗌𝖾 : 𝖬𝗈𝗇𝗀𝗈𝖣𝖡
- 𝖡𝖮𝖳 𝖲𝖾𝗋𝗏𝖾𝗋 : 𝖠𝗇𝗒𝖶𝗁𝖾𝗋𝖾
"""
