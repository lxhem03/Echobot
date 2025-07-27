from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "demo_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text("👋 Hello! I'm alive. Send me any message!")

@app.on_message(filters.command("help"))
async def help(_, message: Message):
    await message.reply_text("This is a Pyrogram demo bot.\nSend a message and I'll echo it back.")

@app.on_message(filters.text & ~filters.command(["start", "help"]))
async def echo(_, message: Message):
    await message.reply_text(f"You said: {message.text}")

if __name__ == "__main__":
    print("Bot is running...")
    app.run()
