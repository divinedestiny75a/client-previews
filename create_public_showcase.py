import os
import json
import sys

BASE_DIR = r"c:\Users\Richi\OneDrive\Desktop\antigravity\13_Website_Design_Agency"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

sys.path.append(BASE_DIR)
from generate_all_13_sites import businesses as us_businesses
from generate_10_uk_sites import uk_businesses

def build_showcase_html():
    cards_html = ""

    # 1. RENDER 10 UK BESPOKE SITES FIRST (OR SECTIONS)
    for b in uk_businesses:
        cat_lower = b['category'].lower()
        if "roof" in cat_lower:
            cat_slug = "roofing"
        elif "plumb" in cat_lower or "heat" in cat_lower:
            cat_slug = "plumbing"
        elif "electr" in cat_lower:
            cat_slug = "electrical"
        elif "drive" in cat_lower or "landscap" in cat_lower or "paving" in cat_lower:
            cat_slug = "landscaping"
        elif "paint" in cat_lower or "decor" in cat_lower:
            cat_slug = "painting"
        else:
            cat_slug = "other"

        sample_url = f"./samples/{b['id']}/"

        cards_html += f"""
        <div class="prototype-card" data-category="{cat_slug}" data-country="uk">
          <div class="card-visual" style="background: linear-gradient(180deg, rgba(10,14,23,0.2) 0%, rgba(10,14,23,0.95) 100%), url('{b['theme']['hero_img']}') center/cover no-repeat;">
            <div class="country-tag uk-tag">🇬🇧 UK PROTOTYPE</div>
            <div class="card-badge" style="background: {b['theme']['badge_bg']}; color: {b['theme']['badge_text']}; border: 1px solid {b['theme']['border_accent']};">
              <span>{b['category'].upper()}</span>
            </div>
            <div class="client-mark" style="background: {b['theme']['surface_card']}; border: 1px solid {b['theme']['border_accent']}; color: {b['theme']['primary']};">
              {b['mark']}
            </div>
          </div>
          
          <div class="card-content">
            <div class="card-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
              {b['location']} • Postcode {b['postcode']}
            </div>
            <h3 class="card-title">{b['name']}</h3>
            <p class="card-trade">{b['trade']}</p>
            
            <div class="feature-pills">
              <span class="pill-feat"><svg class="pill-svg" viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/></svg> £ GBP Investment Estimator</span>
              <span class="pill-feat"><svg class="pill-svg" viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg> {b['badges'][0]}</span>
              <span class="pill-feat"><svg class="pill-svg" viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg> 1-Click UK Call Routing</span>
              <span class="pill-feat"><svg class="pill-svg" viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> 0.5s Turbo Load</span>
            </div>

            <div class="card-action">
              <a href="{sample_url}" target="_blank" class="btn-demo" style="background: {b['theme']['accent_grad']};">
                Explore Live UK Prototype ↗
              </a>
            </div>
          </div>
        </div>
        """

    # 2. RENDER 13 US BESPOKE SITES
    for b in us_businesses:
        cat_lower = b['category'].lower()
        if "roof" in cat_lower:
            cat_slug = "roofing"
        elif "plumb" in cat_lower:
            cat_slug = "plumbing"
        elif "electr" in cat_lower:
            cat_slug = "electrical"
        elif "landscap" in cat_lower or "hardscap" in cat_lower:
            cat_slug = "landscaping"
        elif "paint" in cat_lower:
            cat_slug = "painting"
        elif "hvac" in cat_lower or "heat" in cat_lower:
            cat_slug = "hvac"
        else:
            cat_slug = "other"

        tool_badge = "Interactive Cost Calculator" if b['tool_type'] == 'calculator' else "Emergency Diagnostic System"
        sample_url = f"./samples/{b['id']}/"

        cards_html += f"""
        <div class="prototype-card" data-category="{cat_slug}" data-country="us">
          <div class="card-visual" style="background: linear-gradient(180deg, rgba(10,14,23,0.2) 0%, rgba(10,14,23,0.95) 100%), url('{b['theme']['card_imgs'][0]}') center/cover no-repeat;">
            <div class="country-tag us-tag">🇺🇸 US PROTOTYPE</div>
            <div class="card-badge" style="background: {b['theme']['badge_bg']}; color: {b['theme']['badge_text']}; border: 1px solid {b['theme']['border_accent']};">
              <span>{b['category'].upper()}</span>
            </div>
            <div class="client-mark" style="background: {b['theme']['surface_card']}; border: 1px solid {b['theme']['border_accent']}; color: {b['theme']['primary']};">
              {b['mark']}
            </div>
          </div>
          
          <div class="card-content">
            <div class="card-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
              {b['location']} • {b['service_area']}
            </div>
            <h3 class="card-title">{b['name']}</h3>
            <p class="card-trade">{b['trade']}</p>
            
            <div class="feature-pills">
              <span class="pill-feat"><svg class="pill-svg" viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/></svg> {tool_badge}</span>
              <span class="pill-feat"><svg class="pill-svg" viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg> 1-Click Mobile Call Routing</span>
              <span class="pill-feat"><svg class="pill-svg" viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg> Verified Trust Badges</span>
              <span class="pill-feat"><svg class="pill-svg" viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> 0.5s Turbo Load</span>
            </div>

            <div class="card-action">
              <a href="{sample_url}" target="_blank" class="btn-demo" style="background: {b['theme']['accent_grad']};">
                Explore Live US Prototype ↗
              </a>
            </div>
          </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Antigravity Digital Agency | Client Showcase & Interactive Prototypes</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #07090e;
      --surface: #0e121b;
      --surface-card: #141a27;
      --card-border: rgba(255, 255, 255, 0.08);
      --card-border-hover: rgba(99, 102, 241, 0.4);
      --primary: #6366f1;
      --primary-light: #818cf8;
      --accent: #10b981;
      --text: #f8fafc;
      --text-muted: #94a3b8;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 15% 10%, rgba(99, 102, 241, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 30%, rgba(16, 185, 129, 0.08) 0%, transparent 40%);
      background-attachment: fixed;
    }}
    .container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    /* Global Header / Nav */
    nav {{
      border-bottom: 1px solid var(--card-border);
      padding: 20px 0;
      background: rgba(7, 9, 14, 0.8);
      backdrop-filter: blur(16px);
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .nav-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
    }}
    .brand-mark {{
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, #6366f1 0%, #38bdf8 100%);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 800;
      font-size: 1.2rem;
      box-shadow: 0 0 20px rgba(99, 102, 241, 0.4);
    }}
    .brand-name {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.25rem;
      font-weight: 700;
      color: white;
      letter-spacing: -0.5px;
    }}
    .brand-tag {{
      font-size: 0.72rem;
      color: var(--accent);
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 2px 8px;
      border-radius: 6px;
      font-weight: 700;
      margin-left: 6px;
      letter-spacing: 0.5px;
    }}
    .nav-links {{
      display: flex;
      align-items: center;
      gap: 20px;
    }}
    .nav-status {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.85rem;
      color: var(--text-muted);
      background: var(--surface);
      border: 1px solid var(--card-border);
      padding: 8px 16px;
      border-radius: 100px;
    }}
    .status-dot {{
      width: 8px;
      height: 8px;
      background: #10b981;
      border-radius: 50%;
      box-shadow: 0 0 8px #10b981;
      animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
      0% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(1.2); }}
      100% {{ opacity: 1; transform: scale(1); }}
    }}

    /* Hero Section */
    .hero {{
      padding: 80px 0 50px;
      text-align: center;
    }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(99, 102, 241, 0.12);
      border: 1px solid rgba(99, 102, 241, 0.3);
      color: #a5b4fc;
      padding: 6px 16px;
      border-radius: 100px;
      font-size: 0.88rem;
      font-weight: 600;
      margin-bottom: 24px;
    }}
    .hero h1 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 3.2rem;
      font-weight: 800;
      color: white;
      line-height: 1.15;
      letter-spacing: -1.5px;
      max-width: 980px;
      margin: 0 auto 20px;
    }}
    .hero h1 span {{
      background: linear-gradient(135deg, #818cf8 0%, #38bdf8 50%, #34d399 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero p {{
      color: var(--text-muted);
      font-size: 1.2rem;
      max-width: 780px;
      margin: 0 auto 40px;
      line-height: 1.6;
    }}

    /* Stats Grid */
    .stats-bar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px;
      max-width: 1100px;
      margin: 0 auto 60px;
    }}
    .stat-box {{
      background: var(--surface);
      border: 1px solid var(--card-border);
      padding: 24px;
      border-radius: 16px;
      text-align: center;
    }}
    .stat-box strong {{
      display: block;
      font-size: 2.2rem;
      font-family: 'Space Grotesk', sans-serif;
      color: white;
      letter-spacing: -1px;
    }}
    .stat-box span {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    /* Country & Industry Filter Bars */
    .country-selector {{
      display: flex;
      justify-content: center;
      gap: 12px;
      margin-bottom: 20px;
    }}
    .country-btn {{
      background: var(--surface-card);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 12px 24px;
      border-radius: 12px;
      font-weight: 800;
      font-size: 1rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }}
    .country-btn.active {{
      background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
      border-color: #6366f1;
      box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
    }}

    .filter-wrapper {{
      display: flex;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 45px;
    }}
    .filter-btn {{
      background: var(--surface);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      padding: 8px 18px;
      border-radius: 100px;
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .filter-btn:hover {{
      color: white;
      border-color: rgba(255, 255, 255, 0.25);
    }}
    .filter-btn.active {{
      background: rgba(255, 255, 255, 0.15);
      border-color: rgba(255, 255, 255, 0.4);
      color: white;
    }}

    /* Showcase Grid */
    .showcase-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
      gap: 30px;
      margin-bottom: 80px;
    }}
    .prototype-card {{
      background: var(--surface);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}
    .prototype-card:hover {{
      transform: translateY(-6px);
      border-color: var(--card-border-hover);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6), 0 0 25px rgba(99, 102, 241, 0.15);
    }}
    .card-visual {{
      height: 180px;
      position: relative;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .country-tag {{
      position: absolute;
      top: 14px;
      right: 16px;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 100px;
      letter-spacing: 0.5px;
    }}
    .uk-tag {{
      background: rgba(14, 165, 233, 0.2);
      border: 1px solid #0ea5e9;
      color: #7dd3fc;
    }}
    .us-tag {{
      background: rgba(239, 68, 68, 0.2);
      border: 1px solid #ef4444;
      color: #fca5a5;
    }}

    .card-badge {{
      align-self: flex-start;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: 6px;
      letter-spacing: 0.5px;
    }}
    .client-mark {{
      width: 48px;
      height: 48px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 800;
      font-size: 1.25rem;
      align-self: flex-end;
      box-shadow: 0 6px 16px rgba(0,0,0,0.4);
    }}

    .card-content {{
      padding: 26px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }}
    .card-location {{
      font-size: 0.82rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 8px;
      font-weight: 500;
    }}
    .card-title {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.35rem;
      font-weight: 700;
      color: white;
      margin-bottom: 6px;
    }}
    .card-trade {{
      color: #94a3b8;
      font-size: 0.9rem;
      margin-bottom: 20px;
      line-height: 1.4;
    }}

    .feature-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 26px;
      flex-grow: 1;
    }}
    .pill-feat {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #cbd5e1;
      font-size: 0.78rem;
      padding: 4px 10px;
      border-radius: 6px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .pill-svg {{
      display: inline-block;
      vertical-align: middle;
      flex-shrink: 0;
      color: var(--primary-light);
    }}

    .card-action {{
      margin-top: auto;
    }}
    .btn-demo {{
      display: block;
      width: 100%;
      text-align: center;
      padding: 14px 20px;
      border-radius: 12px;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      color: #ffffff;
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
      transition: all 0.2s ease;
    }}
    .btn-demo:hover {{
      transform: translateY(-2px);
      filter: brightness(1.15);
      box-shadow: 0 8px 25px rgba(0,0,0,0.5);
    }}

    /* Value Section */
    .value-section {{
      background: linear-gradient(135deg, #111827 0%, #0f172a 100%);
      border: 1px solid var(--card-border);
      border-radius: 24px;
      padding: 50px 40px;
      margin-bottom: 80px;
    }}
    .value-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 30px;
      margin-top: 35px;
    }}
    .value-card h4 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      color: white;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .value-card p {{
      color: var(--text-muted);
      font-size: 0.92rem;
      line-height: 1.6;
    }}

    /* CTA Section */
    .cta-banner {{
      background: radial-gradient(circle at 50% 0%, rgba(99, 102, 241, 0.25) 0%, transparent 70%), #0e121b;
      border: 1px solid rgba(99, 102, 241, 0.3);
      border-radius: 24px;
      padding: 60px 30px;
      text-align: center;
      margin-bottom: 80px;
    }}
    .cta-banner h2 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.4rem;
      color: white;
      margin-bottom: 16px;
      letter-spacing: -0.5px;
    }}
    .cta-banner p {{
      color: #cbd5e1;
      font-size: 1.15rem;
      max-width: 650px;
      margin: 0 auto 30px;
    }}
    .cta-actions {{
      display: flex;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .btn-claim {{
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: white;
      text-decoration: none;
      padding: 16px 36px;
      border-radius: 12px;
      font-weight: 800;
      font-size: 1.05rem;
      box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
      transition: all 0.2s;
    }}
    .btn-claim:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(16, 185, 129, 0.6);
    }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--card-border);
      padding: 40px 0;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.9rem;
    }}
    footer a {{ color: var(--text); text-decoration: none; font-weight: 600; }}
    footer a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>

  <!-- Navigation -->
  <nav>
    <div class="container nav-inner">
      <a href="#" class="brand">
        <div class="brand-mark">A</div>
        <div class="brand-name">
          ANTIGRAVITY
          <span class="brand-tag">DIGITAL AGENCY</span>
        </div>
      </a>
      <div class="nav-links">
        <div class="nav-status">
          <span class="status-dot"></span>
          <span>23 Live Prototypes Active</span>
        </div>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="hero container">
    <div class="hero-badge">
      ✦ High-Performance Architecture for American & British Trade Leaders
    </div>
    <h1>Engineered to Convert Homeowners Into <span>High-Ticket Contracts.</span></h1>
    <p>Explore our curated gallery of 23 bespoke digital prototypes across the UK and US, built with real-time project estimators, instant mobile dispatch routing, and sub-second speed.</p>

    <!-- Stats Bar -->
    <div class="stats-bar">
      <div class="stat-box">
        <strong>23</strong>
        <span>Live Trade Prototypes</span>
      </div>
      <div class="stat-box">
        <strong style="color: #38bdf8;">10</strong>
        <span>UK Dedicated Sites</span>
      </div>
      <div class="stat-box">
        <strong style="color: #10b981;">0.48s</strong>
        <span>Average Mobile Speed</span>
      </div>
      <div class="stat-box">
        <strong style="color: #e2e8f0;">£99 / $99</strong>
        <span>Flat Turnkey Package</span>
      </div>
    </div>

    <!-- Country Tabs -->
    <div class="country-selector">
      <button class="country-btn active" onclick="filterCountry('all', this)">All Prototypes (23)</button>
      <button class="country-btn" onclick="filterCountry('uk', this)">🇬🇧 UK Businesses (10)</button>
      <button class="country-btn" onclick="filterCountry('us', this)">🇺🇸 US Businesses (13)</button>
    </div>

    <!-- Filter Buttons -->
    <div class="filter-wrapper">
      <button class="filter-btn active" onclick="filterCategory('all', this)">All Trades</button>
      <button class="filter-btn" onclick="filterCategory('plumbing', this)">Plumbing & Heating</button>
      <button class="filter-btn" onclick="filterCategory('roofing', this)">Roofing</button>
      <button class="filter-btn" onclick="filterCategory('electrical', this)">Electrical</button>
      <button class="filter-btn" onclick="filterCategory('landscaping', this)">Landscaping & Paving</button>
      <button class="filter-btn" onclick="filterCategory('painting', this)">Painting & Decorating</button>
    </div>
  </section>

  <!-- Prototype Showcase Gallery -->
  <main class="container">
    <div class="showcase-grid" id="prototypeGrid">
      {cards_html}
    </div>
  </main>

  <!-- Agency Engineering Values -->
  <section class="container">
    <div class="value-section">
      <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.8rem; color: white; text-align: center;">The Antigravity Engineering Standard</h3>
      <p style="text-align: center; color: var(--text-muted); max-width: 680px; margin: 10px auto 0;">Why established contractors across the UK & US upgrade to our bespoke digital framework.</p>
      
      <div class="value-grid">
        <div class="value-card">
          <h4>🚀 Sub-Second Load Speeds</h4>
          <p>Zero slow WordPress plugins, heavy databases, or bloated page builders. Handcrafted vanilla CSS & HTML running on ultra-fast global edge CDNs.</p>
        </div>
        <div class="value-card">
          <h4>🧮 Interactive Project Estimators</h4>
          <p>Homeowners can immediately calculate project square footage and receive instant ballpark estimates, filtering out tire-kickers before your phone rings.</p>
        </div>
        <div class="value-card">
          <h4>🛡️ High-Trust Local Architecture</h4>
          <p>Deep integration of Gas Safe, NICEIC, NFRC, Chamber of Commerce seals, and £5M liability proof to justify premium pricing.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Client Inquiry & Claim Banner -->
  <section class="container">
    <div class="cta-banner">
      <h2>Ready to Claim or Customize Your Website?</h2>
      <p>Each design can be connected to your official company domain (.co.uk or .com) with full cloud hosting, SSL encryption, and direct lead routing in under 24 hours.</p>
      <div class="cta-actions">
        <a href="mailto:skykingly1@gmail.com?subject=Website%20Inquiry%20-%20Antigravity%20Digital%20Agency%20(%C2%A399)" class="btn-claim">
          Claim Your Prototype (£99 / $99 Flat)
        </a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <p style="margin-bottom: 8px;"><strong>Antigravity Digital Agency</strong> • High-Performance Web Systems for Trade Professionals</p>
      <p style="font-size: 0.85rem;">Founder: Sky King • Direct Inquiries: <a href="mailto:skykingly1@gmail.com">skykingly1@gmail.com</a></p>
      <p style="font-size: 0.8rem; margin-top: 14px; color: #64748b;">© 2026 Antigravity Digital Agency. All rights reserved.</p>
    </div>
  </footer>

  <script>
    let activeCountry = 'all';
    let activeCategory = 'all';

    function filterCountry(country, btn) {{
      document.querySelectorAll('.country-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCountry = country;
      applyFilters();
    }}

    function filterCategory(category, btn) {{
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCategory = category;
      applyFilters();
    }}

    function applyFilters() {{
      const cards = document.querySelectorAll('.prototype-card');
      cards.forEach(card => {{
        const cardCountry = card.getAttribute('data-country');
        const cardCategory = card.getAttribute('data-category');

        const matchCountry = (activeCountry === 'all' || cardCountry === activeCountry);
        const matchCategory = (activeCategory === 'all' || cardCategory === activeCategory);

        if (matchCountry && matchCategory) {{
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
    return html

if __name__ == "__main__":
    content = build_showcase_html()
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully built updated client-facing index.html with UK Businesses section!")
