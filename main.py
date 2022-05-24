"""
This bot provide information on real time stock prices
"""

# Import varous packages.
import discord
import os
from dotenv import load_dotenv
from helper_function import get_link, getsearchresult

load_dotenv()

client = discord.Client()

# Message for when bot is in server.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="If I work, don't fix me."))
    print("{0.user} is online".format(client))
    

# Bot listens to messages and await specific command.
@client.event
async def on_message(message):
    # Bot only listens to user message.
    if message.author == client.user:
        return

    # Bot provides statement for comedic relif.
    if message.content == '.iwannatalk':
        await message.channel.send('you do not need me go talk to someone else, stupid.')
        print("message printed")


    #  Bot only takes action when provided with this statement.
    # The following will only work on the host computer.
    if message.content.startswith('.stock_open '):
        user_msg = message.content.split()
        print(user_msg)
        stock_name = user_msg[1]

        getsearchresult(stock_name)
        print("stock {} has been loaded to HOST".format(stock_name))

    # This will provide a link to the webpage.
    if message.content.startswith('.stock '):
        user_msg = message.content.split()
        print(user_msg)
        stock_name = user_msg[1]

        url_link = get_link(stock_name)
        await message.channel.send(url_link)
        print("stock {} has been loaded to SERVER".format(stock_name))

# Run Discord Bot.
client.run(os.getenv('TOKEN'))

