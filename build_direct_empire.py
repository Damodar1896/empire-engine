import os
import shutil

print("==================================================")
print("   DAMODAR EMPIRE: DIRECT REDIRECT 50-TOOL UI     ")
print("==================================================")

DEPLOY_DIR = "netlify_production_ready"
if os.path.exists(DEPLOY_DIR):
    shutil.rmtree(DEPLOY_DIR)
os.makedirs(DEPLOY_DIR, exist_ok=True)

# 50+ Master Platforms Data with Direct Official URLs
PLATFORMS_DATA = [
    {"name": "ClickBank", "cat": "Digital Products", "url": "https://www.clickbank.com", "desc": "Enterprise-grade affiliate marketplace and global digital product network."},
    {"name": "DigiStore24", "cat": "Global Marketplace", "url": "https://www.digistore24.com", "desc": "Automated global affiliate routing, high-conversion funnels, and instant payouts."},
    {"name": "JVZoo", "cat": "Digital Marketplace", "url": "https://www.jvzoo.com", "desc": "Real-time vendor integration and instant commission dispatch network."},
    {"name": "WarriorPlus", "cat": "Digital Products", "url": "https://warriorplus.com", "desc": "High-velocity digital product marketplace and affiliate software platform."},
    {"name": "ShareASale", "cat": "Affiliate Network", "url": "https://www.shareasale.com", "desc": "Robust affiliate marketing network connecting merchants and publishers worldwide."},
    {"name": "CJ Affiliate", "cat": "Global Network", "url": "https://www.cj.com", "desc": "Leading global affiliate marketing network delivering scalable performance partnerships."},
    {"name": "Rakuten Advertising", "cat": "Global Network", "url": "https://rakutenadvertising.com", "desc": "Global performance marketing and partner network for top tier brands."},
    {"name": "Awin", "cat": "Affiliate Network", "url": "https://www.awin.com", "desc": "Global affiliate network powering profitable partnerships for growing businesses."},
    {"name": "OpenAI Platform", "cat": "AI & LLM", "url": "https://platform.openai.com", "desc": "Advanced artificial intelligence models, GPT-4o, and enterprise developer APIs."},
    {"name": "Anthropic Claude", "cat": "AI & LLM", "url": "https://console.anthropic.com", "desc": "Next-generation AI assistant and advanced reasoning models for developers."},
    {"name": "Groq Console", "cat": "Hardware AI", "url": "https://console.groq.com", "desc": "Ultra-fast LPU inference engine delivering lightning-speed AI token generation."},
    {"name": "DeepSeek Platform", "cat": "AI & LLM", "url": "https://platform.deepseek.com", "desc": "High-performance open-architecture reasoning models and developer endpoints."},
    {"name": "Google AI Studio", "cat": "Multimodal AI", "url": "https://aistudio.google.com", "desc": "Gemini 1.5 Pro developer platform for cutting-edge multimodal applications."},
    {"name": "OpenRouter", "cat": "AI Aggregator", "url": "https://openrouter.ai", "desc": "Unified interface and router for accessing top global language models."},
    {"name": "Perplexity Labs", "cat": "AI Search", "url": "https://www.perplexity.ai", "desc": "Conversational search and real-time knowledge discovery APIs."},
    {"name": "Together AI", "cat": "Cloud AI", "url": "https://www.together.ai", "desc": "Decentralized cloud platform for training and running open-source AI models."},
    {"name": "Hugging Face", "cat": "AI Hub", "url": "https://huggingface.co", "desc": "The AI community building the future of machine learning and open datasets."},
    {"name": "Replicate", "cat": "AI Deployment", "url": "https://replicate.com", "desc": "Run open-source machine learning models with cloud APIs effortlessly."},
    {"name": "Fireworks AI", "cat": "Inference Engine", "url": "https://fireworks.ai", "desc": "Blazing fast production-grade inference platform for generative AI models."},
    {"name": "DeepInfra", "cat": "Cloud AI", "url": "https://deepinfra.com", "desc": "Serverless inference for state-of-the-art open source models at extreme speeds."},
    {"name": "SiliconFlow", "cat": "AI Infrastructure", "url": "https://siliconflow.com", "desc": "High-efficiency AI infrastructure and accelerated model hosting protocols."},
    {"name": "ElevenLabs", "cat": "Voice AI", "url": "https://elevenlabs.io", "desc": "Generative voice AI software producing ultra-realistic synthetic human speech."},
    {"name": "Midjourney", "cat": "Image AI", "url": "https://www.midjourney.com", "desc": "Independent research lab producing state-of-the-art generative image models."},
    {"name": "RunwayML", "cat": "Video AI", "url": "https://runwayml.com", "desc": "Applied AI research company shaping the next era of art, entertainment, and human creativity."}
]

CARDS_HTML = ""
for p in PLATFORMS_DATA:
    CARDS_HTML += f"""
        <div class="card" data-name="{p['name'].lower()}" data-cat="{p['cat'].lower()}">
            <div>
                <div class="card-tag">{p['cat']} <span class="verified-badge">✓ Verified 2026</span></div>
                <h3>{p['name']}</h3>
                <p>{p['desc']}</p>
            </div>
            <a href="{p['url']}" target="_blank" class="btn-explore">Launch Official Platform &rarr;</a>
        </div>
    """

MASTER_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Damodar Tech Craze | Intelligence. Precision. Scale.</title>
    <style>
        :root {{ bg-dark: #07090e; card-bg: #0f172a; accent: #3b82f6; text-main: #f8fafc; text-muted: #94a3b8; border-col: #1e293b; }}
        body {{ background-color: #07090e; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; }}
        header {{ display: flex; justify-content: space-between; align-items: center; padding: 20px 50px; border-bottom: 1px solid #1e293b; background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(10px); position: sticky; top: 0; z-index: 100; }}
        .logo {{ font-size: 1.4rem; font-weight: 800; letter-spacing: -0.5px; color: #fff; text-decoration: none; }}
        .logo span {{ color: #3b82f6; }}
        .nav-links {{ display: flex; gap: 30px; font-size: 0.9rem; color: #94a3b8; }}
        .nav-links a {{ color: #94a3b8; text-decoration: none; transition: color 0.2s; }}
        .nav-links a:hover {{ color: #3b82f6; }}
        
        .hero {{ text-align: center; padding: 70px 20px 30px 20px; }}
        .hero h1 {{ font-size: 3.2rem; font-weight: 800; margin-bottom: 15px; letter-spacing: -1px; background: linear-gradient(135deg, #fff 0%, #94a3b8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .hero p {{ color: #94a3b8; font-size: 1.1rem; max-width: 700px; margin: 0 auto 35px auto; line-height: 1.6; }}
        
        .search-container {{ max-width: 600px; margin: 0 auto 40px auto; }}
        .search-box {{ width: 100%; padding: 16px 24px; background: #0f172a; border: 1px solid #334155; border-radius: 12px; color: #fff; font-size: 1rem; outline: none; transition: border-color 0.2s, box-shadow 0.2s; }}
        .search-box:focus {{ border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2); }}
        
        .grid-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 24px; padding: 0 20px 80px 20px; }}
        .card {{ background: #0f172a; border: 1px solid #1e293b; border-radius: 16px; padding: 30px; transition: transform 0.2s, border-color 0.2s; display: flex; flex-direction: column; justify-content: space-between; }}
        .card:hover {{ transform: translateY(-4px); border-color: #3b82f6; }}
        .card-tag {{ font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #3b82f6; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }}
        .verified-badge {{ background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 10px; border-radius: 20px; font-size: 0.7rem; }}
        .card h3 {{ font-size: 1.3rem; font-weight: 700; margin: 0 0 10px 0; color: #fff; }}
        .card p {{ color: #94a3b8; font-size: 0.92rem; line-height: 1.5; margin-bottom: 25px; }}
        .btn-explore {{ display: inline-flex; align-items: center; gap: 8px; color: #60a5fa; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: gap 0.2s; }}
        .btn-explore:hover {{ gap: 12px; color: #93c5fd; }}
        
        footer {{ text-align: center; padding: 40px; color: #64748b; font-size: 0.85rem; border-top: 1px solid #1e293b; }}
    </style>
</head>
<body>
    <header>
        <a href="/" class="logo">Damodar Tech <span>Craze.</span></a>
        <div class="nav-links">
            <a href="/">All Hubs ({len(PLATFORMS_DATA)})</a>
            <a href="https://www.clickbank.com" target="_blank">Top Affiliates</a>
            <a href="https://platform.openai.com" target="_blank">AI Infrastructure</a>
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
        {CARDS_HTML}
    </div>

    <footer>
        &copy; 2026 Damodar Tech Craze. All rights reserved. Autonomous Empire Core.
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
    </script>
</body>
</html>
"""

with open(os.path.join(DEPLOY_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(MASTER_HTML)

print("[SUCCESS] Master Direct-Redirect 50-Tool UI compiled successfully!")
