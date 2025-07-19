import asyncio
from aiogram import Bot

async def send_message_notification(name, telegram_user, message):
    from .config import BOT_TOKEN, CHAT_ID 
    
    bot = Bot(token=BOT_TOKEN)

    text = (
        f"📩 Новое сообщение с сайта!\n\n"
        f"👤 Имя: {name}\n"
        f"💬 Telegram: {telegram_user}\n"
        f"📝 Сообщение: {message}"
    )

    await bot.send_message(chat_id=CHAT_ID, text=text)
    await bot.session.close()