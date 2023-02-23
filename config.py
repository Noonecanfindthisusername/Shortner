# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "22098123"))
API_HASH = os.environ.get("API_HASH", "eafebcd50649f8769bd83ce1052c53e9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6119698518:AAGHeAGo-OW2M5YaKyuZwlpM_NHIS7nsdW8")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://luci:luci@cluster0.kazau1i.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1335205118")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001854675376")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "kingbotofficial") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://te.legra.ph/file/f6e6dbf63f9423627ac33.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
