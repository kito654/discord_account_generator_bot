import discord
from discord.ext import commands, tasks
from settings import token

client = commands.Bot(command_prefix="$")


class accountgen(commands.Bot):

    def nordvpn1(self):
        @client.event
        async def on_message(message):
                try:
                    c = await message.author.create_dm()
                    if message.content.startswith('$nordvpn') :
                        if message.channel.type == discord.ChannelType.text:
                            r = open('nordvpn.txt', "r")
                            await c.send(r.readline())
                            data = r.read().splitlines(True)
                            open('nordvpn.txt', 'w').writelines(data[0:])

                    elif message.content.startswith('$disney'):
                        if message.channel.type == discord.ChannelType.text:
                            r = open('disney.txt', "r")
                            await c.send(r.readline())
                            data = r.read().splitlines(True)
                            open('disney.txt', 'w').writelines(data[0:])

                    elif message.content.startswith('$hulu'):
                        if message.channel.type == discord.ChannelType.text:
                            r = open('hulu.txt', "r")
                            await c.send(r.readline())
                            data = r.read().splitlines(True)
                            open('hulu.txt', 'w').writelines(data[0:])


                    elif message.content.startswith('$netflix'):
                        if message.content.type == discord.ChannelType.text:
                            r = open('netflix.txt', "r")
                            await c.send(r.readline())
                            data = r.read().splitlines(True)
                            open('netflix.txt', "w").writelines(data[0:])


                except discord.errors.HTTPException:
                    await c.send('Out of stock!')   

                except AttributeError:
                    pass

                #Problem with reading

    def on_ready(self):
        print('Ready!\n Free account generator bot made by Idk ee#0480 705432218553548830!\nEnjoy.')

    def run(self):
        self.on_ready()
        self.nordvpn1()

a = accountgen(command_prefix="$")
a.run()
client.run(token)

