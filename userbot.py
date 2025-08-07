from telethon import TelegramClient, events
import os
import threading
from webserver import app

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
client = TelegramClient("userbot_session", api_id, api_hash)
OWNER_ID = int(os.environ.get("OWNER_ID"))

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    msg = event.message.message or ""
    if "t.me/gifts" in msg or event.message.web_preview:
        await client.send_message(OWNER_ID, "🎁 Подарок получен!")
        await event.message.forward_to(OWNER_ID)

def start_web():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=start_web).start()
    print("Userbot запущен")
    client.start()
    client.run_until_disconnected()
