import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("TelegramDirectRun")

BOT_TOKEN = "8844329469:AAGebHJye04B2iSQA99_jWvd-HB9N9Qqo44"
CHAT_ID = "8720676587"

def send_test():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "🚀 *Damodar Tech Craze Empire*: Telegram Direct Bridge is 100% Active & Connected!",
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload, timeout=5)
    if response.status_code == 200:
        logger.info("SUCCESS: Live test notification successfully delivered to Telegram!")
    else:
        logger.error(f"Failed: {response.text}")

if __name__ == "__main__":
    send_test()
