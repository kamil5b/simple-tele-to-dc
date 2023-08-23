import discord,os
from dotenv import load_dotenv
from datetime import datetime

print("BOT BERHASIL")

load_dotenv()

async def log_print(msg,txt,author=None, msg_send=False, file_name="dm.log"):
    current_datetime = datetime.now()
    current_date_time = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    print(f'[{current_date_time}]{author}: {txt}\n')
    if msg_send:
        await msg.channel.send(txt)
    f = open(file_name, "a")
    f.write(f'[{current_date_time}]{author}: {txt}\n')
    f.close()

with open('template.txt',encoding="utf-8") as file:
    template = file.read()

client = discord.Client()

dc_key = os.getenv('DISCORD_BOT_API_KEY')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if not msg.guild:

        await log_print(msg,msg.content,author=msg.author.name)
        print("========================================")
        try:
            if msg.content.startswith('!channel_id'):
                tmp = msg.content.split()[1]
                channel_id = 0
                try:
                    channel_id = int(tmp)
                except:
                    tmp_arr = tmp.split(sep="/")
                    try:
                        channel_id = int(tmp_arr[5])
                    except:
                        await log_print(msg,"Error occured.",author=f"Response to {msg.author.name}",msg_send=True)
                        return
                with open('channels.list') as file:
                    channels = [int(line.rstrip()) for line in file]
                if channel_id in channels:
                    await log_print(msg,f"Sorry, The channel with ID {channel_id} already registered\n",author=f"Response to {msg.author.name}",msg_send=True)
                else:
                    try:
                        #Check if channel can be registered
                        ch = client.get_channel(channel_id)
                        await ch.send(template)

                        #If can, then add to list
                        f = open("channels.list", "a")
                        f.write("\n"+str(channel_id))
                        f.close()

                        await log_print(msg,f'Your channel successfully registered with ID:{channel_id}',author=f"Response to {msg.author.name}",msg_send=True)

                    except:
                        await log_print(msg,f'Sorry, we couldn\'t access your channel with ID:{channel_id}',author=f"Response to {msg.author.name}",msg_send=True)

            elif msg.content.startswith('!report'):
                current_datetime = datetime.now()
                current_date_time = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
                txt = msg.content.replace('!report',"\n["+current_date_time+"]"+msg.author.name+":")
                f = open("reports.log", "a")
                f.write(txt)
                f.close()
                print(txt)
                await msg.channel.send("Thank you for reporting!")
            elif msg.author != client.user:
                await log_print(msg,'Template response',author=f"Response to {msg.author.name}")
                await msg.channel.send(template)
        except discord.errors.Forbidden:
            pass
        except:
            await log_print(msg, 'Error occured.',author=f"Response to {msg.author.name}",msg_send=True)
    else:
        pass
    

client.run(dc_key)