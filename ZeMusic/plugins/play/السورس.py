import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","سيما","السورس", "سورس سيما"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/4de92822c3b4873db9572.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ  𝘴SOURS SIMA(t.me/Uyut70)
么 [َ ᯓ 𝘼𝙇𓄂𝙈𝙊𝙃𝘼𝙉𝘿𝙄𝙎 ](t.me/yqr70)
么 [َ ᥉υρρ᥆ᖇƚ ](t.me/YR_HX)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹  ᯓ 𝘼𝙇𓄂𝙈𝙊𝙃𝘼𝙉𝘿𝙄𝙎  . 🕷 › ", url=f"https://t.me/yqr70"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲ️ꪀꪀᥱᥣ›", url=f"https://t.me/yut70"), 
                    InlineKeyboardButton(
                        "‹ ᥉υρρ᥆ᖇƚ›", url=f"https://t.me/YR_HX "),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )
  
