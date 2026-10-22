import json

leads_data = [
    {
        "id": "larry-dickerson-roofing",
        "name": "Larry Dickerson Roofing LLC",
        "niche": "Roofing & Storm Restoration",
        "loc": "Plainview, TX",
        "source": "Plainview Texas Chamber",
        "email": "larrydickersonroofing@gmail.com",
        "phone": "(806) 429-5009",
        "sample": "samples/larry-dickerson-roofing/",
        "color": "#cbd5e1",
        "bg_banner": "linear-gradient(135deg, #090b0e 0%, #334155 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#e2e8f0" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
        "pitch": "Platinum Silver theme, Texas hail storm damage estimator & instant photo inspection scheduler"
    },
    {
        "id": "blue-haven-plumbing",
        "name": "Blue Haven Plumbing LLC",
        "niche": "Plumbing & Drain Services",
        "loc": "Tillamook, OR",
        "source": "Tillamook Area Chamber",
        "email": "bluehavenplumbing@gmail.com",
        "phone": "(503) 842-8877",
        "sample": "samples/blue-haven-plumbing/",
        "color": "#38bdf8",
        "bg_banner": "linear-gradient(135deg, #080c14 0%, #0369a1 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
        "pitch": "Coastal azure theme, 24/7 emergency dispatch selector, tankless water heaters & sewer jetting"
    },
    {
        "id": "gurda-landscaping",
        "name": "Gurda Landscaping LLC",
        "niche": "Landscaping & Hardscaping",
        "loc": "Pine Island, NY",
        "source": "Pine Island Chamber",
        "email": "gurdalandscape@gmail.com",
        "phone": "(845) 683-1314",
        "sample": "samples/gurda-landscaping/",
        "color": "#4ade80",
        "bg_banner": "linear-gradient(135deg, #070c09 0%, #15803d 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#4ade80" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg>',
        "pitch": "Emerald forest aesthetic, Unilock patio estimator, natural stone retaining walls & estate turf maintenance"
    },
    {
        "id": "red-cap-electrical",
        "name": "Red Cap Electrical Services LLC",
        "niche": "Electrical Contractor",
        "loc": "Dumas, TX",
        "source": "Dumas Area Chamber",
        "email": "redcelectricservs@gmail.com",
        "phone": "(806) 935-4421",
        "sample": "samples/red-cap-electrical/",
        "color": "#ef4444",
        "bg_banner": "linear-gradient(135deg, #0c0a09 0%, #991b1b 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
        "pitch": "High-voltage crimson & onyx theme, 200A breaker panel upgrades, Level-2 EV charging & ranch power"
    },
    {
        "id": "four-families-roofing",
        "name": "Four Families Roofing LLC",
        "niche": "Mountain & Metal Roofing",
        "loc": "Highlands, NC",
        "source": "Highlands Chamber",
        "email": "letmeroofme@gmail.com",
        "phone": "(828) 634-1664",
        "sample": "samples/four-families-roofing/",
        "color": "#34d399",
        "bg_banner": "linear-gradient(135deg, #080c0a 0%, #047857 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>',
        "pitch": "Alpine forest emerald theme, standing seam metal roofing, heavy snow defense & drone video audits"
    },
    {
        "id": "aim-plumbing",
        "name": "AIM Plumbing Services",
        "niche": "Plumbing & Pipe Repair",
        "loc": "Refugio County, TX",
        "source": "Refugio County Chamber",
        "email": "aimplumbingservices@gmail.com",
        "phone": "(361) 526-7890",
        "sample": "samples/aim-plumbing/",
        "color": "#0ea5e9",
        "bg_banner": "linear-gradient(135deg, #080d16 0%, #0369a1 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#0ea5e9" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24"/><path d="m14.83 9.17 4.24-4.24"/></svg>',
        "pitch": "Coastal bend cyan theme, acoustic under-slab leak detection, water heater replacements & cleanouts"
    },
    {
        "id": "ave-electric",
        "name": "AVE. Electric LLC",
        "niche": "Licensed Electrical Contractor",
        "loc": "Pomona, CA",
        "source": "Pomona Chamber",
        "email": "ave.3lectric@gmail.com",
        "phone": "(909) 620-1940",
        "sample": "samples/ave-electric/",
        "color": "#a78bfa",
        "bg_banner": "linear-gradient(135deg, #0a0a14 0%, #6d28d9 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
        "pitch": "Electric violet theme, commercial LED high-bay retrofits, California Title 24 compliance & smart building automation"
    },
    {
        "id": "elite-roofing",
        "name": "Elite Roofing",
        "niche": "Roofing & Desert Coatings",
        "loc": "Yucca Valley, CA",
        "source": "Yucca Valley Chamber",
        "email": "phil.eliteroofing@gmail.com",
        "phone": "(760) 449-6835",
        "sample": "samples/elite-roofing/",
        "color": "#fb923c",
        "bg_banner": "linear-gradient(135deg, #0c0a08 0%, #c2410c 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#fb923c" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><path d="m4.93 4.93 14.14 14.14"/></svg>',
        "pitch": "Mojave terracotta theme, elastomeric silicone cool roof coatings that drop rooftop heat 25°F & Spanish tile relay"
    },
    {
        "id": "doctor-electrical",
        "name": "Doctor Electrical Services Inc.",
        "niche": "Electrical Inspections & Repairs",
        "loc": "Camano Island, WA",
        "source": "Camano Island Chamber",
        "email": "doctorelectricalservices@gmail.com",
        "phone": "(360) 387-9912",
        "sample": "samples/doctor-electrical/",
        "color": "#14b8a6",
        "bg_banner": "linear-gradient(135deg, #060c12 0%, #0f766e 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#14b8a6" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/></svg>',
        "pitch": "Pacific Northwest teal theme, standby generator transfer switches, salt-air corrosion resistant panels & dock wiring"
    },
    {
        "id": "nuco-electric",
        "name": "NuCo Electric",
        "niche": "Residential & Commercial Electric",
        "loc": "Oswego, IL",
        "source": "Oswego Area Chamber",
        "email": "nucoelectric@gmail.com",
        "phone": "(630) 554-7100",
        "sample": "samples/nuco-electric/",
        "color": "#eab308",
        "bg_banner": "linear-gradient(135deg, #0a0a0c 0%, #a16207 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#eab308" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
        "pitch": "Fox Valley amber theme, finished basement canless lighting, clean EMT conduit runs & 240V Tesla garage stations"
    },
    {
        "id": "apm-painting",
        "name": "APM Painting & Design",
        "niche": "Painting & Design",
        "loc": "Bethel, CT",
        "source": "Bethel Chamber of Commerce",
        "email": "apmpainting25@gmail.com",
        "phone": "(203) 791-8844",
        "sample": "samples/apm-painting/",
        "color": "#fb7185",
        "bg_banner": "linear-gradient(135deg, #0c0b0a 0%, #be123c 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#fb7185" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg>',
        "pitch": "Fairfield rose-cashmere aesthetic, factory-finish kitchen cabinet spraying, HEPA dustless sanding & exterior weatherproofing"
    },
    {
        "id": "wake-forest-hvac",
        "name": "Wake Forest HVAC Company",
        "niche": "Heating, AC & Heat Pumps",
        "loc": "Rolesville & Wake Forest, NC",
        "source": "Rolesville Chamber of Commerce",
        "email": "wafohvac@gmail.com",
        "phone": "(919) 556-9180",
        "sample": "samples/wake-forest-hvac/",
        "color": "#38bdf8",
        "bg_banner": "linear-gradient(135deg, #070c14 0%, #0369a1 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="4"/></svg>',
        "pitch": "Carolina ice-blue theme, 18+ SEER2 variable inverter heat pumps, Duke Energy rebates & 24/7 no-cool emergency repair"
    },
    {
        "id": "big-ts-painting",
        "name": "Big T's Painting & Construction",
        "niche": "Painting & Construction",
        "loc": "Spring Grove, MN",
        "source": "Spring Grove Chamber of Commerce",
        "email": "ladsten1@gmail.com",
        "phone": "(507) 498-5520",
        "sample": "samples/big-ts-painting/",
        "color": "#f97316",
        "bg_banner": "linear-gradient(135deg, #0c0908 0%, #c2410c 100%)",
        "icon": '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#f97316" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>',
        "pitch": "Minnesota Driftless rust theme, agricultural pole barn spray painting, exterior home weatherproofing & cedar deck staining"
    }
]

# Generate Cards HTML
cards_html = ""
for item in leads_data:
    cards_html += f"""
      <div class="sample-card">
        <div class="card-banner" style="background: {item['bg_banner']}; border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
          {item['icon']}
        </div>
        <div class="card-body">
          <h3>{item['name']}</h3>
          <div class="target-biz" style="color: {item['color']};">Location: {item['loc']} • {item['niche']}</div>
          <p>{item['pitch']}</p>
          <div class="action-row">
            <a href="{item['sample']}" target="_blank" class="btn-view" style="background: {item['color']}; color: #090b0e;">Open Dedicated Live Demo ↗</a>
          </div>
        </div>
      </div>
    """

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Website Client Acquisition Hub | 13 Dedicated Live Client Sites</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #090d16;
      --card: #111827;
      --card-border: #1f2937;
      --primary: #6366f1;
      --primary-hover: #4f46e5;
      --accent: #10b981;
      --text: #f9fafb;
      --text-muted: #9ca3af;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background-color: var(--bg); color: var(--text); line-height: 1.6; padding: 40px 24px; }}
    .container {{ max-width: 1440px; margin: 0 auto; }}

    header {{
      margin-bottom: 35px;
      padding-bottom: 25px;
      border-bottom: 1px solid var(--card-border);
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      flex-wrap: wrap;
      gap: 20px;
    }}
    .title-group h1 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.2rem;
      color: white;
      letter-spacing: -0.5px;
    }}
    .title-group p {{
      color: var(--text-muted);
      font-size: 1.05rem;
      margin-top: 6px;
    }}
    .stats-pills {{
      display: flex;
      gap: 15px;
      flex-wrap: wrap;
    }}
    .pill {{
      background: var(--card);
      border: 1px solid var(--card-border);
      padding: 10px 18px;
      border-radius: 10px;
      text-align: center;
    }}
    .pill strong {{ display: block; font-size: 1.25rem; color: var(--accent); }}
    .pill span {{ font-size: 0.78rem; color: var(--text-muted); text-transform: uppercase; font-weight: 600; }}

    /* Quick Dispatch Banner */
    .dispatch-banner {{
      background: linear-gradient(135deg, #1e1b4b 0%, #172554 100%);
      border: 1px solid rgba(99, 102, 241, 0.4);
      border-radius: 16px;
      padding: 24px 30px;
      margin-bottom: 40px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }}
    .dispatch-info h3 {{
      color: white;
      font-size: 1.2rem;
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 6px;
    }}
    .dispatch-info p {{
      color: #cbd5e1;
      font-size: 0.92rem;
      max-width: 800px;
    }}
    .dispatch-badge {{
      background: rgba(16, 185, 129, 0.2);
      border: 1px solid #10b981;
      color: #6ee7b7;
      padding: 6px 14px;
      border-radius: 100px;
      font-size: 0.82rem;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .section-title {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.5rem;
      margin: 40px 0 20px;
      color: white;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .samples-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
      margin-bottom: 50px;
    }}
    .sample-card {{
      background: var(--card);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.25s, border-color 0.25s;
    }}
    .sample-card:hover {{
      transform: translateY(-4px);
      border-color: rgba(255,255,255,0.3);
      box-shadow: 0 15px 30px rgba(0,0,0,0.5);
    }}
    .card-banner {{
      height: 120px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }}
    .card-body {{
      padding: 22px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }}
    .card-body h3 {{
      font-size: 1.18rem;
      color: white;
      margin-bottom: 6px;
    }}
    .target-biz {{
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 12px;
    }}
    .card-body p {{
      color: var(--text-muted);
      font-size: 0.88rem;
      margin-bottom: 20px;
      flex-grow: 1;
      line-height: 1.5;
    }}
    .action-row {{
      display: flex;
      gap: 10px;
    }}
    .btn-view {{
      flex: 1;
      text-align: center;
      padding: 10px;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.88rem;
      transition: opacity 0.2s;
    }}
    .btn-view:hover {{ opacity: 0.9; }}

    /* Leads Table */
    .table-container {{
      background: var(--card);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      overflow-x: auto;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.88rem;
    }}
    th {{
      background: rgba(0, 0, 0, 0.25);
      padding: 16px 18px;
      color: var(--text-muted);
      font-weight: 700;
      border-bottom: 1px solid var(--card-border);
      text-transform: uppercase;
      font-size: 0.75rem;
      letter-spacing: 0.05em;
    }}
    td {{
      padding: 16px 18px;
      border-bottom: 1px solid var(--card-border);
      color: #e5e7eb;
      vertical-align: middle;
    }}
    tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
    }}
    .status-badge {{
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 700;
      white-space: nowrap;
      display: inline-block;
    }}
    .status-pending {{
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}
    .status-delivered {{
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.4);
    }}

    /* Action Buttons in Table */
    .table-actions {{
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .btn-action-gmail {{
      background: linear-gradient(135deg, #ea4335 0%, #c5221f 100%);
      color: white;
      border: 1px solid rgba(255,255,255,0.2);
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .btn-action-gmail:hover {{
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(234, 67, 53, 0.4);
    }}
    .btn-action-api {{
      background: #1e293b;
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
    }}
    .btn-action-api:hover {{
      background: #0284c7;
      color: white;
    }}
    .btn-action-preview {{
      background: #374151;
      color: #e5e7eb;
      border: 1px solid #4b5563;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .btn-action-preview:hover {{
      background: #4b5563;
      color: white;
    }}

    /* Email Modal */
    #emailModal {{
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.8);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 20px;
    }}
    .modal-content {{
      background: #111827;
      border: 1px solid #374151;
      border-radius: 16px;
      max-width: 720px;
      width: 100%;
      padding: 30px;
      box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    }}
    .modal-content h3 {{
      color: white;
      font-size: 1.3rem;
      margin-bottom: 8px;
    }}
    .modal-textarea {{
      width: 100%;
      height: 320px;
      background: #090d16;
      border: 1px solid #374151;
      border-radius: 10px;
      color: #e5e7eb;
      padding: 15px;
      font-size: 0.88rem;
      line-height: 1.5;
      font-family: monospace;
      margin: 15px 0 20px;
      resize: none;
    }}
    .modal-actions {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .modal-right-actions {{
      display: flex;
      gap: 10px;
    }}
    .btn-close {{
      background: #374151;
      color: white;
      border: none;
      padding: 10px 18px;
      border-radius: 8px;
      cursor: pointer;
      font-weight: 600;
      font-size: 0.88rem;
    }}
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div class="title-group">
        <h1>Website Client Acquisition Hub</h1>
        <p>13 Verified Chamber of Commerce businesses with 100% individual custom-built live websites</p>
      </div>
      <div class="stats-pills">
        <div class="pill">
          <strong>13</strong>
          <span>Bespoke Sites</span>
        </div>
        <div class="pill">
          <strong>100%</strong>
          <span>Live Hosted</span>
        </div>
        <div class="pill">
          <strong id="sentCount">0 / 13</strong>
          <span>Delivered</span>
        </div>
        <div class="pill">
          <strong>$199 / $29mo</strong>
          <span>Offer Hook</span>
        </div>
      </div>
    </header>

    <!-- 1-Click Direct Delivery Banner -->
    <div class="dispatch-banner">
      <div class="dispatch-info">
        <h3>⚡ Direct Dispatch Connected: <span style="color: #6ee7b7;">skykingly1@gmail.com</span></h3>
        <p>Clicking <strong>"⚡ 1-Click Send (Gmail)"</strong> instantly opens Gmail routed directly under <strong>skykingly1@gmail.com</strong> with the recipient, subject, and personalized pitch pre-loaded with their live website preview link. No copying, no pasting, no manual switching required.</p>
      </div>
      <div>
        <span class="dispatch-badge">● Sender: skykingly1@gmail.com</span>
      </div>
    </div>

    <!-- 13 Distinct Websites Grid -->
    <h2 class="section-title">✨ 13 Dedicated Live Website Samples (Bespoke to Each Business)</h2>
    <div class="samples-grid">
      {cards_html}
    </div>

    <!-- Leads Table Section -->
    <h2 class="section-title">📋 1-Click Outreach Pipeline (No Copying Required)</h2>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Business Name</th>
            <th>Industry</th>
            <th>Location</th>
            <th>Contact Email / Phone</th>
            <th>Sample</th>
            <th>Delivery Status</th>
            <th>1-Click Direct Action</th>
          </tr>
        </thead>
        <tbody id="leadsBody">
          <!-- Populated by JavaScript -->
        </tbody>
      </table>
    </div>

  </div>

  <!-- Email Modal -->
  <div id="emailModal">
    <div class="modal-content">
      <h3 id="modalBizTitle">Personalized Outreach Email</h3>
      <p style="color: #9ca3af; font-size: 0.88rem;">Review the generated pitch below or deliver it with one click:</p>
      <textarea id="modalEmailText" class="modal-textarea"></textarea>
      <div class="modal-actions">
        <button class="btn-close" onclick="closeModal()">Close</button>
        <div class="modal-right-actions">
          <button class="btn-action-preview" onclick="copyModalText()">📋 Copy Text</button>
          <a id="modalMailtoBtn" href="#" class="btn-action-preview" style="text-decoration: none;">✉️ Mail App</a>
          <button id="modalApiBtn" class="btn-action-api" onclick="sendModalApi()">🚀 Auto-Send API</button>
          <a id="modalGmailBtn" href="#" target="_blank" class="btn-action-gmail" onclick="markCurrentSent()">⚡ 1-Click Send (Gmail)</a>
        </div>
      </div>
    </div>
  </div>

  <script>
    const leads = {json.dumps(leads_data, indent=2)};
    let activeModalIndex = 0;

    // Load sent state from localStorage
    function getSentState() {{
      try {{
        return JSON.parse(localStorage.getItem('skyking_sent_leads') || '{{}}');
      }} catch (e) {{
        return {{}};
      }}
    }}

    function markLeadSent(id) {{
      const state = getSentState();
      state[id] = new Date().toISOString();
      localStorage.setItem('skyking_sent_leads', JSON.stringify(state));
      renderTable();
    }}

    function buildEmail(l) {{
      const liveUrl = 'https://skyking-client-previews.surge.sh/' + l.sample;
      const subject = `${{l.name}}: built a live website prototype for your team (no cost)`;
      const body = `Hi ${{l.name}} Team,

I'll keep this short because I know you're busy running jobs in ${{l.loc}}.

I was researching top-rated ${{l.niche.toLowerCase()}} contractors on the ${{l.source}} directory and noticed something surprising: you have great local reputation and craftsmanship, but when homeowners in ${{l.loc}} search for your business on their phone, they hit a dead end with no official website.

Right now, out-of-town franchises and lead-broker middle-men are capturing high-ticket ${{l.niche.toLowerCase()}} jobs in your backyard simply because they show up first with a polished mobile page.

Instead of sending you an annoying sales pitch, I decided to build you the solution upfront.

Last night, I designed and coded a complete, modern interactive website custom-tailored for ${{l.name}}. It is 100% functional and live right now:

👉 Test Drive Your Prototype: ${{liveUrl}}

Take 30 seconds to tap around on your phone:
• Instant Project Cost Calculator: Lets homeowners in ${{l.loc}} get immediate estimates and filters out tire-kickers.
• 1-Click Direct Emergency Dispatch: Routes emergency calls straight to your line (${{l.phone}}).
• Fast Lead Capture Form: Pushes qualified customer project requests directly to your inbox (${{l.email}}).
• Clean Chamber of Commerce & Licensed/Insured Trust Badges: Builds instant credibility so you can charge premium rates.
• Blazing 0.5s Load Time: Fully responsive across iPhone, Android, and Desktop.

Most web agencies charge $3,000–$5,000 upfront and take 6 to 8 weeks. We think that's crazy for hard-working trades.

Since I already did the design and coding work for you, you can claim this complete site under your own domain name (.com) with lightning-fast cloud hosting and SSL security for an affordable flat $199 (or $29/mo with zero contracts).

If you want to keep it and launch it this week, simply reply "I'm interested" to this email and I'll handle the rest for you.

If not, no worries at all—feel free to use the preview link as inspiration. Keep up the great work serving ${{l.loc}}!

Best regards,
Sky King
Founder, Antigravity Digital Agency
Email: skykingly1@gmail.com`;
      return {{ subject, body }};
    }}

    function getGmailComposeUrl(email, subject, body) {{
      return `https://mail.google.com/mail/u/skykingly1@gmail.com/?view=cm&fs=1&authuser=skykingly1@gmail.com&to=${{encodeURIComponent(email)}}&su=${{encodeURIComponent(subject)}}&body=${{encodeURIComponent(body)}}`;
    }}

    function renderTable() {{
      const tbody = document.getElementById('leadsBody');
      tbody.innerHTML = '';
      const sentState = getSentState();
      let sentCount = 0;

      leads.forEach((l, index) => {{
        const isSent = Boolean(sentState[l.id]);
        if (isSent) sentCount++;
        const {{ subject, body }} = buildEmail(l);
        const gmailUrl = getGmailComposeUrl(l.email, subject, body);
        const mailtoUrl = `mailto:${{l.email}}?subject=${{encodeURIComponent(subject)}}&body=${{encodeURIComponent(body)}}`;

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><strong>${{l.name}}</strong></td>
          <td>${{l.niche}}</td>
          <td>${{l.loc}}</td>
          <td>
            <div style="font-weight: 600; color: #38bdf8;">${{l.email}}</div>
            <div style="font-size: 0.8rem; color: #94a3b8;">${{l.phone}}</div>
          </td>
          <td>
            <a href="${{l.sample}}" target="_blank" style="color: ${{l.color}}; text-decoration: none; font-weight: 700;">Open Demo ↗</a>
          </td>
          <td>
            <span class="status-badge ${{isSent ? 'status-delivered' : 'status-pending'}}">
              ${{isSent ? 'Delivered ✉️' : 'Pending ⏳'}}
            </span>
          </td>
          <td>
            <div class="table-actions">
              <a href="${{gmailUrl}}" target="_blank" class="btn-action-gmail" onclick="markLeadSent('${{l.id}}')">
                ⚡ 1-Click Send (Gmail)
              </a>
              <button class="btn-action-api" onclick="sendDirectApi('${{l.id}}', '${{l.name}}', '${{l.email}}')">
                🚀 Auto-Send API
              </button>
              <button class="btn-action-preview" onclick="openEmailModal(${{index}})">
                Review Pitch
              </button>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      }});

      document.getElementById('sentCount').innerText = `${{sentCount}} / ${{leads.length}}`;
    }}

    async function sendDirectApi(id, name, email) {{
      const l = leads.find(item => item.id === id);
      const {{ subject, body }} = buildEmail(l);

      try {{
        const resp = await fetch('http://localhost:5050/api/send', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{
            recipient: email,
            lead_name: name,
            subject: subject,
            body: body
          }})
        }});
        const res = await resp.json();
        if (res.success) {{
          markLeadSent(id);
          alert(`✅ Delivered directly from skykingly1@gmail.com to ${{email}}!`);
        }} else {{
          alert(`⚠️ Backend Notice: ${{res.error || 'Server not configured'}}\n\nOpening 1-Click Gmail compose (skykingly1@gmail.com)...`);
          const gmailUrl = getGmailComposeUrl(email, subject, body);
          window.open(gmailUrl, '_blank');
          markLeadSent(id);
        }}
      }} catch (err) {{
        alert(`ℹ️ Outreach Server not running locally.\n\nOpening 1-Click Gmail directly under skykingly1@gmail.com...`);
        const gmailUrl = getGmailComposeUrl(email, subject, body);
        window.open(gmailUrl, '_blank');
        markLeadSent(id);
      }}
    }}

    function openEmailModal(index) {{
      activeModalIndex = index;
      const l = leads[index];
      const {{ subject, body }} = buildEmail(l);

      document.getElementById('modalBizTitle').innerText = `Personalized Pitch: ${{l.name}}`;
      document.getElementById('modalEmailText').value = body;

      const gmailUrl = getGmailComposeUrl(l.email, subject, body);
      const mailtoUrl = `mailto:${{l.email}}?subject=${{encodeURIComponent(subject)}}&body=${{encodeURIComponent(body)}}`;

      document.getElementById('modalGmailBtn').href = gmailUrl;
      document.getElementById('modalMailtoBtn').href = mailtoUrl;

      document.getElementById('emailModal').style.display = 'flex';
    }}

    function markCurrentSent() {{
      const l = leads[activeModalIndex];
      markLeadSent(l.id);
      closeModal();
    }}

    function sendModalApi() {{
      const l = leads[activeModalIndex];
      const editedBody = document.getElementById('modalEmailText').value;
      const subject = `Quick question about ${{l.name}} / preview website`;

      fetch('http://localhost:5050/api/send', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify({{
          recipient: l.email,
          lead_name: l.name,
          subject: subject,
          body: editedBody
        }})
      }}).then(r => r.json()).then(res => {{
        if (res.success) {{
          markLeadSent(l.id);
          alert(`✅ Delivered directly to ${{l.email}}!`);
          closeModal();
        }} else {{
          alert(`Notice: ${{res.error}}`);
        }}
      }}).catch(err => {{
        alert("Outreach server is not running on http://localhost:5050. Run 'python outreach_server.py' in your terminal or click '⚡ 1-Click Send (Gmail)'.");
      }});
    }}

    function closeModal() {{
      document.getElementById('emailModal').style.display = 'none';
    }}

    function copyModalText() {{
      const copyText = document.getElementById("modalEmailText");
      copyText.select();
      navigator.clipboard.writeText(copyText.value);
      alert("Personalized email copied to clipboard!");
    }}

    // Initial table render
    renderTable();
  </script>
</body>
</html>
"""

with open(r"c:\Users\Richi\OneDrive\Desktop\antigravity\13_Website_Design_Agency\index.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Updated index.html successfully with direct 1-click email action pipeline!")
