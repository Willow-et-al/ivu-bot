import discord
from discord.ext import commands

class Meta(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		with open('license-notice.txt') as f:
			self.license_notice = f.read()

	@commands.command()
	async def source(self, ctx):
		"""Sends you a link to the source code of this bot."""
		await ctx.send(self.bot.config['repo'])

	@commands.command()
	async def copyright(self, ctx):
		"""Tells you about the copyright license of this bot"""
		await ctx.send(self.license_notice)

async def setup(bot):
	await bot.add_cog(Meta(bot))
