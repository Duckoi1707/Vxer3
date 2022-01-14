from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Chất lượng âm thanh", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Âm lượng âm thanh", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Người dùng được ủy quyền", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Bảng điều khiển", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Đóng", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Cài Đặt**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Menu lệnh của người trợ giúp", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Cài đặt", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **Đây là{MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Menu lệnh của người trợ giúp", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Cài đặt", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Nhóm hỗ trợ", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Đây là {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Menu lệnh của người trợ giúp", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Cài đặt", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Kênh chính thức", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **Đây là {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Chất lượng âm thanh", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Âm lượng âm thanh", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Người dùng được ủy quyền", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Bảng điều khiển", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Đóng", callback_data="close"),
            InlineKeyboardButton(text="🔙 Quay lại", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Đặt lại âm lượng âm thanh 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Âm Lượng Thấp", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Âm Lượng Trung", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 Âm Lượng Cao", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Âm Lượng Khuếch Đại", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Âm lượng tùy chỉnh 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Quay Lại", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Cài Đặt**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼 Âm lượng tùy chỉnh 🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Cài Đặt**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Tất cả mọi người", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Quản Trị Viên", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Danh sách người dùng được ủy quyền", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Quay Lại", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Cài Đặt**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ Hoạt Động", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Quay Lại", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Cài Đặt**", buttons
