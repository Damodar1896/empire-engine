import os
import shutil

print("==================================================")
print("   DAMODAR EMPIRE: WORLD-CLASS UI GENERATOR       ")
print("==================================================")

DEPLOY_DIR = "netlify_production_ready"
if os.path.exists(DEPLOY_DIR):
    shutil.rmtree(DEPLOY_DIR)
os.makedirs(DEPLOY_DIR, exist_ok=True)

# 1. Generate Master Luxury Index Page
MASTER_INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Damodar Tech Craze | Intelligence. Precision. Scale.</title>
    <style>
        :root { bg-dark: #07090e; card-bg: #0f172a; accent: #3b82f6; text-main: #f8fafc; text-muted: #94a3b8; border-col: #1e293b; }
        body { background-color: #07090e; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; }
        header { display: flex; justify-content: space-between; align-items: center; padding: 20px 50px; border-bottom: 1px solid #1e293b; background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(10px); position: sticky; top: 0; z-index: 100; }
        .logo { font-size: 1.4rem; font-weight: 800; letter-spacing: -0.5px; color: #fff; text-decoration: none; }
        .logo span { color: #3b82f6; }
        .nav-links { display: flex; gap: 30px; font-size: 0.9rem; color: #94a3b8; }
        .nav-links a { color: #94a3b8; text-decoration: none; transition: color 0.2s; }
        .nav-links a:hover { color: #3b82f6; }
        
        .hero { text-align: center; padding: 80px 20px 40px 20px; }
        .hero h1 { font-size: 3.5rem; font-weight: 800; margin-bottom: 15px; letter-spacing: -1px; background: linear-gradient(135deg, #fff 0%, #94a3b8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .hero p { color: #94a3b8; font-size: 1.15rem; max-width: 700px; margin: 0 auto 40px auto; line-height: 1.6; }
        
        .search-container { max-width: 600px; margin: 0 auto 50px auto; }
        .search-box { width: 100%; padding: 16px 24px; background: #0f172a; border: 1px solid #334155; border-radius: 12px; color: #fff; font-size: 1rem; outline: none; transition: border-color 0.2s, box-shadow 0.2s; }
        .search-box:focus { border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2); }
        
        .grid-container { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 24px; padding: 0 20px 80px 20px; }
        .card { background: #0f172a; border: 1px solid #1e293b; border-radius: 16px; padding: 30px; transition: transform 0.2s, border-color 0.2s; display: flex; flex-direction: column; justify-content: space-between; }
        .card:hover { transform: translateY(-4px); border-color: #3b82f6; }
        .card-tag { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #3b82f6; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }
        .verified-badge { background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 10px; border-radius: 20px; font-size: 0.7rem; }
        .card h3 { font-size: 1.4rem; font-weight: 700; margin: 0 0 12px 0; color: #fff; }
        .card p { color: #94a3b8; font-size: 0.95rem; line-height: 1.5; margin-bottom: 25px; }
        .btn-explore { display: inline-flex; align-items: center; gap: 8px; color: #60a5fa; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: gap 0.2s; }
        .btn-explore:hover { gap: 12px; color: #93c5fd; }
        
        footer { text-align: center; padding: 40px; color: #64748b; font-size: 0.85rem; border-top: 1px solid #1e293b; }
    </style>
</head>
<body>
    <header>
        <a href="/" class="logo">Damodar Tech <span>Craze.</span></a>
        <div class="nav-links">
            <a href="/">Ecosystem Hub</a>
            <a href="/hubs/clickbank.html">Privileged Deals</a>
            <a href="/pseo/free-openai-api-key-generator-2026.html">Security Protocols</a>
        </div>
    </header>

    <div class="hero">
        <h1>Intelligence. Precision. Scale.</h1>
        <p>Access 45+ verified enterprise platforms, optimized autonomous protocols, and exclusive partner infrastructure curated for elite execution.</p>
        
        <div class="search-container">
            <input type="text" class="search-box" placeholder="Search platforms, tools, networks..." id="searchInput">
        </div>
    </div>

    <div class="grid-container" id="cardGrid">
        <!-- Card 1 -->
        <div class="card" data-name="clickbank">
            <div>
                <div class="card-tag">Digital Products <span class="verified-badge">✓ Verified 2026</span></div>
                <h3>ClickBank</h3>
                <p>Enterprise-grade review, performance benchmarking, and exclusive partner pricing structure.</p>
            </div>
            <a href="/hubs/clickbank.html" class="btn-explore">Initialize Partner Access &rarr;</a>
        </div>

        <!-- Card 2 -->
        <div class="card" data-name="digistore24">
            <div>
                <div class="card-tag">Global Marketplace <span class="verified-badge">✓ Verified 2026</span></div>
                <h3>DigiStore24</h3>
                <p>Automated global affiliate routing, high-conversion funnels, and instant payout protocols.</p>
            </div>
            <a href="/hubs/digistore24.html" class="btn-explore">Initialize Partner Access &rarr;</a>
        </div>

        <!-- Card 3 -->
        <div class="card" data-name="jvzoo">
            <div>
                <div class="card-tag">Digital Marketplace <span class="verified-badge">✓ Verified 2026</span></div>
                <h3>JVZoo</h3>
                <p>Real-time vendor integration, instant commission dispatch, and secure gateway management.</p>
            </div>
            <a href="/hubs/jvzoo.html" class="btn-explore">Initialize Partner Access &rarr;</a>
        </div>
    </div>

    <footer>
        &copy; 2026 Damodar Tech Craze. All rights reserved. Autonomous Empire Core.
    </footer>

    <script>
        const searchInput = document.getElementById('searchInput');
        const cards = document.querySelectorAll('.card');
        searchInput.addEventListener('input', (e) => {
            const val = e.target.value.toLowerCase();
            cards.forEach(card => {
                const text = card.innerText.toLowerCase();
                card.style.display = text.includes(val) ? 'flex' : 'none';
            });
        });
    </script>
</body>
</html>
"""

with open(os.path.join(DEPLOY_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(MASTER_INDEX_HTML)

# 2. Generate Interactive Sub-Hubs Inside /hubs/
HUBS_DIR = os.path.join(DEPLOY_DIR, "hubs")
os.makedirs(HUBS_DIR, exist_ok=True)

SUB_HUBS = [
    {"slug": "clickbank", "title": "ClickBank Enterprise Gateway", "desc": "Exclusive 2026 architecture analysis, performance metrics, and direct integration portal."},
    {"slug": "digistore24", "title": "DigiStore24 Global Marketplace Hub", "desc": "High-conversion affiliate pathways, automated checkout streams, and secure revenue tracking."},
    {"slug": "jvzoo", "title": "JVZoo Vendor & Affiliate Hub", "desc": "Instant commission networks, real-time telemetry, and secure partner authorization."}
]

SUB_HUB_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Damodar Tech Craze</title>
    <style>
        body {{ background-color: #07090e; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 60px 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; background: #0f172a; border: 1px solid #1e293b; padding: 50px; border-radius: 20px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7); }}
        .badge {{ display: inline-block; background: rgba(59, 130, 246, 0.1); color: #60a5fa; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; margin-bottom: 20px; border: 1px solid rgba(59, 130, 246, 0.2); }}
        h1 {{ font-size: 2.5rem; margin-top: 0; color: #fff; letter-spacing: -0.5px; }}
        p {{ color: #94a3b8; font-size: 1.1rem; line-height: 1.7; margin-bottom: 30px; }}
        .terminal-box {{ background: #020617; border: 1px solid #1e293b; padding: 20px; border-radius: 12px; font-family: monospace; color: #34d399; margin-bottom: 30px; font-size: 0.95rem; }}
        .btn {{ display: inline-block; background: #3b82f6; color: white; padding: 14px 30px; border-radius: 10px; text-decoration: none; font-weight: bold; transition: background 0.2s; }}
        .btn:hover {{ background: #2563eb; }}
        .back-link {{ display: block; margin-top: 25px; color: #94a3b8; text-decoration: none; font-size: 0.9rem; }}
        .back-link:hover {{ color: #fff; }}
    </style>
</head>
<body>
    <div class="container">
        <span class="badge">Verified Autonomous Node • 2026 Active</span>
        <h1>{title}</h1>
        <p>{desc}</p>
        
        <div class="terminal-box">
            STATUS: SECURE_TUNNEL_ACTIVE<br>
            ENCRYPTION: MILITARY_AES_256<br>
            ROUTING: DAMODAR_TECH_CRAZE_EDGE_NETWORK
        </div>

        <a href="https://{slug}.com" target="_blank" class="btn">Launch External Official Platform &rarr;</a>
        <a href="/" class="back-link">&larr; Return to Master Ecosystem Hub</a>
    </div>
</body>
</html>
"""

for hub in SUB_HUBS:
    file_path = os.path.join(HUBS_DIR, f"{hub['slug']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(SUB_HUB_TEMPLATE.format(title=hub['title'], desc=hub['desc'], slug=hub['slug']))
    print(f"[SUCCESS] Generated Sub-Hub -> /hubs/{hub['slug']}.html")

print("\n[COMPLETE] World-class luxury UI generated successfully!")
