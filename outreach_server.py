import http.server
import socketserver
import json
import smtplib
import os
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PORT = 5050
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "email_credentials.json")
LOG_FILE = os.path.join(os.path.dirname(__file__), "OUTREACH_DISPATCH_LOG.json")

# Default credentials template
DEFAULT_CONFIG = {
    "sender_email": "skykingly1@gmail.com",
    "app_password": "",
    "sender_name": "Sky King | Antigravity Digital Agency",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, indent=2)
        return DEFAULT_CONFIG
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_CONFIG

def log_dispatch(record):
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except Exception:
            logs = []
    logs.append(record)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)

class OutreachHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/status':
            config = load_config()
            has_password = bool(config.get("app_password", "").strip())
            logs = []
            if os.path.exists(LOG_FILE):
                try:
                    with open(LOG_FILE, "r", encoding="utf-8") as f:
                        logs = json.load(f)
                except Exception:
                    pass
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            resp = {
                "status": "online",
                "configured": has_password,
                "sender_email": config.get("sender_email"),
                "sender_name": config.get("sender_name"),
                "dispatched_count": len(logs),
                "logs": logs
            }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/api/send':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": f"Invalid JSON: {e}"}).encode('utf-8'))
                return

            recipient = data.get("recipient")
            subject = data.get("subject")
            body = data.get("body")
            lead_name = data.get("lead_name", recipient)

            if not recipient or not subject or not body:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": "Missing recipient, subject, or body"}).encode('utf-8'))
                return

            config = load_config()
            sender_email = config.get("sender_email", "").strip()
            app_password = config.get("app_password", "").strip()
            sender_name = config.get("sender_name", "Sky King")

            if not app_password:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": False,
                    "error": "Google App Password not configured yet in email_credentials.json. You can still use the '1-Click Gmail' button to send immediately via browser!"
                }).encode('utf-8'))
                return

            try:
                msg = MIMEMultipart()
                msg['From'] = f"{sender_name} <{sender_email}>"
                msg['To'] = recipient
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP(config.get("smtp_server", "smtp.gmail.com"), config.get("smtp_port", 587))
                server.starttls()
                server.login(sender_email, app_password)
                server.send_message(msg)
                server.quit()

                record = {
                    "lead_name": lead_name,
                    "recipient": recipient,
                    "subject": subject,
                    "sent_at": datetime.datetime.now().isoformat(),
                    "sender": sender_email,
                    "status": "DELIVERED"
                }
                log_dispatch(record)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": True,
                    "message": f"Successfully delivered directly to {recipient}!",
                    "record": record
                }).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run():
    load_config()
    with socketserver.TCPServer(("", PORT), OutreachHandler) as httpd:
        print(f"[OK] Outreach Server running on http://localhost:{PORT}")
        print(f"[READY] Ready to receive 1-Click direct email dispatch calls from dashboard!")
        httpd.serve_forever()

if __name__ == "__main__":
    run()
