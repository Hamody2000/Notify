import requests
import time
import subprocess

BOT_TOKEN = "8368814819:AAHAN1mxeKFe4_jSqF7GQsr_nnX2H5tejDs"
CHAT_ID = "830229958"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_message(msg):
    try:
        requests.post(URL, data={"chat_id": CHAT_ID, "text": msg}, timeout=5)
        print("Message sent:", msg)
    except Exception as e:
        print("Send failed:", e)

def is_online():
    try:
        result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.PIPE)
        return result.returncode == 0
    except Exception:
        return False

last_state = None
while True:
    online = is_online()
    if last_state is None:
        last_state = online

    if not online and last_state:
        send_message("⚠️ النت فصل!")
    elif online and not last_state:
        send_message("✅ النت رجع!")

    last_state = online
    time.sleep(5)