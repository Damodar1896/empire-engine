import os
import shutil
import json

print("==================================================")
print("   DAMODAR EMPIRE: AFFILIATE LINK BINDING ENGINE  ")
print("==================================================")

DEPLOY_DIR = "netlify_production_ready"
if os.path.exists(DEPLOY_DIR):
    shutil.rmtree(DEPLOY_DIR)
os.makedirs(DEPLOY_DIR, exist_ok=True)

# Master Vault with Permanent Affiliate Tracking Links
AFFILIATE_VAULT = [
    {"name": "TotalSoft+ Core Suite", "cat": "TotalSoft+ Software", "url": "https://totalsoftplus.com/?aff=damodar_empire", "desc": "Flagship TotalSoft+ enterprise automation suite and high-performance digital toolkit."},
    {"name": "TotalSoft+ Funnel Builder", "cat": "TotalSoft+ Software", "url": "https://totalsoftplus.com/funnels?aff=damodar_empire", "desc": "Drag-and-drop high converting sales funnels powered by TotalSoft+ architecture."},
    {"name": "TotalSoft+ AI Writer & SEO", "cat": "TotalSoft+ Software", "url": "https://totalsoftplus.com/ai-writer?aff=damodar_empire", "desc": "Autonomous AI content generation and programmatic SEO scaling engine by TotalSoft+."},
    {"name": "TotalSoft+ Cloud Vault", "cat": "TotalSoft+ Software", "url": "https://totalsoftplus.com/cloud?aff=damodar_empire", "desc": "Secure cloud asset management and automated data synchronization platform."},
    {"name": "ClickBank", "cat": "Affiliate Network", "url": "https://www.clickbank.com/?aff=damodar_empire", "desc": "Enterprise-grade global affiliate marketplace and high-converting digital product network."},
    {"name": "DigiStore24", "cat": "Affiliate Network", "url": "https://www.digistore24.com/redir/damodar_empire", "desc": "Automated global affiliate routing, high-conversion funnels, and instant payout protocols."},
    {"name": "JVZoo", "cat": "Affiliate Network", "url": "https://www.jvzoo.com/ref/damodar_empire", "desc": "Real-time vendor integration and instant commission dispatch network."},
    {"name": "WarriorPlus", "cat": "Affiliate Network", "url": "https://warriorplus.com/o2/a/damodar_empire/0", "desc": "High-velocity digital product marketplace and affiliate software platform."},
    {"name": "ShareASale", "cat": "Affiliate Network", "url": "https://www.shareasale.com/m.cfm?u=damodar_empire", "desc": "Robust affiliate marketing network connecting global merchants and publishers."},
    {"name": "CJ Affiliate", "cat": "Affiliate Network", "url": "https://www.cj.com/ref/damodar_empire", "desc": "Leading global affiliate marketing network delivering scalable partnerships."},
    {"name": "OpenAI Platform", "cat": "AI & LLM", "url": "https://platform.openai.com", "desc": "Advanced artificial intelligence models, GPT-4o, and enterprise developer APIs."},
    {"name": "Anthropic Claude", "cat": "AI & LLM", "url": "https://console.anthropic.com", "desc": "Next-generation AI assistant and advanced reasoning models for developers."},
    {"name": "Groq Console", "cat": "AI & LLM", "url": "https://console.groq.com", "desc": "Ultra-fast LPU inference engine delivering lightning-speed token generation."},
    {"name": "DeepSeek Platform", "cat": "AI & LLM", "url": "https://platform.deepseek.com", "desc": "High-performance open-architecture reasoning models and developer endpoints."}
]

# Save Vault Config
with open(os.path.join(DEPLOY_DIR, "affiliate_vault.json"), "w", encoding="utf-8") as vf:
    json.dump(AFFILIATE_VAULT, vf, indent=4)

cards_html = ""
for p in AFFILIATE_VAULT:
    cards_html += f"""
        <div class="card" data-name="{p['name'].lower()}" data-cat="{p['cat'].lower()}">
            <div>
                <div class="card-tag">
                    <span>{p['cat']}</span>
                    <span class="verified-badge">★ Verified Secure</span>
                </div>
                <h3>{p['name']}</h3>
                <p>{p['desc']}</p>
            </div>
            <div class="card-footer">
                <a href="{p['url']}" target="_blank" class="btn-explore">Access Portal &rarr;</a>
            </div>
        </div>
    """

total_portals = len(AFFILIATE_VAULT)
whatsapp_link = "https://chat.whatsapp.com/FOhff0IDlQzKT3OJZV24BB?s=sh&p=a&mlu=0&ilr=0"
telegram_link = "https://t.me/damodartechcraze"

master_index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Damodar Tech Craze | Ultra-Luxury Enterprise & TotalSoft+ Ecosystem</title>
    <style>
        :root {{
            --bg-deep: #02040a;
            --bg-card: rgba(10, 15, 30, 0.75);
            --border-glass: rgba(255, 255, 255, 0.08);
            --border-glow: rgba(59, 130, 246, 0.4);
            --accent-blue: #3b82f6;
            --accent-glow: rgba(59, 130, 246, 0.5);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }}
        
        * {{ box-sizing: border-box; }}
        body {{
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0; padding: 0; overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(29, 78, 216, 0.22) 0%, transparent 45%),
                radial-gradient(circle at 85% 85%, rgba(147, 51, 234, 0.15) 0%, transparent 45%);
        }}
        
        header {{
            display: flex; justify-content: space-between; align-items: center;
            padding: 24px 60px; border-bottom: 1px solid var(--border-glass);
            background: rgba(2, 4, 10, 0.85); backdrop-filter: blur(20px);
            position: sticky; top: 0; z-index: 1000;
        }}
        
        .logo {{
            font-size: 1.6rem; font-weight: 900; letter-spacing: -0.5px;
            color: #fff; text-decoration: none; display: flex; align-items: center; gap: 10px;
        }}
        .logo span {{ color: var(--accent-blue); text-shadow: 0 0 25px rgba(59, 130, 246, 0.6); }}
        
        .nav-social {{ display: flex; gap: 15px; align-items: center; }}
        .social-btn {{
            background: rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.3);
            color: #60a5fa; padding: 8px 16px; border-radius: 20px; font-size: 0.82rem; font-weight: 600;
            text-decoration: none; transition: all 0.2s ease;
        }}
        .social-btn:hover {{ background: var(--accent-blue); color: #fff; box-shadow: 0 0 15px rgba(59, 130, 246, 0.5); }}
        
        .hero {{ text-align: center; padding: 100px 20px 40px 20px; max-width: 950px; margin: 0 auto; }}
        .hero h1 {{
            font-size: 4.2rem; font-weight: 900; margin-bottom: 20px; letter-spacing: -1.5px;
            background: linear-gradient(135deg, #ffffff 20%, #cbd5e1 70%, #60a5fa 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            text-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .hero p {{ color: var(--text-muted); font-size: 1.25rem; line-height: 1.6; margin-bottom: 45px; }}
        
        .search-container {{ max-width: 700px; margin: 0 auto 35px auto; position: relative; }}
        .search-box {{
            width: 100%; padding: 20px 30px; background: rgba(10, 15, 30, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 16px; color: #fff; font-size: 1.1rem; outline: none;
            backdrop-filter: blur(15px); transition: all 0.3s ease; box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.8);
        }}
        .search-box:focus {{ border-color: var(--accent-blue); box-shadow: 0 0 0 4px var(--accent-glow); }}
        .kbd-shortcut {{
            position: absolute; right: 20px; top: 50%; transform: translateY(-50%);
            background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15);
            padding: 4px 8px; border-radius: 6px; font-size: 0.75rem; color: #94a3b8; font-family: monospace;
        }}
        
        .filter-bar {{ display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; max-width: 1000px; margin: 0 auto 60px auto; padding: 0 20px; }}
        .filter-btn {{
            background: rgba(10, 15, 30, 0.6); border: 1px solid var(--border-glass); color: var(--text-muted);
            padding: 10px 22px; border-radius: 25px; font-size: 0.9rem; font-weight: 600; cursor: pointer; transition: all 0.25s ease;
        }}
        .filter-btn:hover, .filter-btn.active {{
            background: var(--accent-blue); color: #fff; border-color: var(--accent-blue); box-shadow: 0 0 25px rgba(59, 130, 246, 0.6);
        }}
        
        .grid-container {{
            max-width: 1350px; margin: 0 auto; display: grid;
            grid-template-columns: repeat(auto-fill, minmax(390px, 1fr)); gap: 30px; padding: 0 30px 80px 30px;
        }}
        
        .card {{
            background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 22px; padding: 38px;
            backdrop-filter: blur(16px); transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1); display: flex; flex-direction: column; justify-content: space-between;
            position: relative; overflow: hidden; box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
        }}
        .card::before {{
            content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 2px;
            background: linear-gradient(90deg, transparent, var(--accent-blue), transparent); opacity: 0; transition: opacity 0.3s ease;
        }}
        .card:hover {{ transform: translateY(-8px); border-color: var(--border-glow); box-shadow: 0 30px 60px -20px rgba(0, 0, 0, 0.9), 0 0 30px rgba(59, 130, 246, 0.25); }}
        .card:hover::before {{ opacity: 1; }}
        
        .card-tag {{ font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: var(--accent-blue); margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center; }}
        .verified-badge {{ background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 10px; border-radius: 20px; font-size: 0.7rem; border: 1px solid rgba(16, 185, 129, 0.2); }}
        
        .card h3 {{ font-size: 1.6rem; font-weight: 700; margin: 0 0 12px 0; color: #fff; }}
        .card p {{ color: var(--text-muted); font-size: 0.98rem; line-height: 1.6; margin-bottom: 35px; }}
        
        .card-footer {{ display: flex; justify-content: flex-end; align-items: center; border-top: 1px solid var(--border-glass); padding-top: 22px; }}
        .btn-explore {{
            display: inline-flex; align-items: center; gap: 8px; background: rgba(59, 130, 246, 0.12); color: #60a5fa;
            border: 1px solid rgba(59, 130, 246, 0.35); padding: 12px 26px; border-radius: 12px; text-decoration: none; font-weight: 600; font-size: 0.92rem; transition: all 0.25s ease;
        }}
        .btn-explore:hover {{ background: var(--accent-blue); color: #fff; box-shadow: 0 0 25px rgba(59, 130, 246, 0.7); transform: scale(1.02); }}
        
        .ai-concierge {{
            position: fixed; bottom: 30px; right: 30px; background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            color: white; padding: 16px 26px; border-radius: 30px; font-weight: bold; box-shadow: 0 15px 35px rgba(59, 130, 246, 0.5);
            cursor: pointer; z-index: 9999; display: flex; align-items: center; gap: 10px; border: 1px solid rgba(255,255,255,0.25);
            transition: transform 0.2s ease;
        }}
        .ai-concierge:hover {{ transform: scale(1.05); }}
        
        footer {{ text-align: center; padding: 60px; color: #64748b; font-size: 0.88rem; border-top: 1px solid var(--border-glass); background: rgba(2, 4, 10, 0.95); }}
    </style>
</head>
<body>
    <header>
        <a href="/" class="logo">Damodar Tech <span>Craze.</span></a>
        <div class="nav-social">
            <a href="{telegram_link}" target="_blank" class="social-btn">💬 Telegram Hub</a>
            <a href="{whatsapp_link}" target="_blank" class="social-btn" style="background: rgba(16, 185, 129, 0.1); border-color: rgba(16, 185, 129, 0.3); color: #34d399;">🟢 WhatsApp Community</a>
        </div>
    </header>

    <div class="hero">
        <h1>Intelligence. Precision. Scale.</h1>
        <p>Access TotalSoft+ software suites, verified enterprise affiliate networks, encrypted AI nodes, and high-performance monetization portals curated for elite execution.</p>
        
        <div class="search-container">
            <input type="text" class="search-box" placeholder="Search TotalSoft+, affiliate portals, AI models..." id="searchInput">
            <span class="kbd-shortcut">Cmd + K</span>
        </div>
    </div>

    <div class="filter-bar">
        <button class="filter-btn active" onclick="filterCategory('all')">All Portals ({total_portals})</button>
        <button class="filter-btn" onclick="filterCategory('totalsoft+')">TotalSoft+ Software</button>
        <button class="filter-btn" onclick="filterCategory('affiliate network')">Affiliate Networks</button>
        <button class="filter-btn" onclick="filterCategory('ai & llm')">AI & LLM Infrastructure</button>
    </div>

    <div class="grid-container" id="cardGrid">
        {cards_html}
    </div>

    <div class="ai-concierge" onclick="alert('Damodar AI Concierge: Welcome! All affiliate tracking hooks are fully bound and active.')">
        🤖 Damodar AI Concierge
    </div>

    <footer>
        &copy; 2026 Damodar Tech Craze. All rights reserved. Ultra-Luxury Autonomous Architecture.
    </footer>

    <script>
        const searchInput = document.getElementById('searchInput');
        const cards = document.querySelectorAll('.card');

        searchInput.addEventListener('input', (e) => {{
            const val = e.target.value.toLowerCase();
            cards.forEach(card => {{
                const text = card.innerText.toLowerCase();
                card.style.display = text.includes(val) ? 'flex' : 'none';
            }});
        }});

        document.addEventListener('keydown', (e) => {{
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {{
                e.preventDefault();
                searchInput.focus();
            }}
        }});

        function filterCategory(cat) {{
            document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            cards.forEach(card => {{
                const cardCat = card.getAttribute('data-cat');
                if (cat === 'all' || cardCat.includes(cat)) {{
                    card.style.display = 'flex';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}
    </script>
</body>
</html>
"""

with open(os.path.join(DEPLOY_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(master_index_html)

print("[SUCCESS] Affiliate Tracking Vault fully bound to all portal cards!")
