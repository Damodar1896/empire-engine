import os
import shutil

print("==================================================")
print("   DAMODAR EMPIRE: ULTRA-LUXURY v3 MASTER CORE    ")
print("==================================================")

DEPLOY_DIR = "netlify_production_ready"
if os.path.exists(DEPLOY_DIR):
    shutil.rmtree(DEPLOY_DIR)
os.makedirs(DEPLOY_DIR, exist_ok=True)

# Master Database with Affiliate Tracking Links & Metadata
MASTER_ECOSYSTEM = [
    # Affiliate Networks (With placeholder affiliate tracking hooks)
    {"name": "ClickBank", "cat": "Affiliate Network", "url": "https://www.clickbank.com/?aff=damodar_craze", "desc": "Enterprise-grade global affiliate marketplace and digital product network.", "payout": "Weekly / Net-15"},
    {"name": "DigiStore24", "cat": "Affiliate Network", "url": "https://www.digistore24.com/redir/damodar_empire", "desc": "Automated global affiliate routing, high-conversion funnels, and instant payouts.", "payout": "Instant / Bi-Weekly"},
    {"name": "JVZoo", "cat": "Affiliate Network", "url": "https://www.jvzoo.com/ref/damodar", "desc": "Real-time vendor integration and instant commission dispatch network.", "payout": "Instant PayPal"},
    {"name": "WarriorPlus", "cat": "Affiliate Network", "url": "https://warriorplus.com/o2/a/damodar/0", "desc": "High-velocity digital product marketplace and affiliate software platform.", "payout": "Instant Wallet"},
    {"name": "ShareASale", "cat": "Affiliate Network", "url": "https://www.shareasale.com/m.cfm?u=damodar", "desc": "Robust affiliate marketing network connecting merchants and publishers.", "payout": "Monthly Net-30"},
    {"name": "CJ Affiliate", "cat": "Affiliate Network", "url": "https://www.cj.com/ref/damodar", "desc": "Leading global affiliate marketing network delivering scalable partnerships.", "payout": "Direct Deposit"},
    {"name": "Rakuten Advertising", "cat": "Affiliate Network", "url": "https://rakutenadvertising.com?ref=damodar", "desc": "Global performance marketing and partner network for top tier brands.", "payout": "Reliable Net-30"},
    {"name": "Awin", "cat": "Affiliate Network", "url": "https://www.awin.com/?ref=damodar", "desc": "Global affiliate network powering profitable business partnerships.", "payout": "Flexible Payouts"},
    {"name": "PartnerStack", "cat": "SaaS Affiliate", "url": "https://partnerstack.com/?ref=damodar", "desc": "The #1 affiliate and partner ecosystem for B2B SaaS companies.", "payout": "Stripe / PayPal"},
    {"name": "Impact.com", "cat": "Affiliate Network", "url": "https://impact.com/?ref=damodar", "desc": "Partnership automation platform transforming how enterprises grow.", "payout": "Multi-Currency"},
    {"name": "MaxBounty", "cat": "CPA Network", "url": "https://www.maxbounty.com/?ref=damodar", "desc": "Top-tier performance-based CPA affiliate network worldwide.", "payout": "Weekly Net-7"},
    {"name": "Amazon Associates", "cat": "E-Commerce", "url": "https://affiliate-program.amazon.com/?tag=damodar0f-20", "desc": "World's largest e-commerce monetization and affiliate ecosystem.", "payout": "Direct Deposit"},
    
    # AI & LLM Infrastructure
    {"name": "OpenAI Platform", "cat": "AI & LLM", "url": "https://platform.openai.com", "desc": "Advanced artificial intelligence models, GPT-4o, and developer APIs.", "payout": "Developer API"},
    {"name": "Anthropic Claude", "cat": "AI & LLM", "url": "https://console.anthropic.com", "desc": "Next-generation AI assistant and advanced reasoning models.", "payout": "Enterprise Tier"},
    {"name": "Groq Console", "cat": "AI & LLM", "url": "https://console.groq.com", "desc": "Ultra-fast LPU inference engine for lightning-speed token generation.", "payout": "Hardware Accelerated"},
    {"name": "DeepSeek Platform", "cat": "AI & LLM", "url": "https://platform.deepseek.com", "desc": "High-performance open-architecture reasoning models.", "payout": "Low Cost API"},
    {"name": "Google AI Studio", "cat": "AI & LLM", "url": "https://aistudio.google.com", "desc": "Gemini 1.5 Pro developer platform for multimodal applications.", "payout": "Google Cloud"},
    {"name": "OpenRouter", "cat": "AI Aggregator", "url": "https://openrouter.ai", "desc": "Unified interface and router for accessing global language models.", "payout": "Unified Billing"},
    {"name": "Perplexity Labs", "cat": "AI Search", "url": "https://www.perplexity.ai", "desc": "Conversational search and real-time knowledge discovery APIs.", "payout": "API Credits"},
    {"name": "Together AI", "cat": "Cloud AI", "url": "https://www.together.ai", "desc": "Decentralized cloud platform for running open-source AI models.", "payout": "Cloud Compute"},
    {"name": "Hugging Face", "cat": "AI Hub", "url": "https://huggingface.co", "desc": "The AI community building the future of machine learning.", "payout": "Open Access"},
    {"name": "Replicate", "cat": "AI Deployment", "url": "https://replicate.com", "desc": "Run open-source machine learning models with cloud APIs.", "payout": "Pay-per-second"},
    {"name": "ElevenLabs", "cat": "Voice AI", "url": "https://elevenlabs.io", "desc": "Generative voice AI producing ultra-realistic synthetic human speech.", "payout": "Creator Tier"},
    {"name": "Midjourney", "cat": "Image AI", "url": "https://www.midjourney.com", "desc": "Independent research lab producing state-of-the-art generative images.", "payout": "Subscription"}
]

CARDS_HTML = ""
for idx, p in enumerate(MASTER_ECOSYSTEM, 1):
    CARDS_HTML += f"""
        <div class="card" data-name="{p['name'].lower()}" data-cat="{p['cat'].lower()}">
            <div>
                <div class="card-tag">
                    <span>{p['cat']}</span>
                    <span class="verified-badge">⚡ {p['payout']}</span>
                </div>
                <h3>{p['name']}</h3>
                <p>{p['desc']}</p>
            </div>
            <div class="card-footer">
                <span class="node-id">NODE #{idx:02d}</span>
                <a href="{p['url']}" target="_blank" class="btn-explore">Launch Portal &rarr;</a>
            </div>
        </div>
    """

ULTRA_LUXURY_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Damodar Tech Craze | Ultra-Luxury Enterprise Ecosystem</title>
    <style>
        :root {{
            --bg-deep: #02040a;
            --bg-card: rgba(10, 15, 30, 0.75);
            --border-glass: rgba(255, 255, 255, 0.08);
            --border-glow: rgba(59, 130, 246, 0.3);
            --accent-blue: #3b82f6;
            --accent-glow: rgba(59, 130, 246, 0.35);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }}
        
        * {{ box-sizing: border-box; }}
        body {{
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 20% 10%, rgba(29, 78, 216, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 80% 90%, rgba(147, 51, 234, 0.1) 0%, transparent 40%);
        }}
        
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 24px 60px;
            border-bottom: 1px solid var(--border-glass);
            background: rgba(2, 4, 10, 0.85);
            backdrop-filter: blur(20px);
            position: sticky;
            top: 0;
            z-index: 1000;
        }}
        
        .logo {{
            font-size: 1.6rem;
            font-weight: 900;
            letter-spacing: -0.5px;
            color: #fff;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .logo span {{ color: var(--accent-blue); text-shadow: 0 0 25px rgba(59, 130, 246, 0.6); }}
        
        .status-pill {{
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(16, 185, 129, 0.08);
            border: 1px solid rgba(16, 185, 129, 0.25);
            padding: 8px 16px;
            border-radius: 30px;
            font-size: 0.82rem;
            color: #34d399;
            font-weight: 600;
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.1);
        }}
        .pulse {{ width: 8px; height: 8px; background: #34d399; border-radius: 50%; box-shadow: 0 0 12px #34d399; animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.4; }} 100% {{ opacity: 1; }} }}
        
        .hero {{
            text-align: center;
            padding: 100px 20px 40px 20px;
            max-width: 950px;
            margin: 0 auto;
        }}
        .hero h1 {{
            font-size: 4rem;
            font-weight: 900;
            margin-bottom: 20px;
            letter-spacing: -1.5px;
            background: linear-gradient(135deg, #ffffff 20%, #cbd5e1 70%, #60a5fa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .hero p {{
            color: var(--text-muted);
            font-size: 1.25rem;
            line-height: 1.6;
            margin-bottom: 45px;
        }}
        
        .search-container {{
            max-width: 700px;
            margin: 0 auto 35px auto;
            position: relative;
        }}
        .search-box {{
            width: 100%;
            padding: 20px 30px;
            background: rgba(10, 15, 30, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 16px;
            color: #fff;
            font-size: 1.1rem;
            outline: none;
            backdrop-filter: blur(15px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.8);
        }}
        .search-box:focus {{
            border-color: var(--accent-blue);
            box-shadow: 0 0 0 4px var(--accent-glow), 0 25px 60px -15px rgba(59, 130, 246, 0.4);
        }}
        
        .filter-bar {{
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            max-width: 1000px;
            margin: 0 auto 60px auto;
            padding: 0 20px;
        }}
        .filter-btn {{
            background: rgba(10, 15, 30, 0.6);
            border: 1px solid var(--border-glass);
            color: var(--text-muted);
            padding: 10px 22px;
            border-radius: 25px;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.25s ease;
            backdrop-filter: blur(10px);
        }}
        .filter-btn:hover, .filter-btn.active {{
            background: var(--accent-blue);
            color: #fff;
            border-color: var(--accent-blue);
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.6);
            transform: translateY(-2px);
        }}
        
        .grid-container {{
            max-width: 1350px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(390px, 1fr));
            gap: 30px;
            padding: 0 30px 120px 30px;
        }}
        
        .card {{
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 22px;
            padding: 38px;
            backdrop-filter: blur(16px);
            transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
        }}
        .card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 2px;
            background: linear-gradient(90deg, transparent, var(--accent-blue), transparent);
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        .card:hover {{
            transform: translateY(-8px);
            border-color: var(--border-glow);
            box-shadow: 0 30px 60px -20px rgba(0, 0, 0, 0.9), 0 0 30px rgba(59, 130, 246, 0.2);
        }}
        .card:hover::before {{ opacity: 1; }}
        
        .card-tag {{
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            color: var(--accent-blue);
            margin-bottom: 14px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .verified-badge {{
            background: rgba(59, 130, 246, 0.1);
            color: #60a5fa;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.72rem;
            border: 1px solid rgba(59, 130, 246, 0.25);
            font-weight: 600;
        }}
        
        .card h3 {{
            font-size: 1.6rem;
            font-weight: 700;
            margin: 0 0 12px 0;
            color: #fff;
            letter-spacing: -0.5px;
        }}
        .card p {{
            color: var(--text-muted);
            font-size: 0.98rem;
            line-height: 1.6;
            margin-bottom: 35px;
        }}
        
        .card-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid var(--border-glass);
            padding-top: 22px;
        }}
        .node-id {{
            font-family: monospace;
            font-size: 0.8rem;
            color: #64748b;
        }}
        .btn-explore {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(59, 130, 246, 0.12);
            color: #60a5fa;
            border: 1px solid rgba(59, 130, 246, 0.35);
            padding: 11px 22px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.92rem;
            transition: all 0.25s ease;
        }}
        .btn-explore:hover {{
            background: var(--accent-blue);
            color: #fff;
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.7);
            gap: 14px;
            transform: scale(1.02);
        }}
        
        footer {{
            text-align: center;
            padding: 60px;
            color: #64748b;
            font-size: 0.88rem;
            border-top: 1px solid var(--border-glass);
            background: rgba(2, 4, 10, 0.95);
        }}
    </style>
</head>
<body>
    <header>
        <a href="/" class="logo">Damodar Tech <span>Craze.</span></a>
        <div class="status-pill">
            <div class="pulse"></div>
            <span>Encrypted Affiliate Engine Active</span>
        </div>
    </header>

    <div class="hero">
        <h1>Intelligence. Precision. Scale.</h1>
        <p>Access verified enterprise affiliate networks, encrypted AI nodes, and high-performance monetization portals curated for elite execution.</p>
        
        <div class="search-container">
            <input type="text" class="search-box" placeholder="Search affiliate portals, AI models, networks (Cmd + K)..." id="searchInput">
        </div>
    </div>

    <div class="filter-bar">
        <button class="filter-btn active" onclick="filterCategory('all')">All Portals (24+)</button>
        <button class="filter-btn" onclick="filterCategory('affiliate network')">Affiliate Networks</button>
        <button class="filter-btn" onclick="filterCategory('ai & llm')">AI & LLM Infrastructure</button>
        <button class="filter-btn" onclick="filterCategory('e-commerce')">E-Commerce</button>
    </div>

    <div class="grid-container" id="cardGrid">
        {CARDS_HTML}
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
    f.write(ULTRA_LUXURY_HTML)

print("[SUCCESS] Ultra-Luxury v3 Ecosystem UI compiled with Affiliate Tracking Hooks!")
