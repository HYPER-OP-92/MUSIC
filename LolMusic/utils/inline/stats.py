# ======================================================
# ©️ 2025-26 ᴘʀᴇᴍɪᴜᴍ ᴄᴏᴅᴇ ʙʏ ʀᴇᴠᴀɴɢᴇ 😎
# 🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : t.me/dmcatelegram
# 📢 ᴄʜᴀɴɴᴇʟ : t.me/dmcatelegram
# 🛠 ᴍᴏᴅɪғɪᴇᴅ sᴛᴀᴛs ᴜɪ ᴠᴇʀsɪᴏɴ
# =======================================================

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def stats_buttons(_, status):
    """
    Advanced Stats Buttons 
    Status: True if User is Sudo, False otherwise
    """
    # 🔘 Buttons for Regular Users
    not_sudo = [
        [
            InlineKeyboardButton(text="📊 " + _["SA_B_1"], callback_data="TopOverall")
        ],
        [
            InlineKeyboardButton(text="🗑️ " + _["CLOSE_BUTTON"], callback_data="close")
        ]
    ]

    # 🔘 Buttons for Sudo/Owners (More options)
    sudo = [
        [
            InlineKeyboardButton(text="⚙️ " + _["SA_B_2"], callback_data="bot_stats_sudo"),
            InlineKeyboardButton(text="📈 " + _["SA_B_3"], callback_data="TopOverall")
        ],
        [
            InlineKeyboardButton(text="🌐 ɢʟᴏʙᴀʟ sᴛᴀᴛs", callback_data="v_stats"), # Extra feature
            InlineKeyboardButton(text="🔄 ʀᴇғʀᴇsʜ", callback_data="stats_back") # Refresh option
        ],
        [
            InlineKeyboardButton(text="🗑️ " + _["CLOSE_BUTTON"], callback_data="close")
        ]
    ]
    
    # Return Layout based on status
    return InlineKeyboardMarkup(sudo) if status else InlineKeyboardMarkup(not_sudo)


def back_stats_buttons(_):
    """
    Stylish Back & Close Buttons Layout
    """
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="⬅️ " + _["BACK_BUTTON"],
                    callback_data="stats_back",
                ),
                InlineKeyboardButton(
                    text="🗑️ " + _["CLOSE_BUTTON"],
                    callback_data="close",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📢 sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ",
                    url="https://t.me/maanavbots"
                )
            ]
        ]
    )
    return upl

# ======================================================
# ⚡ ᴜᴘɢʀᴀᴅᴇᴅ ʙʏ : @dmcatelegram
# ======================================================
