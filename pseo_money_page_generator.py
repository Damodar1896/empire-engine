import os
import json

print("==================================================")
print("   DAMODAR EMPIRE: pSEO MONEY PAGE GENERATOR      ")
print("==================================================")

OUTPUT_DIR = "generated_pseo_pages"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load harvested keys if available
WALLET_FILE = "damodar_master_api_wallet.json"
master_wallet = {}
if os.path.exists(WALLET_FILE):
    try:
        with open(WALLET_FILE, "r", encoding="utf-8") as wf:
            master_wallet = json.load(wf)
    except:
        pass

# pSEO Niche Keywords & Matrix
PSEO_TARGETS = [
    {"keyword": "free-openai-api-key-generator-2026", "title": "Free OpenAI GPT-4o API Key Generator & Vault | Damodar Tech Craze", "platform": "OpenAI API", "category": "LLM Infrastructure"},
    {"keyword": "anthropic-claude-free-tokens-api", "title": "Anthropic Claude 3.5 Sonnet Free API Access Hub | Damodar Tech Craze", "platform": "Anthropic Claude Console", "category": "Neural Processing"},
    {"keyword": "groq-lpu-ultra-fast-inference-key", "title": "Groq LPU Ultra-Fast Inference Free API Key Portal | Damodar Tech Craze", "platform": "Groq Console", "category": "Hardware Acceleration"},
    {"keyword": "deepseek-r1-free-developer-api", "title": "DeepSeek R1 Free Developer API Endpoint & Key Vault | Damodar Tech Craze", "platform": "DeepSeek Platform", "category": "Reasoning Models"},
    {"keyword": "google-gemini-1.5-pro-free-key", "title": "Google AI Studio Gemini 1.5 Pro Free API Key Generator | Damodar Tech Craze", "platform": "Google AI Studio (Gemini)", "category": "Multimodal AI"}
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    <meta name="description" content="Access verified 24x7 autonomous {platform} infrastructure, live secure keys, and high-performance developer endpoints powered by Damodar Tech Craze.">
    <style>
        body {{ background-color: #0b0f19; color: #f3f4f6; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 40px; }}
        .container {{ max-width: 900px; margin: 0 auto; background: #111827; padding: 40px; border-radius: 16px; border: 1px solid #1f2937; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5); }}
        h1 {{ color: #60a5fa; font-size: 2.5rem; margin-bottom: 10px; }}
        .badge {{ display: inline-block; background: #3b82f6; color: white; padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; margin-bottom: 20px; }}
        p {{ line-height: 1.7; color: #9ca3af; font-size: 1.1rem; }}
        .key-box {{ background: #1f2937; padding: 20px; border-radius: 10px; border: 1px solid #374151; margin: 30px 0; font-family: monospace; color: #34d399; word-break: break-all; }}
        .btn {{ display: inline-block; background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); color: white; padding: 12px 28px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 20px; }}
        .footer {{ margin-top: 50px; text-align: center; font-size: 0.85rem; color: #6b7280; border-top: 1px solid #1f2937; padding-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <span class="badge">Verified Enterprise Hub • 24x7 Active</span>
        <h1>{platform} Secure Gateway</h1>
        <p>Welcome to the automated programmatic gateway for <strong>{platform}</strong>, categorized under <em>{category}</em>. This node is continuously synchronized with the Damodar Empire autonomous harvesting swarm.</p>
        
        <h3>Live Secure Infrastructure Status</h3>
        <p>Operational parameters indicate 100% uptime with automated residential proxy routing and anti-ban jitter protection enabled.</p>
        
        <div class="key-box">
            Status: OPTIMIZED_ACTIVE_2026<br>
            Endpoint Protocol: REST / gRPC Secure<br>
            System Sync: Damodar Tech Craze Autonomous Core
        </div>

        <a href="https://damodartechcraze.netlify.app" class="btn">Return to Master Portal</a>
        
        <div class="footer">
            &copy; 2026 Damodar Tech Craze. All rights reserved. Autonomous pSEO Execution Engine.
        </div>
    </div>
</body>
</html>
"""

def generate_pages():
    count = 0
    for target in PSEO_TARGETS:
        filename = f"{target['keyword']}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        rendered_html = HTML_TEMPLATE.format(
            page_title=target['title'],
            platform=target['platform'],
            category=target['category']
        )
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(rendered_html)
        print(f"[pSEO GENERATED] -> {filename}")
        count += 1

    print(f"\n[SUCCESS] Generated {count} unique high-impact pSEO money pages inside '{OUTPUT_DIR}/'.")

if __name__ == "__main__":
    generate_pages()
