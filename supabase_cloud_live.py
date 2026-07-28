import os
import logging
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SupabaseCloudLiveEngine")

# Supabase Cloud Credentials with Straight Quotes
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://zhdrghjygatcqsyjmvdl.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpoZHJnaGp5Z2F0Y3FzeWptdmRsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4NTA0MTU2MiwiZXhwIjoyMTAwNjE3NTYyfQ.siqScmP8G0RVCMLw_bOtxe8fRAEc5V_TgZZuIkHUD9s")

def push_lead_to_supabase(business_name: str, owner_name: str, city: str, status: str):
    """Pushes lead pipeline status directly to Supabase Cloud PostgreSQL DB (Demo Sent -> Clicked -> Paid)"""
    payload = {
        "business_name": business_name,
        "owner_name": owner_name,
        "city": city,
        "status": status,
        "brand_name": "Damodar Tech Craze Ventures"
    }
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    url = f"{SUPABASE_URL}/rest/v1/empire_leads"
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)
        if response.status_code in [200, 201]:
            logger.info(f"SUCCESS: Lead [{business_name}] safely synced to Supabase Cloud Database!")
            return True
        else:
            logger.error(f"Cloud sync failed: {response.text}")
            return False
    except Exception as e:
        logger.error(f"Supabase connection error: {e}")
        return False

if __name__ == "__main__":
    logger.info("Initializing Supabase Cloud Connection...")
    push_lead_to_supabase("Mumbai Elite HVAC", "Rajesh", "Mumbai", "Demo Sent")
    push_lead_to_supabase("Austin Prime Plumbers", "David", "Austin, TX", "Checkout Viewed")
    logger.info("Step 1 Complete: Supabase Cloud Database bridge is fully configured!")
