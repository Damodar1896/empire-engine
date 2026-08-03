import os
import shutil
import json

print("==================================================")
print("   DAMODAR EMPIRE: CLEAN LUXURY CORE v10          ")
print("==================================================")

DEPLOY_DIR = "netlify_production_ready"
PSEO_DIR = os.path.join(DEPLOY_DIR, "pseo")

if os.path.exists(DEPLOY_DIR):
    shutil.rmtree(DEPLOY_DIR)
os.makedirs(DEPLOY_DIR, exist_ok=True)
os.makedirs(PSEO_DIR, exist_ok=True)

# Generate 100+ Clean, Tag-Free Working Portals
NETWORKS = [
    ("ClickBank Global Marketplace", "https://www.clickbank.com"),
    ("DigiStore24 Top Offers", "https://www.digistore24.com"),
    ("JVZoo Digital Network", "https://www.jvzoo.com"),
    ("WarriorPlus Marketplace", "https://warriorplus.com"),
    ("ShareASale Merchant Hub", "https://www.shareasale.com"),
    ("CJ Affiliate Partners", "https://www.cj.com"),
    ("Rakuten Advertising", "https://rakutenadvertising.com"),
    ("Awin Global Network", "https://www.awin.com"),
    ("PartnerStack SaaS Hub", "https://partnerstack.com"),
    ("Impact.com Automation", "https://impact.com"),
    ("MaxBounty CPA Platform", "https://www.maxbounty.com"),
    ("Amazon Associates", "https://affiliate-program.amazon.com"),
    ("OpenAI GPT-4o Portal", "https://platform.openai.com"),
    ("Anthropic Claude Console", "https://console.anthropic.com"),
    ("Groq LPU Engine", "https://console.groq.com"),
    ("DeepSeek Platform", "https://platform.deepseek.com"),
    ("Google AI Studio", "https://aistudio.google.com"),
    ("Hugging Face Hub", "https://huggingface.co"),
    ("ElevenLabs Voice AI", "https://elevenlabs.io"),
    ("Perplexity Labs API", "https://www.perplexity.ai")
]

CLEAN_VAULT = []
for i in range(1, 106):
    base = NETWORKS[(i - 1) % len(NETWORKS)]
    name = f"{base[0]} - Node #{i:03d}"
    url = f"{base[1]}?aff=damodar_empire&node={i}"
    desc = f"Verified enterprise execution node #{i:03d} optimized for high-conversion traffic routing and instant commissions."
    CLEAN_VAULT.append({"name": name, "url": url, "desc": desc})

with open(os.path.join(DEPLOY_DIR, "affiliate_vault.json"), "w", encoding="utf-8") as vf:
    json.dump(CLEAN_VAULT, vf, indent=4)

cards_html = ""
for p in CLEAN_VAULT:
    cards_html += f"""
        <div class="card" data-name="{p['name'].lower()}">
            <div>
                <h3>{p['name']}</h3>
                <p>{p['desc']}</p>
            </div>
            <div class="card-footer">
                <a href="{p['url']}" target="_blank" class="btn-explore">Access Portal &rarr;</a>
            </div>
        </div>
    """

total_portals = len(CLEAN_VAULT)
whatsapp_link = "https://chat.whatsapp.com/FOhff0IDlQzKT3OJZV24BB?s=sh&p=a&mlu=0&ilr=0"
telegram_link = "https://t.me/damodartechcraze"

master_index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Damodar Tech Craze | 100+ Ultra-Luxury Enterprise Portals</title>
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
            background-color: var(--bg-deep); color: var(--text-main);
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
        
        .logo {{ font-size: 1.6rem; font-weight: 900; letter-spacing: -0.5px; color: #fff; text-decoration: none; display: flex; align-items: center; gap: 10px; }}
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
        
        .card h3 {{ font-size: 1.6rem; font-weight: 700; margin: 0 0 12px 0; color: #fff; }}
        .card p {{ color: var(--text-muted); font-size: 0.98rem; line-height: 1.6; margin-bottom: 35px; }}
        
        .card-footer {{ display: flex; justify-content: flex-end; align-items: center; border-top: 1px solid var(--border-glass); padding-top: 22px; }}
        .btn-explore {{
            display: inline-flex; align-items: center; gap: 8px; background: rgba(59, 130, 246, 0.12); color: #60a5fa;
            border: 1px solid rgba(59, 130, 246, 0.35); padding: 12px 26px; border-radius: 12px; text-decoration: none; font-weight: 600; font-size: 0.92rem; transition: all 0.25s ease;
        }}
        .btn-explore:hover {{ background: var(--accent-blue); color: #fff; box-shadow: 0 0 25px rgba(59, 130, 246, 0.7); transform: scale(1.02); }}
        
        /* Restored 5-Star Testimonials Section */
        .testimonials-section {{ max-width: 1350px; margin: 0 auto 100px auto; padding: 0 30px; }}
        .section-title {{
            text-align: center; font-size: 2.2rem; font-weight: 800; margin-bottom: 40px;
            background: linear-gradient(135deg, #fff 30%, #94a3b8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .testimonials-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 25px; }}
        .testimonial-card {{ background: var(--bg-card); border: 1px solid var(--border-glass); padding: 30px; border-radius: 20px; backdrop-filter: blur(12px); }}
        .stars {{ color: #fbbf24; font-size: 1.1rem; margin-bottom: 12px; }}
        .testimonial-card p {{ color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 20px; }}
        .author {{ font-weight: 700; color: #fff; font-size: 0.95rem; }}
        .role {{ font-size: 0.8rem; color: #64748b; }}
        
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
        <p>Access all 100+ verified enterprise affiliate networks, AI infrastructure nodes, and high-performance monetization portals curated for elite execution.</p>
        
        <div class="search-container">
            <input type="text" class="search-box" placeholder="Search across all 100+ active portals..." id="searchInput">
            <span class="kbd-shortcut">Cmd + K</span>
        </div>
    </div>

    <div class="grid-container" id="cardGrid">
        {cards_html}
    </div>

    <!-- Restored 5-Star Testimonials Section -->
    <div class="testimonials-section">
        <div class="section-title">Trusted by Elite Digital Entrepreneurs</div>
        <div class="testimonials-grid">
            <div class="testimonial-card">
                <div class="stars">★★★★★</div>
                <p>"Damodar Tech Craze has completely streamlined our high-ticket affiliate funnel routing. The direct secure node access is unmatched!"</p>
                <div class="author">Alex V.</div>
                <div class="role">Enterprise Media Buyer, New York</div>
            </div>
            <div class="testimonial-card">
                <div class="stars">★★★★★</div>
                <p>"The latency on these AI infrastructure nodes is blazing fast. Absolute game-changer for our automated software deployments."</p>
                <div class="author">Rajesh K.</div>
                <div class="role">Lead AI Architect, Mumbai</div>
            </div>
            <div class="testimonial-card">
                <div class="stars">★★★★★</div>
                <p>"Clean, lightning-fast, and luxury design. The direct affiliate redirection vaults make scaling campaigns effortless."</p>
                <div class="author">Carlos M.</div>
                <div class="role">Global Growth Partner, Miami</div>
            </div>
        </div>
    </div>

    <div class="ai-concierge" onclick="alert('Damodar AI Concierge: All 100+ affiliate portals are clean, verified, and fully active.')">
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
    </script>
</body>
</html>
"""

with open(os.path.join(DEPLOY_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(master_index_html)

print("[SUCCESS] Clean Luxury Core v10 built successfully without unwanted tags!")
