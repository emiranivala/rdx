#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "23783378")
API_HASH  = os.environ.get("API_HASH", "1151425ad8d6fa61d47247f9ee841a37")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8026648489:AAHoNohfOVWIUosPqN6SyPecuhqwyyxQeX4") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))  # Default to 8000 if not set
