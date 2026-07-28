import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("UltraAdvancedMasterOutreach")

MASTER_COLD_EMAIL_TEMPLATE = """
Subject: Urgent site conversion audit for {business_name} (revenue leakage detected)

Hi {owner_name},

I’ll keep this exceptionally brief and bypass the standard agency sales pitch.

While running a automated late-night mobile conversion benchmark across {city} last week, my engineering unit flagged {business_name} for a severe profit leak that your top local competitors are actively capitalizing on.

Here is the exact behavioral math:
When high-intent local homeowners search for your services past 7 PM, your current mobile setup forces them into a static, dead-end contact form. Industry metrics prove that 68% of those active prospects bounce instantly and call the competitor who deploys an instant digital estimator. 

That translates to roughly 4 to 7 high-ticket emergency jobs slipping past {business_name} every single week.

Instead of merely sending an audit report, we took the liberty of spending 20 minutes custom-coding a fully functional, production-ready "Instant After-Hours Estimator Widget" pre-styled with {business_name}'s precise brand identity, color palette, and assets.

You can inspect your 30-second personalized video breakdown and test-drive your live working preview right here:
👉 {prebuilt_demo_link}

If you prefer to permanently plug this leak and automate your night-time acquisition directly on your domain, you can activate it in 15 minutes right here:
⚡ {elite_checkout_link}

*(Note: Because this asset was custom-engineered specifically for {business_name}'s domain infrastructure, this pre-built reservation slot auto-expires in exactly 48 hours before being automatically reassigned to another local provider in {city}).*

Take a 10-second glance at your live interactive preview above. What are your thoughts on this, {owner_name}?

Best regards,

{sender_name}
{brand_name}
"""

def generate_master_outreach_payload(business_name: str, owner_name: str, city: str, demo_link: str, checkout_link: str, sender_name: str = "Damodar", brand_name: str = "Damodar Tech Craze Ventures") -> str:
    """Generates the 10x psychological-triggered master email payload with locked sender and brand names."""
    email_body = MASTER_COLD_EMAIL_TEMPLATE.format(
        business_name=business_name,
        owner_name=owner_name,
        city=city,
        prebuilt_demo_link=demo_link,
        elite_checkout_link=checkout_link,
        sender_name=sender_name,
        brand_name=brand_name
    )
    logger.info(f"SUCCESS: 10x Master Email compiled with Sender [{sender_name}] and Brand [{brand_name}] for {business_name}!")
    return email_body

if __name__ == "__main__":
    # Yahan sender_name mein "Damodar" ya "Subhash" set kar sakte hain
    sample_payload = generate_master_outreach_payload(
        business_name="Austin Prime Plumbers",
        owner_name="David",
        city="Austin, TX",
        demo_link="https://instant-utility.site/demo/austin-prime-plumbers",
        checkout_link="https://instant-utility.site/checkout/austin-prime-plumbers",
        sender_name="Subhash",
        brand_name="Damodar Tech Craze Ventures"
    )
    print("\n--- GENERATED 10X ADVANCED MASTER EMAIL PREVIEW ---\n")
    print(sample_payload)
