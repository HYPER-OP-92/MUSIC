# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎

# 🧑‍💻 Developer : t.me/dmcatelegram
# 🔗 Source link : https://github.com/hexamusic/LolMusic
# 📢 Telegram channel : t.me/dmcatelegram
# =======================================================

import time, asyncio
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython import VideosSearch

import config
from LolMusic import app
from LolMusic.misc import _boot_
from LolMusic.plugins.sudo.sudoers import sudoers_list
from LolMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from LolMusic.utils import bot_sys_stats
from LolMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from LolMusic.utils.decorators.language import LanguageStart
from LolMusic.utils.formatters import get_readable_time
from LolMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

# ---------------- IMAGES -------------------
NEXIO = [
    "https://files.catbox.moe/6ewyca.jpg",
        "https://files.catbox.moe/cbpj3q.jpg",
        "https://files.catbox.moe/hn384x.jpg",
        "https://files.catbox.moe/0acktl.jpg",
        "https://files.catbox.moe/s1pxqw.jpg",
        "https://files.catbox.moe/2e3tyo.jpg",
        "https://files.catbox.moe/01ecpl.jpg",
        "https://files.catbox.moe/n82tpe.jpg",
        "https://files.catbox.moe/nvkq2r.jpg",
        "https://files.catbox.moe/63o774.jpg",
        "https://files.catbox.moe/h0foag.jpg",
        "https://files.catbox.moe/duwctr.jpg",
        "https://files.catbox.moe/s1hrd3.jpg",
        "https://files.catbox.moe/0n6ej5.jpg",
        "https://files.catbox.moe/3esxuh.jpg",
        "https://files.catbox.moe/i1o537.jpg",
        "https://files.catbox.moe/n02mbg.jpg",
        "https://files.catbox.moe/jofmuy.jpg",
        "https://files.catbox.moe/pysrqh.jpg",
        "https://files.catbox.moe/4as5xk.jpg",
        "https://files.catbox.moe/rtd9zp.jpg",
        "https://files.catbox.moe/m5tzvi.jpg",
        "https://files.catbox.moe/h4ae1t.jpg",
]

# ---------------- STICKER -------------------
REVANGE_STKR = [
    "CAACAgUAAxkBAAKOmmkz-ntJaFPXb0carGSNRtKHl69sAAL7HQACNIWhVdDyUdqb8yMtHgQ",
    "CAACAgUAAxkBAAKOm2kz-nsnFNG9zS0eyjaE9mEriTN2AAKLHQACXmKhVWRYc-mThaGHHgQ",
    "CAACAgUAAxkBAAKOnGkz-ny89GKzIC8y38Gqdg_ujQg4AAIkHAAChPKgVcjV8fUfimNGHgQ",
    "CAACAgUAAxkBAAKOnWkz-nz5cZGEYLoWfp7QZgIbf9HbAAIRHQAC_jOgVdqhnaopN_EJHgQ", 
    "CAACAgUAAxkBAAKOnmkz-n013B233W24UyE4KiAtEbRlAAKAGwAC0VOgVe_Z1cRSzI-sHgQ", 
    "CAACAgUAAxkBAAKOn2kz-n2FSJi7MKC9q0Wy6T7CilM8AALTHAACvgABoFXBEMums5ywdR4E", 
    "CAACAgUAAxkBAAKOoGkz-n7ENOqTjvLOaCZFSkOZLiYCAAJaGwACWXKgVaxKbq4HeZ4MHgQ",
    "CAACAgUAAxkBAAKOoWkz-n7JfmZjgzI7n5srNEY_bkyGAAINGgACbpigVSc4KH8aMEshHgQ", 
    "CAACAgUAAxkBAAKOomkz-n-62srSaAOYMPKLHPevi8FBAAJvHAACcwmgVbva9WxHwDJIHgQ", 
    "CAACAgUAAxkBAAKOo2kz-oBmaCHZ96BNQafgepRINZKYAAKjGwACeZmgVSPTNWP_M9WLHgQ",
]

# ---------------- START PM -------------------
@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)

    stk = await message.reply_sticker(random.choice(REVANGE_STKR))
    await asyncio.sleep(1)
    await stk.delete()

    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]

        # help
        if name.startswith("help"):
            keyboard = help_pannel(_)
            return await message.reply_photo(
                random.choice(NEXIO),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )

        # sudo
        if name.startswith("sud"):
            await sudoers_list(client=client, message=message, _=_)
            return

        # info youtube
        if name.startswith("inf"):
            waiting = await message.reply("🔎 Searching...")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"

            results = VideosSearch(query, limit=1)
            data = (await results.next())["result"][0]

            title = data["title"]
            duration = data["duration"]
            views = data["viewCount"]["short"]
            thumbnail = data["thumbnails"][0]["url"].split("?")[0]
            link = data["link"]
            channellink = data["channel"]["link"]
            channel = data["channel"]["name"]
            published = data["publishedTime"]

            text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )

            key = InlineKeyboardMarkup(
                [[InlineKeyboardButton(text=_["S_B_8"], url=link)]]
            )

            await waiting.delete()

            return await message.reply_photo(
                photo=thumbnail,
                caption=text,
                reply_markup=key,
            )

    # Main start message
    hello = await message.reply_text(f"**Hey {message.from_user.mention} 💖**")
    await asyncio.sleep(0.5)
    await hello.edit("**I am your music bot...✨**")
    await asyncio.sleep(0.5)
    await hello.edit("**Ready to play? 🎧**")
    await asyncio.sleep(0.5)
    await hello.delete()

    out = private_panel(_)
    await message.reply_photo(
        random.choice(NEXIO),
        caption=_["start_2"].format(message.from_user.mention, app.mention),
        reply_markup=InlineKeyboardMarkup(out),
    )

# ---------------- START GROUP -------------------
@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        random.choice(NEXIO),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)

# ---------------- WELCOME -------------------
@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)

            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass

            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)

                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    random.choice(NEXIO),
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)

# ======================================================
# ©️ 2025-26 All Rights Reserved by Revange 😎
