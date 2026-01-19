# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from LolMusic import app
import config
from LolMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**<u>❃ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇᴧᴍ ᴧᴧʀᴜᴍɪ ʀᴇᴘᴏs ❃</u>

✼ ʀᴇᴘᴏ ɪs ɴᴏᴡ ᴘʀɪᴠᴧᴛᴇ ᴅᴜᴅᴇ 😌
 
❉  ʏᴏᴜ ᴄᴧɴ мʏ ᴜsᴇ ᴘᴜʙʟɪᴄ ʀᴇᴘᴏs !! 

✼ || ᴄᴏɴᴛᴧᴄᴛ :-  [˹ ᴍᴀᴀɴᴀᴠ sᴜᴘᴘᴏʀᴛ ᴄʜᴧᴛ ˼ ](https://t.me/maanavbots) ||
 
❊ ʀᴜɴ 24x7 ʟᴧɢ ϝʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
    [
        InlineKeyboardButton("𝐌𝐀𝐀𝐍𝐀𝐕 𝐗 𝐌𝐔𝐒𝐈𝐂", url="https://t.me/maanavXmuzicbot"),
        InlineKeyboardButton("𝐀𝐍𝐈𝐊𝐀𝐀 𝐗 𝐌𝐔𝐒𝐈𝐂", url="https://t.me/anikaaXmuzicbot")
    ],
    [
        InlineKeyboardButton("𝐀𝐍𝐔𝐏𝐑𝐈𝐘𝐀 𝐗 𝐌𝐔𝐒𝐈𝐂", url="https://t.me/cuteanubot"),
        InlineKeyboardButton("ᴄʜᴧᴛ ʙᴏᴛ", url="https://t.me/maanavbots")
    ],
    [
        InlineKeyboardButton("ᴜsᴇʀ ʙᴏᴛ", url="https://t.me/maanavbots"),
        InlineKeyboardButton("sᴘᴧᴍ ʙᴏᴛ", url="https://t.me/maanavbots")
    ],
    [
        InlineKeyboardButton("sᴇssɪᴏɴ ʙᴏᴛ", url="https://t.me/maanavbots"),
        InlineKeyboardButton("sᴇssɪᴏɴ ʜᴧᴄᴋ", url="https://t.me/maanavbots")
    ],
    [
        InlineKeyboardButton("ʙᴧɴᴧʟʟ ʙᴏᴛ", url="https://t.me/maanavbots"),
        InlineKeyboardButton("ᴧɴʏ ɪssᴜᴇ", user_id=config.OWNER_ID)
    ],
    [
        InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴧᴛ ✙", url=f"https://t.me/{app.username}?startgroup=true")
    ]
]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/7enu2i.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================
