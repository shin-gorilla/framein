import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # .env ファイルからトークン読み込み

TOKEN = os.getenv("DISCORD_TOKEN")

print(f"TOKEN読み込み結果: {TOKEN}")

intents = discord.Intents.default()
intents.message_content = True  # これを追加！
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send("やっほー！FrameIn、起動してるよ！")

bot.run(TOKEN)
