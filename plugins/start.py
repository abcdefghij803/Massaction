import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from info import Config, Txt


@Client.on_message(filters.private & filters.command('start'))
async def handle_start(bot:Client, message:Message):

    Btn = [
        [InlineKeyboardButton(text='˹ ʜєʟᴘ ˼', callback_data='help'), InlineKeyboardButton(text='˹ ʙσᴛ sᴛᴧᴛυs ˼', callback_data='server')],
        [InlineKeyboardButton(text='˹ υᴘᴅᴧᴛє ˼', url='https://t.me/Grandxmasti'), InlineKeyboardButton(text='˹ ʙσᴛ ɪηғσ ˼', callback_data='about')],
        [InlineKeyboardButton(text='˹ σᴡηєꝛ ˼', url='https://t.me/aboutitachii')]
        ]

    await message.reply_text(text=Txt.START_MSG.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(Btn))


#Restart to cancell all process 
@Client.on_message(filters.private & filters.command("r") & filters.user(Config.SUDO))
async def restart_bot(b, m):
    await m.reply_text("🔄__𝗒𝗈𝗎𝗋 𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗋𝖾𝗌𝗍𝖺𝗋𝗍.....__")
    os.execl(sys.executable, sys.executable, *sys.argv)
