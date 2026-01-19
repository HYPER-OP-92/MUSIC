# ======================================================
# ©️ 2025-26 ᴘʀᴇᴍɪᴜᴍ ᴄᴏᴅᴇ ʙʏ ʀᴇᴠᴀɴɢᴇ 😎
# 🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : t.me/dmcatelegram
# 📢 ᴄʜᴀɴɴᴇʟ : t.me/dmcatelegram
# 🛠 ᴜᴘᴅᴀᴛᴇᴅ : ᴠᴇʀsɪᴏɴ 3.0 (ᴀᴅᴠᴀɴᴄᴇᴅ ᴜɪ)
# =======================================================

import time
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from LolMusic import app
import config
from LolMusic.utils.formatters import get_readable_time

# Start Time for Uptime
start_time = time.time()

# Premium Text Design
REPO_TEXT = """
✨ **━━━━━━『 ᴋɪʀᴜ ᴛᴇᴄʜ 』━━━━━━** ✨

👋 **ʜᴇʟʟᴏ {name}!**
ᴛʜɪs ɪs ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ʀᴇᴘᴏsɪᴛᴏʀʏ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ʜᴜʙ.

🚀 **sᴛᴀᴛᴜs:** ᴏɴʟɪɴᴇ & ʟᴀɢ-ғʀᴇᴇ
🛠 **ᴠᴇʀsɪᴏɴ:** ᴠ3.0 (ᴜʟᴛɪᴍᴀᴛᴇ)
⏳ **ᴜᴘᴛɪᴍᴇ:** `{uptime}`

📢 **ɴᴏᴛᴇ:** sᴏᴍᴇ ʀᴇᴘᴏs ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ **ᴘʀɪᴠᴀᴛᴇ** 🔐 
ғᴏʀ sᴇᴄᴜʀɪᴛʏ ʀᴇᴀsᴏɴs. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴏᴜʀ ᴘᴜʙʟɪᴄ ʙᴏᴛs ʙᴇʟᴏᴡ.

━━━━━━━『 **ᴏᴜʀ ᴘʀᴏᴊᴇᴄᴛs** 』━━━━━━━
"""

@app.on_message(filters.command("repo"))
async def repo_command(_, message: Message):
    # Calculate Uptime
    current_time = time.time()
    uptime_seconds = int(round(current_time - start_time))
    uptime = get_readable_time(uptime_seconds)

    # Stylish Buttons
    buttons = [
        [
            InlineKeyboardButton("🤖 ᴀᴀʀᴜ ᴍᴜsɪᴄ", url="https://t.me/aaru_music_rbot"),
            InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/NOBITA_SUPPORT")
        ],
        [
            InlineKeyboardButton("🤖 ɴɪᴋᴋᴜ ᴍᴜᴢɪᴄ", url="https://t.me/NIKKU_ROBOT"),
            InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/NOBITA_SUPPORT")
        ],
        [
            InlineKeyboardButton("🤖 ʀᴀᴅʜᴀ ᴍᴜsɪᴄ", url="https://t.me/RADHAVIBEBOT"),
            InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/NOBITA_SUPPORT")
        ],
        [
            InlineKeyboardButton("🤖 sʜʏᴀᴍ ᴍᴜsɪᴄ", url="https://t.me/SHYAMVIBEBOT"),
            InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/NOBITA_SUPPORT")
        ],
        [
            InlineKeyboardButton("👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=config.OWNER_ID),
            InlineKeyboardButton("📢 ᴄʜᴀɴɴᴇʟ", url="https://t.me/VnioxTechApi")
        ],
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{app.username}?startgroup=true")
        ]
    ]

    # Sending the message with a premium photo
    await message.reply_photo(
        photo="https://graph.org/file/46a60562ff98cc1180237-0b722292cd1bcca02f.jpg",
        caption=REPO_TEXT.format(
            name=message.from_user.mention,
            uptime=uptime
        ),
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# ======================================================
# ⚡ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dmcatelegram
# ======================================================
