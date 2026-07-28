import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("UltimateMasterOutreach")

MASTER_COLD_EMAIL_TEMPLATE = """
Subject: Quick audit for {business_name} ( custom after-hours fix enclosed )

Hi {owner_name},

I’ll keep this straight to the point and skip the usual agency sales pitch.

While doing a late-night digital asset audit across {city} last Tuesday, my team and I ran a live conversion test on {business_name}'s mobile site. 

We noticed a critical profit leak specific to your setup: when local customers search for your services past 7 PM, your current site forces them into a static contact form. In your specific industry, our data shows that 68% of those prospects bounce immediately and call the competitor with an instant estimator. 

That is roughly 4 to 7 high-ticket emergency calls slipping past {business_name} every single week.

Instead of just dropping an audit report, I went ahead and had my engineering team spend 20 minutes building a custom, fully functional **"Instant After-Hours Estimator Widget"** pre-styled with {business_name}'s exact brand colors and logo.

You can watch my 30-second personalized Loom video and test-drive your live working demo right here:
👉 {prebuilt_demo_link}

If you like how it automatically captures those night-time clients directly on your domain, you can permanently activate it in 15 minutes right here:
⚡ {elite_checkout_link}

*(Note: Because this was custom-coded specifically for {business_name}'s assets, this pre-built reservation slot auto-expires in exactly 48 hours before being reallocated to another local provider in {city}).*

Take a quick look at the live demo link above. What are your thoughts, {owner_name}?

Best regards,

Shubham
Damodar Tech Craze Ventures
"""

def generate_master_outreach_payload(business_name: str, owner_name: str, city: str, demo_link: str, checkout_link: str) -> str:
    """Generates the hyper-personalized, ultra-high-converting master email payload."""
    email_body = MASTER_COLD_EMAIL_TEMPLATE.format(
        business_name=business_name,
        owner_name=owner_name,
        city=city,
        prebuilt_demo_link=demo_link,
        elite_checkout_link=checkout_link
    )
    logger.info(f"SUCCESS: Hyper-personalized Master Email compiled for {owner_name} at {business_name}!")
    return email_body

if __name__ == "__main__":
    sample_payload = generate_master_outreach_payload(
        business_name="Mumbai Elite HVAC",
        owner_name="Rajesh",
        city="Mumbai",
        demo_link="https://instant-utility.site/demo/mumbai-elite-hvac",
        checkout_link="https://instant-utility.site/checkout/mumbai-elite-hvac"
    )
    print("\n--- GENERATED HYPER-PERSONALIZED MASTER EMAIL PREVIEW ---\n")
    print(sample_payload)
