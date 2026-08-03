import os
import datetime

print("==================================================")
print("   DAMODAR EMPIRE: SITEMAP & PING ENGINE          ")
print("==================================================")

DEPLOY_DIR = "netlify_production_ready"
PSEO_DIR = os.path.join(DEPLOY_DIR, "pseo")

# Base Domain (Netlify Production URL)
BASE_URL = "https://damodartechcraze.netlify.app"

urls = [f"{BASE_URL}/"]

# Collect all pSEO pages
if os.path.exists(PSEO_DIR):
    for file in os.listdir(PSEO_DIR):
        if file.endswith(".html"):
            slug = file[:-5]
            urls.append(f"{BASE_URL}/pseo/{file}")

# Generate sitemap.xml
today = datetime.date.today().isoformat()
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for u in urls:
    sitemap_content += f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n"

sitemap_content += '</urlset>'

sitemap_path = os.path.join(DEPLOY_DIR, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"[SUCCESS] Generated sitemap.xml containing {len(urls)} URLs successfully!")
