import discord,os
from dotenv import load_dotenv
from datetime import datetime

print("BOT BERHASIL")

load_dotenv()

with open('template.txt') as file:
    template = file.read()

client = discord.Client()

dc_key = os.getenv('DISCORD_BOT_API_KEY')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if not msg.guild:
        
        current_datetime = datetime.now()
        current_date_time = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
        print(f"[{current_date_time}]{msg.author.name}:{msg.content}\n")
        f = open("dm.log", "a")
        f.write(f"[{current_date_time}]{msg.author.name}:{msg.content}\n")
        f.close()
        print("========================================")
        try:
            if msg.content.startswith('!channel_id'):
                channel_id = int(msg.content.split()[1])
                with open('channels.list') as file:
                    channels = [int(line.rstrip()) for line in file]
                if channel_id in channels:
                    print(f'[{current_date_time}]Response to {msg.author.name}: Sorry, The channel with ID {channel_id} already registered\n')
                    await msg.channel.send(f'Sorry, The channel with ID {channel_id} already registered')
                    f = open("dm.log", "a")
                    f.write(f'[{current_date_time}]Response to {msg.author.name}: Sorry, The channel with ID {channel_id} already registered\n')
                    f.close()
                else:
                    try:
                        ch = client.get_channel(channel_id)
                        await ch.send(template)
                        f = open("channels.list", "a")
                        f.write("\n"+str(channel_id))
                        f.close()
                        print(f'[{current_date_time}]Response to {msg.author.name}: Your channel successfully registered with ID:{channel_id}\n')
                        await msg.channel.send(f'Your channel successfully registered with ID:{channel_id}')
                        f = open("dm.log", "a")
                        f.write(f'[{current_date_time}]Response to {msg.author.name}: Your channel successfully registered with ID:{channel_id}\n')
                        f.close()
                    except:
                        print(f'[{current_date_time}]Response to {msg.author.name}: Sorry, we couldn\'t access your channel with ID:{channel_id}\n')
                        await msg.channel.send(f'Sorry, we couldn\'t access your channel with ID:{channel_id}')
                        f = open("dm.log", "a")
                        f.write(f'[{current_date_time}]Response to {msg.author.name}: Sorry, we couldn\'t access your channel with ID:{channel_id}\n')
                        f.close()

            elif msg.content.startswith('!report'):
                txt = msg.content.replace('!report',"\n["+current_date_time+"]"+msg.author.name+":")
                f = open("reports.log", "a")
                f.write(txt)
                f.close()
                print(txt)
                await msg.channel.send("Thank you for reporting!")
            elif msg.author != client.user:
                print(f"[{current_date_time}]Response to {msg.author.name}: template response\n")
                await msg.channel.send(template)
                f = open("dm.log", "a")
                f.write(f'[{current_date_time}]Response to {msg.author.name}: template response\n')
                f.close()
        except discord.errors.Forbidden:
            pass
    else:
        pass
    

client.run(dc_key)