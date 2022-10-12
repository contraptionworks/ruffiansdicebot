# IMPORT DISCORD.PY FOR API
import discord
from discord import app_commands

# OS MODULE (FOR .ENV FILE)
import os

# IMPORT LOAD_DOTENV.
from dotenv import load_dotenv

# LOADS LOCAL .ENV FILE
load_dotenv()

# DISCORD API TOKEN FROM .ENV FILE.
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# DISCORD GUILD FROM .ENV FILE.
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

# RANDOM NUMBER GENERATOR
from random import randint

# ROLL A DIE
def roll():
	return(randint(1, 6))

# MAIN DICE LOOP
def dice_results(b, p):

    #SET LOCAL VARIABLES
    base_dice = b
    push_dice = p

    # ENSURES DICE NUMBERS ARE IN RANGE
    if (base_dice) > 5:
        return ("*Error: Use 1-5 base dice and 0-2 push dice.*")
    elif (base_dice) < 1:
        return ("*Error: Use 1-5 base dice and 0-2 push dice.*")
    elif (push_dice) > 2:
        return ("*Error: Use 1-5 base dice and 0-2 push dice.*")
    elif (push_dice) < 0:
        return ("*Error: Use 1-5 base dice and 0-2 push dice.*")

    # ROLLS BASE DICE AND LISTS RESULTS
    base_dice_results = []
    i=0
    while i < (base_dice):
        base_dice_results.append(roll())
        i = i + 1

    # ROLLS PUSH DICE AND LISTS RESULTS
    push_dice_results = []
    i=0
    while i < (push_dice):
        push_dice_results.append(roll())
        i = i + 1

    # LISTS DICE RESULTS AND INTERPRETATIONS AND RETURNS AS STRING
    mylist=[base_dice_results, push_dice_results, "\n", interpret_main(base_dice_results, push_dice_results), interpret_setback(push_dice_results)]
    mystring=' '.join(map(str,mylist))
    return(mystring)

# INTERPRETS HITS AND MISSES
def interpret_main(b, p):
    if ((b + p).count(6)) > 1:
        return("Critical Hit!")
    elif ((b + p).count(6)) == 1:
        return("Strong Hit!")
    elif ((b + p).count(5)) > 0:
        return("Weak Hit!")
    else:
        return("Miss!")

# INTERPRETS SETBACKS
def interpret_setback(p):
    if (p.count(1)) > 1:
        return("Two Setbacks!")
    elif (p.count(1)) > 0:
        return("One Setback!")
    else:
        return("")

# SLASH COMMAND CODE
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id = DISCORD_GUILD))
            self.Synced = True
        print(f"{self.user} has logged in.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "rd", description = "Ruffians Dice", guild = discord.Object(id = DISCORD_GUILD))
async def self(interaction: discord.Interaction, base: int, push: int):
    await interaction.response.send_message(dice_results(base, push))

# DISCORD APP TOKEN
client.run(DISCORD_TOKEN)
