from dotenv import load_dotenv
import os
import requests
from telethon import TelegramClient, events

load_dotenv()


session_name = os.getenv('TELEGRAM_SESSION_NAME')
api_id = int(os.getenv('TELEGRAM_API_ID'))
api_hash = os.getenv('TELEGRAM_API_HASH')
dc_key = os.getenv('DISCORD_BOT_API_KEY')
tele_username = os.getenv('TELEGRAM_USERNAME')

client = TelegramClient(session_name, api_id, api_hash)

print("TELEGRAM CLIENT ON",session_name)

def send_dc(msg,media=None):
    with open('channels.list') as file:
        channels = [int(line.rstrip()) for line in file]
    headers = {
        #'Content-Type': 'multipart/form-data',
        'authorization': f"Bot {dc_key}"
        }
    
    payload = {
        "content":msg
    }

    if media is not None:
        print(media)
        
        print("ada media")
        for id in channels:
            try:
                m = open('./'+media, 'rb')
                files = {
                    "file" : (media[6:], m, 'image/jpeg')
                }
                requests.post(f"https://discord.com/api/v10/channels/{id}/messages", data=payload, headers=headers, files=files)
                print(id)
            except:
                print("fail to send to",id)

    else:
        print("Tidak ada Media")
        for id in channels:
            try:
                requests.post(f"https://discord.com/api/v10/channels/{id}/messages", data=payload, headers=headers)
                print(id)
            except:
                print("fail to send to",id)

#USE THIS IF YOU DON'T WANT A SPECIFIC TELEGRAM USERNAME ID RECIEVER (RECIEVE ALL)
#@client.on(events.NewMessage)

#USE THIS IF YOU WANT A SPECIFIC TELEGRAM USERNAME ID RECIEVER
@client.on(events.NewMessage(chats=tele_username))
async def my_event_handler(event):
    print("============================")
    msg_id = event.id
    texts = event.text
    raw_text = texts.replace('[🔗','🔗[')
    file_name = str(msg_id) + '.tlmsg'
    if event.photo:
        # shorthand for client.download_media(event.message, file_name)
        media_name = "media/" + str(msg_id) + '.jpg'
        print("Media saved on",media_name)
        await event.download_media(media_name)
        send_dc(raw_text,media=media_name)
    else:
        send_dc(raw_text)
    print("succeed")
    print(raw_text)
    f = open("message/"+file_name, "w",encoding="utf-8")
    f.write(raw_text)
    f.close()

client.start()
client.run_until_disconnected()
