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
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["عفرتو","مطور السورس","مبرمج السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ْᯓ 𝘼𝙇𓄂𝙈𝙊𝙃𝘼𝙉𝘿𝙄𝙎 🜝](https://t.me/yQr70)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @yQr70 ❫
◉ 𝙸𝙳      : ❪ `6304465500` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@yqr70)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ْᯓ 𝘼𝙇𓄂𝙈𝙊𝙃𝘼𝙉𝘿𝙄𝙎 🜝", url=f"https://t.me/yQr70"), 
                 ],[
                   InlineKeyboardButton(
                        "「SOURS SIMA」", url=f"https://t.me/yqr70"),
                ],

            ]

        ),

    )
