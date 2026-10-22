import json
import smtplib
import os
import sys
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\Richi\OneDrive\Desktop\antigravity\13_Website_Design_Agency"
CONFIG_FILE = os.path.join(BASE_DIR, "email_credentials.json")
LOG_FILE = os.path.join(BASE_DIR, "UK_VERIFIED_DISPATCH_LOG.json")

from generate_10_uk_sites import uk_businesses

def load_credentials():
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def build_uk_email(lead):
    sample_url = f"https://skyking-client-previews.surge.sh/samples/{lead['id']}/"
    subject = f"{lead['name']}: built a live website prototype for your team (£99 flat)"
    
    body = f"""Hi {lead['name']} Team,

I'll keep this short because I know you're busy running jobs across {lead['location']}.

I was doing research on top-rated {lead['category'].lower()} specialists in {lead['location']} and noticed something surprising: you have great local reputation and craft, but when homeowners in {lead['postcode']} search for your business on their mobile phone, they hit a dead end with no official website.

Meanwhile, out-of-town franchises and lead-broker middle-men on platforms like Checkatrade and Bark charge you hundreds in monthly fees while scooping up high-ticket jobs in your own backyard.

Instead of sending you an annoying pitch, I decided to build you the solution upfront.

Last night, I designed and coded an ultra-modern, high-speed mobile prototype custom-tailored specifically for {lead['name']}. It is 100% functional and live right now:

👉 Live Interactive Prototype for {lead['name']}:
{sample_url}

Take 30 seconds to tap around on your phone:
• 1-Click Mobile Call Routing straight to your trade dispatch ({lead['phone']})
• Instant Project Quote Estimator (filters out tire-kickers and sends real homeowner project requests to {lead['email']})
• Verified Accreditations ({lead['badges'][0]} & £5M Public Liability Trust Seals)
• Blazing 0.5s Turbo Load Speed on iPhone & Android

Most UK web design agencies bill £1,500 to £3,000 upfront and take 6 weeks. We think that's absurd for hard-working British trades.

Since this prototype is already 100% designed and built for you, you can claim the complete website, your custom company domain (.co.uk), and high-speed UK cloud hosting for an affordable flat £99 (or £19/mo with zero contracts). One single customer callout pays for the entire site immediately.

If you'd like to claim this design and have it live on Google under your own domain this week, simply reply "I'm interested" to this email and I'll handle the rest for you.

If not, no worries at all—feel free to use the preview link as inspiration. Keep up the brilliant work serving {lead['service_area']}!

Best regards,
Sky King
Founder, Antigravity Digital Agency
Direct Email: skykingly1@gmail.com
"""
    return subject, body

def dispatch_verified_uk(dry_run=False):
    creds = load_credentials()
    if not creds:
        print("❌ Error: email_credentials.json not found!")
        return

    sender_email = creds.get("sender_email", "skykingly1@gmail.com")
    app_password = creds.get("app_password", "").strip()
    sender_name = creds.get("sender_name", "Sky King | Antigravity Digital Agency")
    smtp_server = creds.get("smtp_server", "smtp.gmail.com")
    smtp_port = creds.get("smtp_port", 587)

    if not app_password and not dry_run:
        print("❌ Error: No Google App Password configured.")
        return

    print(f"🚀 Preparing dispatch to {len(uk_businesses)} VERIFIED UK Trade Businesses with live dedicated prototypes (£99 Flat Offer)...")
    
    server = None
    if not dry_run:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)
        print("✅ Connected & Authenticated to Google SMTP successfully!\n")

    dispatch_log = []
    sent_count = 0

    for i, lead in enumerate(uk_businesses, 1):
        subj, body = build_uk_email(lead)
        to_email = lead['email']
        sample_url = f"https://skyking-client-previews.surge.sh/samples/{lead['id']}/"
        
        if dry_run:
            print(f"[{i}/{len(uk_businesses)}] [DRY RUN] -> {lead['name']} <{to_email}>")
            print(f"       Prototype: {sample_url}")
            print(f"       Subject: {subj}")
            sent_count += 1
            continue

        try:
            msg = MIMEMultipart()
            msg['From'] = f"{sender_name} <{sender_email}>"
            msg['To'] = to_email
            msg['Subject'] = subj
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            server.sendmail(sender_email, to_email, msg.as_string())
            print(f"[{i}/{len(uk_businesses)}] ✅ Delivered directly to: {lead['name']} ({to_email})")
            print(f"       Dedicated Site: {sample_url}")
            
            dispatch_log.append({
                "id": lead['id'],
                "name": lead['name'],
                "email": to_email,
                "prototype_url": sample_url,
                "status": "DELIVERED",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            })
            sent_count += 1
            time.sleep(2.0)
        except Exception as e:
            print(f"[{i}/{len(uk_businesses)}] ❌ Failed to send to {to_email}: {e}")
            dispatch_log.append({
                "id": lead['id'],
                "name": lead['name'],
                "email": to_email,
                "status": "FAILED",
                "error": str(e),
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            })

    if server:
        server.quit()

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(dispatch_log, f, indent=2)

    print(f"\n🎉 Verified UK Outreach Complete! {sent_count}/{len(uk_businesses)} bespoke prototypes pitched.")

if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    dispatch_verified_uk(dry_run=dry)
