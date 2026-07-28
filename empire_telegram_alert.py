import os
import sys
import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("TelegramAlertBridge")

def send_realtime_telegram_notification(message: str):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "8844329469:AAGebHJye04B2iSQA99_jWvd-HB9N9Qqo44")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "8720676587")

    if bot_token == "YOUR_BOT_TOKEN":
        logger.info(f"[SIMULATED TELEGRAM ALERT TO FOUNDER]: {message}")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            logger.info("SUCCESS: Real-time Telegram alert dispatched to founder!")
        else:
            logger.error(f"Failed to send Telegram alert: {response.text}")
    except Exception as e:
        logger.error(f"Telegram connection error: {e}")

if __name__ == "__main__":
    send_realtime_telegram_notification("🔥 *HOT CONVERSION*: A client just viewed the UPI/RTGS checkout portal for Mumbai Elite HVAC!")
