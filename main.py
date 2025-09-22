import discord
from discord.ext import commands
import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot đang chạy!"

def run_web():
    app.run(host="0.0.0.0", port=8080)

# Chạy Flask song song
threading.Thread(target=run_web).start()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công với tên: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "hello":
        await message.channel.send("Xin chào :)")
        
    await bot.process_commands(message)

bot.run(TOKEN)
