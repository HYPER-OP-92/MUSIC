# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from LolMusic import app

@app.on_message(filters.command("privacy"))
async def privacy_command(client: Client, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/46a60562ff98cc1180237-0b722292cd1bcca02f.jpg",
        caption="**➻ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴧᴧʀᴜᴍɪ ʙᴏᴛꜱ ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ.**\n\n**⊚ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛʜᴇɴ ꜱᴇᴇ ʙᴏᴛs ᴘʀɪᴠᴧᴄʏ ᴘᴏʟɪᴄʏ 🔏**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ᴘʀɪᴠᴧᴄʏ ᴘᴏʟɪᴄʏ", url="https://telegra.ph/BOTS--PRIVACY-POLICY-01-19")]
            ]
        )
    )

# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================
