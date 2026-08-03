import os
import shutil
import json

print("==================================================")
print("   DAMODAR EMPIRE: MASTER ECOSYSTEM BUILDER       ")
print("==================================================")

# Directories
SOURCE_WEB_DIR = "damodar_website"
OUTPUT_DIR = "netlify_production_ready"
PSEO_DIR = "generated_pseo_pages"

if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Copy Master Website UI
if os.path.exists(SOURCE_WEB_DIR):
    for item in os.listdir(SOURCE_WEB_DIR):
        s = os.path.join(SOURCE_WEB_DIR, item)
        d = os.path.join(OUTPUT_DIR, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    print("[SUCCESS] Master Luxury UI copied to production deployment folder.")
else:
    print("[WARNING] damodar_website folder not found!")

# 2. Integrate pSEO Money Pages inside the deployment folder
if os.path.exists(PSEO_DIR):
    pseo_dest = os.path.join(OUTPUT_DIR, "pseo")
    os.makedirs(pseo_dest, exist_ok=True)
    for file in os.listdir(PSEO_DIR):
        if file.endswith(".html"):
            shutil.copy2(os.path.join(PSEO_DIR, file), os.path.join(pseo_dest, file))
    print("[SUCCESS] All pSEO money pages integrated successfully under /pseo/ route.")

print("\n[COMPLETE] Master Ecosystem built cleanly and ready for Netlify production deployment!")
