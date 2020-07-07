
import discord
from discord.ext import commands

token = open('token', 'r').read().strip()

rotor = commands.Bot(command_prefix='$')

@rotor.event
async def on_ready():
	print('Rotor ready...')

rotor.run(token)