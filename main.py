import os
import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

# Load .env values
load_dotenv()
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

bot.send_message(chat_id="@YourChannelUsername", text="Bot is active ✅")

# Keep Render service alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running on Render!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run_web).start()

# Start Telegram bot
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# 🔹 Replace with the usernames or IDs of the channels you want to monitor
SOURCE_CHANNELS = ['@thelorenzotrader', '@Magic Trader Signals','@Dream Signals-Free Group']

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def signal_handler(event):
    """When a new message appears in your chosen channels."""
    message = event.message.message
    print(f"📩 New Signal:\n{message}")

    # You can forward the signal to your own channel, for example:
    target_channel = 'TestSignals123'
    await client.send_message(target_channel, f"📊 Copied Signal:\n{message}")

async def main():
    print("✅ Bot is active and listening for new signals...")
    await client.run_until_disconnected()

asyncio.run(main())


