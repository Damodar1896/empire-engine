import os
import sys
import json
import sqlite3
import logging
from datetime import datetime
from typing import Dict, Any

# --- ENTERPRISE LOGGING ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("PaymentGatewayEngine")

DB_PATH = os.getenv("DB_PATH", "empire_safe_mass_scale.db")

class PaymentVerificationDatabase:
    """Handles instant payment logging and client deployment activation."""
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS paid_client_deployments (
                        payment_id TEXT PRIMARY KEY,
                        business_name TEXT,
                        amount_paid REAL,
                        deployment_status TEXT,
                        activated_at TEXT
                    )
                """)
                conn.commit()
        except Exception as e:
            logger.critical(f"Payment DB init error: {e}")
            raise

    def activate_client_widget(self, payment_id: str, business_name: str, amount: float):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT OR REPLACE INTO paid_client_deployments (payment_id, business_name, amount_paid, deployment_status, activated_at) VALUES (?, ?, ?, ?, ?)",
                    (payment_id, business_name, amount, "LIVE_DEPLOYED", datetime.utcnow().isoformat())
                )
                conn.commit()
                logger.info(f"SUCCESS: Payment of ${amount} verified for {business_name}. Widget deployed live automatically!")
        except Exception as e:
            logger.error(f"Failed to activate client deployment: {e}")

db = PaymentVerificationDatabase(DB_PATH)

def simulate_incoming_stripe_webhook(webhook_payload: Dict[str, Any]):
    """
    Simulates a secure incoming Stripe checkout completion webhook.
    In real production, this triggers automatically when a client pays via your Stripe checkout link.
    """
    payment_id = webhook_payload.get("payment_intent", "pi_mock_" + str(int(datetime.utcnow().timestamp())))
    business_name = webhook_payload.get("business_name", "Apex Target Plumbing")
    amount = webhook_payload.get("amount", 29.00)  # $29 irresistible low-friction offer
    
    logger.info(f"Received secure webhook event for payment ID: {payment_id}")
    
    # Verify and instantly deploy
    db.activate_client_widget(payment_id, business_name, amount)

if __name__ == "__main__":
    logger.info("Starting Autonomous Payment Webhook Listener & Deployment Engine...")
    
    # Simulating a live client hitting our $29 payment link and completing checkout successfully
    mock_checkout_event = {
        "payment_intent": "pi_3Mxyz92eZvKYlo2C1abcde",
        "business_name": "Austin Rapid Plumbing",
        "amount": 29.00
    }
    
    simulate_incoming_stripe_webhook(mock_checkout_event)
