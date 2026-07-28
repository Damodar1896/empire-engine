import os
import sys
import time
import json
import sqlite3
import logging
import random
from datetime import datetime
from typing import Dict, Any, List

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("SafeScaleOmniEngine")

DB_PATH = os.getenv("DB_PATH", "empire_safe_scale.db")
BATCH_LIMIT = 5  # Safety batch limit per execution cycle to prevent spam flags

class SafeEmpireDatabase:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS safe_outreach_queue (
                        lead_id TEXT PRIMARY KEY,
                        business_name TEXT,
                        niche TEXT,
                        city TEXT,
                        demo_url TEXT,
                        outreach_status TEXT,
                        created_at TEXT
                    )
                """)
                conn.commit()
        except Exception as e:
            logger.critical(f"DB error: {e}")
            raise

    def get_pending_leads(self) -> List[Dict[str, Any]]:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT lead_id, business_name, niche, city, demo_url FROM safe_outreach_queue WHERE outreach_status = 'PENDING' LIMIT ?", (BATCH_LIMIT,))
                rows = cursor.fetchall()
                return [{"lead_id": r[0], "business_name": r[1], "niche": r[2], "city": r[3], "demo_url": r[4]} for r in rows]
        except Exception as e:
            logger.error(f"Failed to fetch queue: {e}")
            return []

    def mark_sent(self, lead_id: str, channel: str):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("UPDATE safe_outreach_queue SET outreach_status = ? WHERE lead_id = ?", (f"SENT_VIA_{channel.upper()}", lead_id))
                conn.commit()
        except Exception as e:
            logger.error(f"Failed to update status: {e}")

db = SafeEmpireDatabase(DB_PATH)

def seed_initial_leads():
    """Seeds target leads safely into local queue."""
    sample_leads = [
        {"name": "Austin Rapid Plumbing", "niche": "Plumbers", "city": "Austin, TX"},
        {"name": "Dallas Peak Roofers", "niche": "Roofers", "city": "Dallas, TX"},
        {"name": "Miami Frost HVAC", "niche": "HVAC", "city": "Miami, FL"},
        {"name": "Austin Spark Electric", "niche": "Electricians", "city": "Austin, TX"},
        {"name": "Dallas Safe Locksmiths", "niche": "Locksmiths", "city": "Dallas, TX"}
    ]
    with sqlite3.connect(DB_PATH) as conn:
        for lead in sample_leads:
            lead_id = f"SAFE_{abs(hash(lead['name']))}"
            slug = lead['name'].lower().replace(" ", "-")
            demo_url = f"https://instant-preview.autogen-bridge.io/{lead['niche'].lower()}/{slug}-live"
            conn.execute(
                "INSERT OR IGNORE INTO safe_outreach_queue (lead_id, business_name, niche, city, demo_url, outreach_status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (lead_id, lead['name'], lead['niche'], lead['city'], demo_url, "PENDING", datetime.utcnow().isoformat())
            )
        conn.commit()

def safe_dispatch_multichannel(lead: Dict[str, Any]):
    """Simulates safe multi-channel dispatch with human-like jitter delays and anti-ban controls."""
    business = lead["business_name"]
    niche = lead["niche"]
    demo = lead["demo_url"]
    
    # Safety jitter delay between channels
    jitter = random.uniform(1.5, 3.0)
    
    logger.info(f"Preparing secure dispatch for {business} ({niche})...")
    
    # Channel 1: Safe Email Payload Simulation
    email_text = f"Hi Team, built a free instant estimate widget for {business}. Test live: {demo}. Flat $29 setup if it converts after-hours leads."
    time.sleep(jitter)
    logger.info(f"[SECURE EMAIL SENT] -> To {business} | Preview: {demo}")
    db.mark_sent(lead["lead_id"], "email")
    
    # Channel 2: Safe SMS Payload Simulation
    sms_text = f"Hey {business}, check your free custom instant estimate widget here: {demo}"
    time.sleep(jitter)
    logger.info(f"[SECURE SMS DISPATCHED] -> To {business}")
    db.mark_sent(lead["lead_id"], "sms")

def run_safe_orchestration():
    logger.info("Initializing safe batch queue orchestration engine...")
    seed_initial_leads()
    
    pending_leads = db.get_pending_leads()
    if not pending_leads:
        logger.info("No pending leads in queue. System resting safely.")
        return
        
    logger.info(f"Fetched safety batch of {len(pending_leads)} leads for processing.")
    
    for lead in pending_leads:
        safe_dispatch_multichannel(lead)
        # Anti-ban interval gap between distinct target businesses
        time.sleep(random.uniform(2.0, 4.0))
        
    logger.info("Safe batch queue execution completed successfully without triggering limits.")

if __name__ == "__main__":
    run_safe_orchestration()
