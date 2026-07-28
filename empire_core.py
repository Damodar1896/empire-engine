import os
import sys
import time
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
logger = logging.getLogger("UltimateEmpirePaymentEngine")

DB_PATH = os.getenv("DB_PATH", "empire_master_scale.db")

class MasterPaymentDatabase:
    """Manages multi-payment options and 1-click frictionless client checkouts."""
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS master_client_funnel (
                        lead_id TEXT PRIMARY KEY,
                        business_name TEXT,
                        niche TEXT,
                        city TEXT,
                        local_demo_path TEXT,
                        selected_currency TEXT,
                        target_amount REAL,
                        payment_options TEXT,
                        status TEXT,
                        created_at TEXT
                    )
                """)
                conn.commit()
        except Exception as e:
            logger.critical(f"Database initialization error: {e}")
            raise

    def save_client_lead(self, data: Dict[str, Any]):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    """INSERT OR REPLACE INTO master_client_funnel 
                       (lead_id, business_name, niche, city, local_demo_path, selected_currency, target_amount, payment_options, status, created_at) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        data["lead_id"], data["business_name"], data["niche"], data["city"],
                        data["local_demo_path"], data["selected_currency"], data["target_amount"],
                        json.dumps(data["payment_options"]), data["status"], datetime.utcnow().isoformat()
                    )
                )
                conn.commit()
        except Exception as e:
            logger.error(f"Failed to save client lead: {e}")

db = MasterPaymentDatabase(DB_PATH)

def generate_frictionless_payment_widget(business_name: str, niche: str, city: str, amount: float, currency: str) -> Dict[str, Any]:
    """
    Generates a 1-click frictionless checkout page embedded with all 5 user payment methods:
    1. Google Pay / PhonePe UPI ID: damodartechcraze@okaxis
    2. Canara Bank UPI Handle: 923698947@cnrbs
    3. Direct QR Code Scans
    4. PayPal Global Checkout
    5. Crypto Trust Wallet / USDT / Dollar Support
    """
    slug = business_name.lower().replace(" ", "-")
    filename = f"checkout_{slug}.html"
    
    # User's exact payment handles integrated seamlessly
    payment_methods = {
        "gpay_phonepe_upi": "damodartechcraze@okaxis",
        "canara_bank_upi": "923698947@cnrbs",
        "paypal": "paypal.me/damodartechcraze (or direct account)",
        "crypto_trust_wallet": "USDT/Crypto Network Supported",
        "bank_transfer": "RTGS / NEFT / Net Banking Available"
    }
    
    # Frictionless HTML Checkout Page where exact amount is pre-filled
    checkout_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instant Activation & Setup | {business_name}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }}
        .card {{ background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); width: 100%; max-width: 450px; border: 1px solid #334155; }}
        h2 {{ color: #38bdf8; margin-top: 0; font-size: 22px; }}
        .price-tag {{ font-size: 28px; font-weight: bold; color: #22c55e; margin: 15px 0; }}
        p {{ color: #94a3b8; font-size: 14px; line-height: 1.5; }}
        .pay-box {{ background: #0f172a; padding: 15px; border-radius: 8px; margin: 15px 0; border: 1px solid #475569; }}
        .pay-box b {{ color: #38bdf8; }}
        button {{ background: #22c55e; color: #fff; border: none; padding: 14px; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 16px; margin-top: 10px; }}
        button:hover {{ background: #16a34a; }}
    </style>
</head>
<body>
    <div class="card">
        <h2>🚀 Instant Deployment Portal</h2>
        <p>Custom Instant Estimate Widget for <b>{business_name}</b> ({city})</p>
        <div class="price-tag">Total Due: {currency} {amount}</div>
        <p>Choose your preferred payment method below for instant 1-click activation:</p>
        
        <div class="pay-box">
            <b>1. GPay / PhonePe UPI:</b> damodartechcraze@okaxis<br>
            <b>2. Canara Bank UPI:</b> 923698947@cnrbs<br>
            <b>3. PayPal / Global:</b> Supported<br>
            <b>4. Crypto Trust Wallet:</b> USDT / Multi-Chain<br>
            <b>5. Net Banking / RTGS / NEFT:</b> Direct Bank Transfer
        </div>

        <button onclick="alert('Payment instruction verified! Once transferred, your widget goes live instantly on your domain.');">Confirm & Deploy Widget Now</button>
    </div>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(checkout_html.strip())
        
    logger.info(f"Frictionless 1-click checkout portal created for {business_name} -> {filename}")
    return {"path": filename, "options": payment_methods}

def run_master_orchestration():
    logger.info("Running Master Empire Pipeline with 5 Integrated Payment Gateways...")
    
    # Target lead simulation (Plumbers & Roofers in US Tier-1 Cities)
    lead = {
        "lead_id": "MASTER_LEAD_01",
        "business_name": "Austin Prime Plumbers",
        "niche": "Plumber",
        "city": "Austin, TX",
        "selected_currency": "USD",
        "target_amount": 29.00
    }
    
    checkout_data = generate_frictionless_payment_widget(
        lead["business_name"], lead["niche"], lead["city"], lead["target_amount"], lead["selected_currency"]
    )
    
    lead["local_demo_path"] = checkout_data["path"]
    lead["payment_options"] = checkout_data["options"]
    lead["status"] = "CHECKOUT_READY_FOR_CLIENT"
    
    db.save_client_lead(lead)
    logger.info(f"Master pipeline execution successful. Client checkout asset ready at: {checkout_data['path']}")

if __name__ == "__main__":
    run_master_orchestration()
