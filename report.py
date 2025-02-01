import sys
from pyrogram import Client
import asyncio
import json
from pyrogram.raw.functions.account import ReportPeer
from pyrogram.raw.types import *


def get_reason(text):
    reasons = {
        "Report for child abuse": InputReportReasonChildAbuse,
        "Report for impersonation": InputReportReasonFake,
        "Report for copyrighted content": InputReportReasonCopyright,
        "Report an irrelevant geogroup": InputReportReasonGeoIrrelevant,
        "Reason for Pornography": InputReportReasonPornography,
        "Report an illegal drug": InputReportReasonIllegalDrugs,
        "Report for offensive person detail": InputReportReasonSpam,
        "Report for spam": InputReportReasonPersonalDetails,
        "Report for Violence": InputReportReasonViolence
    }
    return reasons.get(text, None)  # Default None if not found


async def main(reason_text, message_text):
    try:
        config = json.load(open("config.json"))
        report_reason_class = get_reason(reason_text)

        if report_reason_class is None:
            print(f"Invalid report reason: {reason_text}")
            return

        report_reason = report_reason_class()
        target = config.get('Target')

        for account in config["accounts"]:
            session_string = account["Session_String"]
            owner_name = account['OwnerName']

            async with Client(name="Session", session_string=session_string) as app:
                try:
                    peer = await app.resolve_peer(target)
                    peer_id = getattr(peer, 'channel_id', None)
                    access_hash = getattr(peer, 'access_hash', None)

                    if peer_id is None or access_hash is None:
                        print(f"Failed to resolve peer: {target}")
                        continue

                    channel = InputPeerChannel(channel_id=peer_id, access_hash=access_hash)
                    
                    report_peer = ReportPeer(
                        peer=channel,
                        reason=report_reason,
                        message=message_text
                    )

                    result = await app.invoke(report_peer)
                    print(f"Success: {result} | Reported by {owner_name}")

                except Exception as e:
                    print(f"Error reporting from {owner_name}: {e}")

    except Exception as e:
        print(f"Error in main function: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your_script.py '<reason>' '<message>'")
        sys.exit(1)

    reason_arg = sys.argv[1]
    message_arg = sys.argv[2]

    asyncio.run(main(reason_arg, message_arg))
