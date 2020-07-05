import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMINS = [
    str(os.getenv("admin_id")),
]

URL_YOUTUBE = os.getenv("URL_YOUTUBE")
URL_GOOGLE = os.getenv("URL_GOOGLE")
URL_GIT = os.getenv("URL_GIT")

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("Db_PASS")
HOST = "localhost"

payment = os.getenv("PAYMENT_TOKEN")

I18N_DOMAIN = 'testbot'
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'

