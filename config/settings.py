import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")