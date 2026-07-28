import os
import sys
import json
import sqlite3
import logging
from datetime import datetime
from typing import Dict, Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("GlobalPaymentEngine")

DB_PATH = os.getenv("DB_PATH", "empire_global_master.db")

class GlobalEmpireDatabase:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS global_funnel (
                        lead_id TEXT PRIMARY KEY,
                        business_name TEXT,
                        market_region TEXT,
                        checkout_file TEXT,
                        amount_due TEXT,
                        status TEXT,
                        created_at TEXT
                    )
                """)
                conn.commit()
        except Exception as e:
            logger.critical(f"DB Error: {e}")
            raise

    def save_funnel(self, data: Dict[str, Any]):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT OR REPLACE INTO global_funnel (lead_id, business_name, market_region, checkout_file, amount_due, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (data["lead_id"], data["business_name"], data["market_region"], data["checkout_file"], data["amount_due"], data["status"], datetime.utcnow().isoformat())
                )
                conn.commit()
        except Exception as e:
            logger.error(f"Failed to save funnel: {e}")

db = GlobalEmpireDatabase(DB_PATH)

def generate_global_checkout_page(business_name: str, niche: str, region: str) -> Dict[str, Any]:
    """
    Generates localized checkout page based on region:
    - US/UK Market: $29 USD via PayPal.me or Crypto
    - India Metro Market: ₹999 INR via GPay/PhonePe/Canara UPI
    """
    slug = business_name.lower().replace(" ", "-")
    filename = f"checkout_{region.lower()}_{slug}.html"
    
    if region.upper() == "US":
        currency = "USD"
        amount = "$29.00"
        payment_instructions = """
            <b>1. PayPal Global:</b> <a href="https://paypal.me/damodartechcraze" target="_blank" style="color: #38bdf8;">paypal.me/damodartechcraze</a><br>
            <b>2. Crypto / Trust Wallet:</b> USDT / Multi-Chain Supported<br>
        """
    else:
        currency = "INR"
        amount = "₹999.00"
        payment_instructions = """
            <b>1. GPay / PhonePe UPI:</b> damodartechcraze@okaxis<br>
            <b>2. Canara Bank UPI:</b> 923698947@cnrbs<br>
            <b>3. Net Banking / QR Scan:</b> Instant Transfer<br>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instant Activation | {business_name}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }}
        .card {{ background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); width: 100%; max-width: 450px; border: 1px solid #334155; }}
        h2 {{ color: #38bdf8; margin-top: 0; font-size: 22px; }}
        .price-tag {{ font-size: 28px; font-weight: bold; color: #22c55e; margin: 15px 0; }}
        p {{ color: #94a3b8; font-size: 14px; line-height: 1.5; }}
        .pay-box {{ background: #0f172a; padding: 15px; border-radius: 8px; margin: 15px 0; border: 1px solid #475569; }}
        .pay-box b {{ color: #38bdf8; }}
        a {{ color: #38bdf8; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        button {{ background: #22c55e; color: #fff; border: none; padding: 14px; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 16px; margin-top: 10px; }}
        button:hover {{ background: #16a34a; }}
    </style>
</head>
<body>
    <div class="card">
        <h2>🚀 Instant Widget Deployment</h2>
        <p>Custom After-Hours Estimate Widget for <b>{business_name}</b></p>
        <div class="price-tag">Total Due: {amount}</div>
        <p>Select your payment method below to activate instantly:</p>
        
        <div class="pay-box">
            {payment_instructions}
        </div>

        <button onclick="alert('Payment notice received! Once processed via PayPal or UPI, your widget goes live permanently.');">I Have Paid - Activate Now</button>
    </div>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content.strip())
        
    logger.info(f"Generated regional checkout for [{region}] -> {filename}")
    return {"file": filename, "amount": amount}

def run_global_test():
    logger.info("Running global multi-region checkout generator test...")
    
    # Testing both US and India markets
    target_us = {"id": "LEAD_US_01", "name": "Austin Prime Plumbers", "niche": "Plumber", "region": "US"}
    target_in = {"id": "LEAD_IN_01", "name": "Mumbai Elite HVAC", "niche": "HVAC", "region": "IN"}
    
    for t in [target_us, target_in]:
        res = generate_global_checkout_page(t["name"], t["niche"], t["region"])
        db.save_funnel({
            "lead_id": t["id"],
            "business_name": t["name"],
            "market_region": t["region"],
            "checkout_file": res["file"],
            "amount_due": res["amount"],
            "status": "READY_FOR_OUTREACH"
        })
        
    logger.info("Global checkout generation tests completed successfully.")

if __name__ == "__main__":
    run_global_test()
