import requests
import discord
from discord.ext import tasks, commands

import configManager

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)
client.db = ""


@client.event
async def on_ready():
    print("Bot has started")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a ton of ducks"))
    sendDuck.start()
    sendFact.start()


@tasks.loop(minutes = 1)
async def sendDuck():
    id = configManager.serverData["duckChannel"]
    channel = client.get_channel(id)
    response = requests.get("https://random-d.uk/api/v2/random").json()
    url = response.get('url')
    await channel.send(url)

@tasks.loop(minutes = 1)
async def sendFact():
    id = configManager.serverData["factChannel"]
    channel = client.get_channel(id)
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en").json()
    fact = response.get('text')
    await channel.send(fact)



try:
    client.run(configManager.botData["bottoken"])
except Exception as e:
    print("Something went wrong when starting the bot.")
    print(e)
