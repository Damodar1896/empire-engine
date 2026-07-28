import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("EmpireProductionConfig")

# --- YOUR PERMANENT BUSINESS & PAYMENT CREDENTIALS ---
BANK_DETAILS = {
    "account_name": "Damodar Tech Craze Ventures",
    "account_number": "120040665228",
    "ifsc_code": "CNRB0004042",
    "bank_name": "Canara Bank",
    "upi_id": "damodartechcraze@okaxis",
    "whatsapp_number": "+919232698947",
    "paypal_link": "https://paypal.me/damodartechcraze"
}

def generate_final_checkout_page(business_name: str, region: str) -> str:
    slug = business_name.lower().replace(" ", "-")
    filename = f"checkout_final_{region.lower()}_{slug}.html"
    
    if region.upper() == "US":
        payment_html = f"""
            <div class="price-tag">$29.00 USD</div>
            <a href="{BANK_DETAILS['paypal_link']}" target="_blank" class="btn-primary" style="background: #0070ba;">Pay $29 via PayPal</a>
            <div class="info-box">🪙 Trust Wallet / USDT (TRC20): <code>Accepted</code></div>
        """
    else:
        payment_html = f"""
            <div class="price-tag">₹999.00 INR</div>
            <div class="info-box">
                <b>⚡ Primary UPI (GPay / PhonePe):</b><br><code>{BANK_DETAILS['upi_id']}</code>
            </div>
            <div class="info-box" style="margin-top: 10px;">
                <b>🏦 Direct Bank Transfer / RTGS / NEFT:</b><br>
                A/C Name: {BANK_DETAILS['account_name']}<br>
                A/C Number: <code>{BANK_DETAILS['account_number']}</code><br>
                IFSC Code: <code>{BANK_DETAILS['ifsc_code']} ({BANK_DETAILS['bank_name']})</code>
            </div>
            <a href="upi://pay?pa={BANK_DETAILS['upi_id']}&pn=DamodarTechCraze&am=999.00&cu=INR" class="btn-primary">📱 Pay ₹999 via 1-Click UPI App</a>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Activation | {business_name}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; background: #060913; color: #f8fafc; padding: 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }}
        .card {{ background: #0f172a; padding: 25px; border-radius: 18px; box-shadow: 0 25px 50px rgba(0,0,0,0.7); width: 100%; max-width: 480px; border: 1px solid #1e293b; }}
        h2 {{ color: #38bdf8; text-align: center; margin-top: 0; }}
        .price-tag {{ font-size: 26px; font-weight: bold; color: #22c55e; text-align: center; margin: 15px 0; }}
        .info-box {{ background: #020617; padding: 12px; border-radius: 8px; border: 1px solid #334155; font-size: 12px; color: #38bdf8; }}
        .btn-primary {{ display: block; background: #22c55e; color: #fff; text-align: center; padding: 12px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 15px; font-size: 14px; }}
        code {{ color: #facc15; font-family: monospace; }}
    </style>
</head>
<body>
    <div class="card">
        <h2>🛡️ Secure Asset Activation</h2>
        <div style="text-align: center; color: #94a3b8; font-size: 12px; margin-bottom: 15px;">Target: {business_name}</div>
        {payment_html}
        <a href="https://wa.me/{BANK_DETAILS['whatsapp_number'].replace('+', '')}?text=Hi,%20I%20have%20completed%20payment%20for%20{business_name}.%20Please%20deploy." target="_blank" class="btn-primary" style="background: #2563eb; margin-top: 12px;">💬 Verify Payment via WhatsApp</a>
    </div>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content.strip())
    logger.info(f"Production Checkout compiled successfully -> {filename}")
    return filename

if __name__ == "__main__":
    generate_final_checkout_page("Austin Prime Plumbers", "US")
    generate_final_checkout_page("Mumbai Elite HVAC", "IN")
    logger.info("All bank details, RTGS/NEFT, UPI, and WhatsApp numbers locked into the system.")
