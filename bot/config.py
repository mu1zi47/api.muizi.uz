from decouple import config

BOT_TOKEN = config("TELEGRAM_BOT_TOKEN", default="")
CHAT_ID = config("TELEGRAM_CHAT_ID", default="")