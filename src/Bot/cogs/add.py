import discord
from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("ExampleCog is ready!")

    @discord.app_commands.command(name="ping", description="A simple ping command")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

async def setup(bot):
    cog = ExampleCog(bot)
    await bot.add_cog(cog)
    # 檢查是否已經註冊過指令
    if not bot.tree.get_command("ping"):
        bot.tree.add_command(cog.ping)