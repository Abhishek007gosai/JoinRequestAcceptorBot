from os import environ

API_ID = int(environ.get("API_ID", "29245477"))
API_HASH = environ.get("API_HASH", "0abc83883262245c90ca337b7a0375c4")
BOT_TOKEN = environ.get("BOT_TOKEN", "7404600334:AAEn3yC-YFYtdJ1IMdLa0UG6dv3y0w1Xzvs")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002456565415"))
ADMINS = int(environ.get("ADMINS", "7654385403"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "cluster0")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
