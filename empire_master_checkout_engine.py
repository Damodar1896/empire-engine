import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("UltimateMasterCheckoutEngine")

# Founder Configurations & Direct Business Details
FOUNDER_WHATSAPP = "9232698947"  
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8844329469:AAGebHJye04B2iSQA99_jWvd-HB9N9Qqo44")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "8720676587")

def generate_production_checkout_portal(business_name: str, region: str) -> str:
    slug = business_name.lower().replace(" ", "-")
    filename = f"checkout_production_{region.lower()}_{slug}.html"
    
    if region.upper() == "US":
        pricing_block = """
            <div class="price-tag">$29.00 USD</div>
            <a href="https://paypal.me/damodartechcraze" target="_blank" class="btn-primary" style="background: #0070ba;">Pay $29 via PayPal</a>
            <div class="crypto-box">🪙 Trust Wallet / USDT (TRC20): <code>Accepted</code></div>
        """
    else:
        pricing_block = """
            <div class="price-tag">₹999.00 INR</div>
            <div class="payment-method-box">
                <b>⚡ Primary UPI (GPay / PhonePe):</b> <br><code>damodartechcraze@okaxis</code>
            </div>
            <div class="payment-method-box" style="margin-top: 8px;">
                <b>🏦 Direct Bank Transfer / RTGS / NEFT:</b><br>
                A/C Name: Damodar Tech Craze Ventures<br>
                A/C Number: <code>120040665228</code><br>
                IFSC Code: <code>CNRB0004042 (Canara Bank)</code>
            </div>
            <a href="upi://pay?pa=damodartechcraze@okaxis&pn=DamodarTechCraze&am=999.00&cu=INR" class="btn-primary">📱 Pay ₹999 via 1-Click UPI App</a>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Activation Portal | {business_name}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #060913; color: #f8fafc; padding: 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }}
        .card {{ background: #0f172a; padding: 25px; border-radius: 18px; box-shadow: 0 25px 50px rgba(0,0,0,0.7); width: 100%; max-width: 480px; border: 1px solid #1e293b; }}
        h2 {{ color: #38bdf8; text-align: center; margin-top: 0; }}
        .price-tag {{ font-size: 26px; font-weight: bold; color: #22c55e; text-align: center; margin: 15px 0; }}
        .payment-method-box {{ background: #020617; padding: 12px; border-radius: 8px; border: 1px solid #334155; font-size: 12px; color: #38bdf8; margin-top: 10px; }}
        .btn-primary {{ display: block; background: #22c55e; color: #fff; text-align: center; padding: 12px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 15px; font-size: 14px; }}
        .btn-primary:hover {{ background: #16a34a; }}
        .crypto-box {{ background: #020617; padding: 10px; border-radius: 8px; font-size: 11px; color: #cbd5e1; margin-top: 10px; border: 1px solid #334155; text-align: center; }}
        code {{ color: #facc15; font-family: monospace; }}
    </style>
</head>
<body>
    <div class="card">
        <h2>🛡️ Secure Asset Activation</h2>
        <div style="text-align: center; color: #94a3b8; font-size: 12px;">Target: {business_name}</div>
        
        {pricing_block}

        <a href="https://wa.me/{FOUNDER_WHATSAPP}?text=Hi,%20I%20have%20completed%20the%20payment%20for%20{business_name}.%20Please%20deploy." target="_blank" class="btn-primary" style="background: #2563eb; margin-top: 12px;">💬 Verify Payment via WhatsApp</a>
    </div>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content.strip())
        
    logger.info(f"Production Checkout generated for {business_name} -> {filename}")
    return filename

if __name__ == "__main__":
    generate_production_checkout_portal("Austin Prime Plumbers", "US")
    generate_production_checkout_portal("Mumbai Elite HVAC", "IN")
    logger.info("All production checkout pages with RTGS/NEFT, UPI, & WhatsApp integration compiled successfully.")
