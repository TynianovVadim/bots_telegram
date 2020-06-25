import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMINS = [
    str(os.getenv("admin_id")),
]

URL_YOUTUBE = os.getenv("URL_YOUTUBE")
URL_GOOGLE = os.getenv("URL_GOOGLE")
URL_GIT = os.getenv("URL_GIT")

PG_HOST = os.getenv("PG_HOST")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
