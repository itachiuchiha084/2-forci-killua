# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Gʀᴏᴜᴘ", url="https://t.me/+g1Fhpyvc6AJkODI1"),
            ],
            [
                InlineKeyboardButton(text="Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Help", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟸", url="https://t.me/+g1Fhpyvc6AJkODI1"),
            ],
            [InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟸", url="https://t.me/+g1Fhpyvc6AJkODI1"),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ʀᴇsᴛᴀʀᴛ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ʀᴇsᴛᴀʀᴛ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟸", url="https://t.me/+g1Fhpyvc6AJkODI1"),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ʀᴇsᴛᴀʀᴛ ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
