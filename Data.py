# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b>How to Use this Bot

  ❏ Commands for BOT Users
  ├ /start - Starts the Bot
  ├ /about - About this Bot
  ├ /help - Help this Bot Command
  ├ /ping - To check live bots
  └ /uptime - To see bot status

  ❏ Commands For BOT Admins
  ├ /logs - To view bot logs
  ├ /setvar - To set var with dibot command
  ├ /delvar - To remove var with dibot command
  ├ /getvar - To see one of the var with dibot command
  ├ /users - To view bot user statistics
  ├ /batch - To link more than one file
  ├ /speedtest - To test the bot server speed
  └ /broadcast - To send a broadcast message to the bot user
  
 👨‍💻 Developed by </b><a href='https://t.me/killua_og'>Killua</a>
"""

    close = [
        [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About this Bot:

 This is a Telegram Bot for storing posts or files that can be accessed via a special link.

  • Creator: @Killua_og

 👨‍💻 Developed by @Anime_Alliance
"""
