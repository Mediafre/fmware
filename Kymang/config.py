#Kymang

import os

from dotenv import load_dotenv

load_dotenv(".env")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "6938657094:AAFpqnpOrg6Ne90WbhT_-FC8ieLd3UA6IRA")
API_ID = int(os.environ.get("API_ID", "17131033"))
API_HASH = os.environ.get("API_HASH", "7768488c115ac09684bb38e608c47997")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://rahdimas2:ZeHzZ3vmz8uD3mit@cluster0.v6muq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1734774709").split())]
MEMBER = [int(x) for x in (os.environ.get("MEMBER", "160").split())]
LOG_GRP = int(os.environ.get("LOG_GRP", "-1002061778178"))
BOT_ID = int(os.environ.get("BOT_ID", "6938657094"))

KITA = [int(x) for x in (os.environ.get("KITA", "1668766845").split())]
