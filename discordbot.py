import discord
from viewbot import *


client = discord.Client()


@client.event
async def on_ready():
    print("~~~~~~~~~~~~~")
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('~~~~~~~~~~~~~')


@client.event
async def on_message(message):
    if message.content.startswith('!viewbot'):
        link = message.content.split(' ')[1]
        num_views = int(message.content.split(' ')[2])
        views(link,num_views)
        embed = discord.Embed(title='eBay View Bot', description=f'{num_views} views sent to {link}', color=0xFFFFF0)
        embed.set_footer(text='made by yggloo', icon_url ='https://i.ibb.co/sggQ5Sr/gnu.png')
        await message.channel.send(embed=embed)

client.run('put your token here')