import os
import time
import logging
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("EmpireBackgroundWorker247")

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://zhdrghjygatcqsyjmvdl.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpoZHJnaGp5Z2F0Y3FzeWptdmRsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4NTA0MTU2MiwiZXhwIjoyMTAwNjE3NTYyfQ.siqScmP8G0RVCMLw_bOtxe8fRAEc5V_TgZZuIkHUD9s")

def run_background_loop():
    logger.info("🚀 24x7 Autopilot Background Worker Initialized...")
    
    # Sample micro-batch queue for background processing
    queue_tasks = [
        {"business": "Miami Roof Experts", "owner": "Carlos", "city": "Miami, FL", "action": "Scrape & Dispatch Demo"},
        {"business": "Dallas Fast Plumbers", "owner": "Mark", "city": "Dallas, TX", "action": "Follow-up Check"}
    ]
    
    for task in queue_tasks:
        logger.info(f"Processing Task: {task['action']} for {task['business']} ({task['city']})")
        # Simulating micro-batch delay to maintain 0% server load
        time.sleep(2)
        
    logger.info("SUCCESS: Micro-batch completed safely without server load. Worker on standby for next cycle.")

if __name__ == "__main__":
    run_background_worker = os.getenv("RUN_ONCE", "true")
    if run_background_worker == "true":
        run_background_loop()
    else:
        # Infinite loop for 24x7 cloud runner
        while True:
            run_background_loop()
            time.sleep(300) # Sleep for 5 minutes before next micro-batch
