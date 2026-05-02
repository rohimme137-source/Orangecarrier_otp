import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from config import *

# ================= DRIVER =================
def create_driver():
    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(), options=options)
    return driver


# ================= TELEGRAM =================
def send_message(text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(url, data={
            "chat_id": ADMIN_CHAT_ID,
            "text": text
        }, timeout=10)

    except Exception as e:
        print("Telegram error:", e)


# ================= LOGIN =================
def login(driver):
    try:
        driver.get(BASE_URL)
        time.sleep(2)

        driver.get(LOGIN_URL)
        time.sleep(3)

        driver.find_element("name", "email").send_keys(ORANGE_EMAIL)
        driver.find_element("name", "password").send_keys(ORANGE_PASSWORD)

        driver.find_element("tag name", "button").click()
        time.sleep(5)

        print("Login success")

    except Exception as e:
        print("Login error:", e)


# ================= FETCH CALL =================
def get_calls(driver):
    try:
        driver.get(BASE_URL)
        time.sleep(2)

        driver.get(CALL_URL)
        time.sleep(3)

        rows = driver.find_elements("class name", "call-row")

        calls = []
        for r in rows:
            try:
                calls.append(r.text.strip())
            except:
                continue

        return calls

    except Exception as e:
        print("Fetch error:", e)
        return []


# ================= MAIN LOOP =================
def main():
    driver = create_driver()
    login(driver)

    seen_calls = set()

    while True:
        try:
            calls = get_calls(driver)

            for call in calls:
                if call not in seen_calls:
                    seen_calls.add(call)

                    msg = f"📞 New Call: {call}"
                    print(msg)

                    send_message(msg)

            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            print("Main loop error:", e)
            time.sleep(5)


if __name__ == "__main__":
    main()