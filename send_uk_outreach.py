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
LEADS_FILE = os.path.join(BASE_DIR, "uk_50_trade_leads.json")
LOG_FILE = os.path.join(BASE_DIR, "UK_OUTREACH_DISPATCH_LOG.json")

def load_credentials():
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def build_uk_email(lead):
    subject = f"{lead['name']}: built a live website prototype for your team (£99 flat)"
    
    body = f"""Hi {lead['name']} Team,

I'll keep this short because I know you're busy on jobs across {lead['location']}.

I was looking through trade listings on the {lead['source']} directory and noticed something surprising: you have great local feedback and craftsmanship, but when homeowners in {lead['location']} search for your business on their phone, they hit a dead end with no official website.

Right now, big out-of-town franchises and lead-broker middle-men on platforms like Checkatrade and Bark are charging you hundreds in monthly listing fees, while taking high-ticket {lead['category'].lower()} jobs right in your local postcodes ({lead['postcode']}).

Instead of pitching you, I decided to build you the solution upfront.

Last night, I designed and coded an ultra-modern, high-speed mobile prototype custom-tailored for {lead['name']}. It is live right now:

👉 Live Interactive Prototype: https://skyking-client-previews.surge.sh/

What we built into this:
• 1-Click Mobile Call Routing straight to your trade line ({lead['phone']})
• Instant Project Quote Estimator (filters out tire-kickers and sends real homeowner jobs to your email)
• Verified Trade Trust Badges ({lead['badge']} & £5M Public Liability Badges)
• Blazing 0.5s Turbo Load Speed on iPhone & Android

Most UK web design agencies bill £1,500 to £3,000 upfront. We think that's absurd for hard-working British trades.

Since the prototype is already 100% designed and built for you, you can claim the complete website, your custom company domain, and high-speed UK cloud hosting for an affordable flat £99 (or £19/mo with zero contracts). One single customer callout pays for the entire site immediately.

If you'd like to claim this design and have it live on Google under your own domain this week, simply reply "I'm interested" to this email and I'll handle the rest for you.

If not, no worries at all—feel free to use the preview link as inspiration. Keep up the brilliant work serving {lead['location']}!

Best regards,
Sky King
Founder, Antigravity Digital Agency
Direct Email: skykingly1@gmail.com
"""
    return subject, body

def dispatch_all_direct(dry_run=False):
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
        print("\n⚠️ Google App Password Required for Direct Automated Dispatch!")
        print(f"Account: {sender_email}")
        print("Google requires a 16-character App Password to allow automated SMTP sending.")
        print("Steps (takes 30 seconds):")
        print("1. Go to: https://myaccount.google.com/apppasswords")
        print("2. Enter app name 'Antigravity Agency' and click Create")
        print("3. Paste the 16 characters into 'app_password' inside 'email_credentials.json'")
        print("4. Re-run this script to automatically dispatch all 50 emails directly!\n")
        return

    with open(LEADS_FILE, "r", encoding="utf-8") as f:
        leads = json.load(f)

    print(f"🚀 Preparing direct dispatch to {len(leads)} UK Trade Businesses at £99 Flat Offer...")
    
    server = None
    if not dry_run:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)
        print("✅ Connected & Authenticated to Google SMTP successfully!\n")

    dispatch_log = []
    sent_count = 0

    for i, lead in enumerate(leads, 1):
        subj, body = build_uk_email(lead)
        to_email = lead['email']
        
        if dry_run:
            print(f"[{i}/{len(leads)}] [DRY RUN] Would send to: {lead['name']} <{to_email}> | Subject: {subj}")
            sent_count += 1
            continue

        try:
            msg = MIMEMultipart()
            msg['From'] = f"{sender_name} <{sender_email}>"
            msg['To'] = to_email
            msg['Subject'] = subj
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            server.sendmail(sender_email, to_email, msg.as_string())
            print(f"[{i}/{len(leads)}] ✅ Delivered directly to: {lead['name']} ({to_email})")
            
            dispatch_log.append({
                "id": lead['id'],
                "name": lead['name'],
                "email": to_email,
                "status": "DELIVERED",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            })
            sent_count += 1
            time.sleep(1.5) # respectful delay to keep deliverability spotless
        except Exception as e:
            print(f"[{i}/{len(leads)}] ❌ Failed to send to {to_email}: {e}")
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

    print(f"\n🎉 Direct Outreach Complete! {sent_count}/{len(leads)} emails dispatched.")

if __name__ == "__main__":
    import sys
    dry = "--dry-run" in sys.argv
    dispatch_all_direct(dry_run=dry)
