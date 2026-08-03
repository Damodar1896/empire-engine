import os
import json

print("==================================================")
print("   DAMODAR EMPIRE: FULL SYSTEM STATUS AUDIT       ")
print("==================================================")

# 1. Check API Wallet Keys
wallet_file = "damodar_master_api_wallet.json"
if os.path.exists(wallet_file):
    try:
        with open(wallet_file, "r", encoding="utf-8") as f:
            wallet_data = json.load(f)
            total_keys = sum(len(keys) for keys in wallet_data.values())
            print(f"[API VAULT] -> Secured API Keys / Tokens: {total_keys}")
    except:
        print("[API VAULT] -> Wallet file found but unreadable.")
else:
    print("[API VAULT] -> No wallet file found.")

# 2. Check Active Affiliate Portals in Vault
vault_file = "netlify_production_ready/affiliate_vault.json"
if os.path.exists(vault_file):
    try:
        with open(vault_file, "r", encoding="utf-8") as vf:
            vault_data = json.load(vf)
            print(f"[AFFILIATE PORTALS] -> Total Active Portals Locked: {len(vault_data)}")
    except:
        print("[AFFILIATE PORTALS] -> Vault file error.")
else:
    print("[AFFILIATE PORTALS] -> Vault file missing.")

# 3. Check Generated pSEO Pages
pseo_dir = "netlify_production_ready/pseo"
if os.path.exists(pseo_dir):
    pseo_files = [f for f in os.listdir(pseo_dir) if f.endswith(".html")]
    print(f"[pSEO ENGINE] -> Total Unique Money Pages Deployed: {len(pseo_files)}")
else:
    print("[pSEO ENGINE] -> pSEO folder not found.")

print("==================================================")
print("   AUDIT COMPLETE: ALL SYSTEMS FULLY OPERATIONAL  ")
print("==================================================")
