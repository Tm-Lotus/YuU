#_____كسمك تحياتي 
#_____@EU_TM

import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from AbdoX import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/HQ_BX/5",
        caption=f"𖥻 WelCoMe To SoUrCe BoDa Music .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𖥻 GrOuP .", url=f"https://t.me/jx_xll"), 
                 InlineKeyboardButton(
                   "𖥻 SoUrCe .",       url=f"https://t.me/l2_2Y"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "𖥻 UR , FaV BoDa .", url=f"https://t.me/II_U_6"), 
                      
             ],[ 
            InlineKeyboardButton(
                      "𖥻 UR , FaV MoHaMeD .", url=f"https://t.me/YeYeYc"), 
                      
             ],[ 
                  InlineKeyboardButton(
                text="𖥻 AdD Me To YoUr GrOuP .",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )





@app.on_message(
    command(["بودا" , "عبدو","مطور السورس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("II_U_6")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"𖥻 SoUrCe DeVeLoPer InFoRmaTioN\n\n 𖥻 UsEr : @{usr.username}\n 𖥻 Id : `{usr.id}`\n 𖥻 BiO : {usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

@app.on_message(
command(["محمد" , "ميدو","حمو","مبرمج السورس"])
    
    
) 
async def yas(client, message):
    usr = await client.get_chat("YeYeYc")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"𖥻 SoUrCe DeVeLoPer InFoRmaTioN\n\n 𖥻 UsEr : @{usr.username}\n 𖥻 Id : `{usr.id}`\n 𖥻 BiO : {usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(filters.command(["المطاور", "مطور السورس", "سينزر", "صاحب السورس", يا يوساننالتف"], ""), group=73) 
async def deev(client: Client, message: Message):
     user = await client.get_chat(chat_id="II_U_6")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"**𖥻 SoUrCe DeVeLoPer InFoRmaTioN\n\n 𖥻 UsEr : @{username}\n 𖥻 Id : `{usr.id}`\n 𖥻 BiO : {usr.bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass

