import os
import json

# ===== TELEGRAM =====
BOT_TOKEN = "8552186596:AAFZ6W1-t9P5gagS8DD-ecLh7lXLmzSsiPM"
ADMIN_CHAT_ID = 8569268347
GROUP_CHAT_ID = -1003843283210

# ===== ORANGE LOGIN =====
ORANGE_EMAIL = "rohimme137@gmail.com"
ORANGE_PASSWORD = "rohim0185"

# ===== URL CONFIG =====
LOGIN_URL = os.environ.get("LOGIN_URL", "https://www.orangecarrier.com/login")
CALL_URL = os.environ.get("CALL_URL", "https://www.orangecarrier.com/live/calls")
BASE_URL = os.environ.get("BASE_URL", "https://www.orangecarrier.com")

# ===== SETTINGS =====
HEADLESS = True
CHECK_INTERVAL = 10

# ===== COOKIES =====
cookies_env = os.environ.get("ORANGE_COOKIES", "[]")

try:
    ORANGE_COOKIES = json.loads(cookies_env)
except:
    ORANGE_COOKIES = []