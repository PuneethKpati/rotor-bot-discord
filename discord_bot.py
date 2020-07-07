
import discord
from discord.ext import commands

class Rotor(commands.Bot):
	def __init__(self, command_prefix):
		super().__init__(command_prefix=command_prefix)

	async def on_ready(self):
		print('Rotor ready...')


token = open('token', 'r').read().strip()
rotor = Rotor(command_prefix='$')
rotor.run(token)