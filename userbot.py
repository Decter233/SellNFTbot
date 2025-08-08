from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
owner_id = int(os.environ.get("OWNER_ID"))
session_string = os.environ.get("SESSION_STRING")

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    msg = event.message.message or ""
    sender = await event.get_sender()
    sender_name = sender.username or sender.first_name or "Unknown"
    print(f"[📩] Получено сообщение от {sender_name}: {msg}")

    if "t.me/gifts" in msg or "https://t.me/gifts" in msg or event.message.web_preview:
        print("[🎁] Найдена ссылка на подарок, пересылаю OWNER_ID...")
        await client.send_message(owner_id, "🎁 Подарок получен!")
        await event.message.forward_to(owner_id)
    else:
        print("[ℹ️] Ссылки на подарок не найдено, сообщение проигнорировано.")

print("✅ Userbot запущен.")
client.start()
client.run_until_disconnected()
