# Simple Telegram to Discord Bot
created by kamil5b.

## How it work?
We have 2 clients, one is the Telegram Client using [Telethon](https://github.com/LonamiWebs/Telethon) and [Discord.py](https://discordpy.readthedocs.io/en/stable/)
It based on python.
the core application for this program is the telebot.py which is running the Telethon client and using [Discord API](https://discord.com/developers/docs/intro) to send Telegram messages to registered Discord channels
All discord channels id to be sented with are registered in channels.list, you can add manually OR you can use the second client which is the dcbot.py
the dcbot.py its completely optional. It used for registering channel id to the list via dm.

## How to use
1. Clone this repository
2. Rename .env-example to .env
3. Fill in the .env :
 - TELEGRAM_API_ID= get your telegram API ID from : https://core.telegram.org/api/obtaining_api_id
 - TELEGRAM_API_HASH= get your telegram API HASH from : https://core.telegram.org/api/obtaining_api_id
 - TELEGRAM_SESSION_NAME= just fill it with whatever you want as long as there is no whitespace
 - DISCORD_BOT_API_KEY= get your Discord bot token
 - TELEGRAM_USERNAME= (OPTIONAL) if you want a specific username to fetch, put the username here for example : @BotFather
 - **IF YOU ARE NOT USING TELEGRAM_USERNAME, CHECK THE telebot.py TO CHANGE IT A LITTLE BIT**
4. Invite your discord bot in to your guild/server
 - Discord developer -> Applications -> Your bot name app -> OAuth2 -> URL Generator -> Select "bot" -> Select "Send Messages", "Embed Links", "Attach files"
 - Copy the generated URL below it
 - Go to the generated URL, and you invite the bot to your guild/server
5. Copy your discord channel id that your bot going to send the message
6. Write it in to the channels.list, you have two options here:
 - Paste it yourself into the channels.list OR
 - Run the dcbot.py and DM your bot with command : !channel_id xxxxx. replace the xxxxx with the channel id
7. Run the telebot.py
 - First time using you will be asked your phone number and the OTP just for the session
8. if you are using the dcbot.py, create template.txt to make a default text like "Thank you for using our bot"