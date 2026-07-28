import os
import sys
import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("TelegramInteractiveSetup")

def setup_and_test_telegram():
    print("\n=== TELEGRAM BOT CONFIGURATION WIZARD ===")
    bot_token = input("8844329469:AAGebHJye04B2iSQA99_jWvd-HB9N9Qqo44").strip()
    chat_id = input("8720676587: ").strip()
    
    if not bot_token or not chat_id:
        logger.error("Error: Bot Token and Chat ID cannot be empty!")
        return

    # Save permanently to local environment configuration file
    env_content = f"export TELEG_BOT_TOKEN='{bot_token}'\nexport TELEG_CHAT_ID='{chat_id}'\n"
    with open("telegram_credentials.env", "w") as f:
        f.write(env_content)
    
    logger.info("Credentials saved successfully to telegram_credentials.env!")
    
    # Test connection by sending a live message
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": "🚀 *Damodar Tech Craze Empire*: Telegram Alert Bridge successfully configured and connected!",
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            logger.info("SUCCESS: Test notification sent to your Telegram chat!")
        else:
            logger.error(f"Failed to verify Telegram credentials: {response.text}")
    except Exception as e:
        logger.error(f"Connection error: {e}")

if __name__ == "__main__":
    setup_and_test_telegram()
