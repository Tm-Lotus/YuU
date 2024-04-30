import asyncio
from pyrogram import Client, filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message , ReplyKeyboardMarkup , KeyboardButton
from  AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)

@app.on_message(filters.text & (filters.channel | filters.private))            
async def hhhki(client: Client, message: Message):
    msg = message.text
    if message.from_user is not None:
        usr = await client.get_chat(message.from_user.id)
        name = usr.first_name
        usr_id = message.from_user.id
        mention = message.from_user.mention
        await app.send_message(OWNER_ID, f"- قام {mention} \n\n- بارسال رسالة للبوت \n\n- {msg}")
    else:
        print("Received message from unknown user.")