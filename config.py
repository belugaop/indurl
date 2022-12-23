import os

from dotenv import load_dotenv
load_dotenv()

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID","5291894")) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH","e15ad5a64cb8bd39b2be463d0314295f") #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN","5575648699:AAHprS8RUMb7YwbvyRvpYlgceNFdyLWU3C8") # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS","1682338390").split(",")] if os.environ.get("ADMINS") else []

DATABASE_NAME = os.environ.get("DATABASE_NAME", "FlashlinkDB")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://9860tushar:9860tushar@cluster0.cp1t882.mongodb.net/?retryWrites=true&w=majority") # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID","5530214163")) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001673909252")) # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", False) # For Force Subscription
BROADCAST_AS_COPY = is_enabled((os.environ.get('BROADCAST_AS_COPY', "False")), False) # true if forward should be avoided
IS_PRIVATE = is_enabled(os.environ.get("IS_PRIVATE", 'False'), 'False') # true for private use and restricting users
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://github.com/PrinceStarLord/FLASHLINK-v2") # for upstream repo
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = is_enabled((os.environ.get('LINK_BYPASS', "False")), False) # if true, droplink urls will be bypassed 
BASE_SITE = os.environ.get("BASE_SITE", "flashlink.in") # your shortener site domain

# For Admin use
CHANNELS = is_enabled((os.environ.get('CHANNELS', "True")), True)
CHANNEL_ID = [int(i.strip()) for i in os.environ.get("CHANNEL_ID").split(" ")] if os.environ.get("CHANNEL_ID") else []

FORWARD_MESSAGE = is_enabled((os.environ.get('FORWARD_MESSAGE', "False")), False) # true if forwardd message to converted by reposting the post

#  Heroku Config for Dynos stats
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None) # your heroku account api from https://dashboard.heroku.com/account/applications
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None) # your heroku app name
HEROKU = bool(HEROKU_API_KEY and HEROKU_APP_NAME)

#  Replit Config for Hosting in Replit
REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None) # your replit username 
REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None) # your replit app name 
REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False

#  Koyeb Config for Hosting in Koyeb
KOYEB_USERNAME = os.environ.get("KOYEB_USERNAME", None) # your koyeb username 
KOYEB_APP_NAME = os.environ.get("KOYEB_APP_NAME", None) # your koyeb app name 
KOYEB = f"https://{KOYEB_APP_NAME}-{KOYEB_USERNAME}.koyeb.app/" if KOYEB_APP_NAME and KOYEB_USERNAME else False

PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

LOG_STR = "\nHeroku is {0}\n".format("Enabled" if HEROKU else "Disabled") + "Users {0} use this bot\n".format("cannot" if IS_PRIVATE else "can")
LOG_STR+= "Server URL: {0}".format(KOYEB or REPLIT or None)
