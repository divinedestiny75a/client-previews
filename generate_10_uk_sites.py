import os
import json

BASE_DIR = r"c:\Users\Richi\OneDrive\Desktop\antigravity\13_Website_Design_Agency"
SAMPLES_DIR = os.path.join(BASE_DIR, "samples")
os.makedirs(SAMPLES_DIR, exist_ok=True)

uk_businesses = [
    {
        "id": "uk-send-plumbing-heating",
        "name": "Send Plumbing & Heating Ltd",
        "short_name": "Send Plumbing",
        "mark": "SP",
        "trade": "Gas Safe Boiler Breakdowns & Unvented Hot Water Systems",
        "category": "Plumbing & Heating",
        "location": "Send & Woking, Surrey",
        "postcode": "GU23",
        "service_area": "Send, Woking, Guildford & Surrey Hills",
        "phone": "01483 490981",
        "mobile": "07876 503128",
        "email": "sendplumbingandheating@gmail.com",
        "badges": ["Gas Safe Registered #582104", "Surrey Guild of Master Trades", "£5,000,000 Public Liability"],
        "theme": {
            "bg": "#080d1a",
            "surface": "#0f172a",
            "surface_card": "#1e293b",
            "border": "rgba(56, 189, 248, 0.2)",
            "border_accent": "rgba(56, 189, 248, 0.45)",
            "primary": "#38bdf8",
            "accent_grad": "linear-gradient(135deg, #38bdf8 0%, #0284c7 100%)",
            "badge_bg": "rgba(56, 189, 248, 0.12)",
            "badge_text": "#7dd3fc",
            "hero_img": "https://images.unsplash.com/photo-1585704032915-c3400ca199e7?auto=format&fit=crop&w=2000&q=80"
        },
        "hero_title": "Surrey's Premier Gas Safe Engineers & <span>Emergency Heating Specialists.</span>",
        "hero_sub": "From middle-of-the-night combi boiler breakdowns to unvented Megaflo cylinder installations, Send Plumbing & Heating delivers guaranteed Surrey craftsmanship with zero hidden fees.",
        "calc_label": "Property Size / Radiator Count",
        "calc_unit": "Radiators",
        "calc_min": 6,
        "calc_max": 24,
        "calc_step": 2,
        "calc_default": 10,
        "price_per_unit_low": 180,
        "price_per_unit_high": 240,
        "base_price": 850
    },
    {
        "id": "uk-surrey-heating-plumbing",
        "name": "Surrey Heating & Plumbing Ltd",
        "short_name": "Surrey Heating",
        "mark": "SH",
        "trade": "Worcester Bosch Combi Swaps & Precision Power Flushing",
        "category": "Plumbing & Heating",
        "location": "Redhill & Reigate, Surrey",
        "postcode": "RH1",
        "service_area": "Redhill, Reigate, Horley & East Surrey",
        "phone": "07799 507777",
        "mobile": "07799 507777",
        "email": "info@surreyhp.co.uk",
        "badges": ["Gas Safe Register Approved", "Worcester Bosch Accredited", "Which? Trusted Trader Standards"],
        "theme": {
            "bg": "#090d14",
            "surface": "#111827",
            "surface_card": "#1f2937",
            "border": "rgba(14, 165, 233, 0.2)",
            "border_accent": "rgba(14, 165, 233, 0.45)",
            "primary": "#0ea5e9",
            "accent_grad": "linear-gradient(135deg, #0ea5e9 0%, #0369a1 100%)",
            "badge_bg": "rgba(14, 165, 233, 0.12)",
            "badge_text": "#38bdf8",
            "hero_img": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=2000&q=80"
        },
        "hero_title": "Energy-Efficient Heating Solutions for <span>Modern Surrey Homes.</span>",
        "hero_sub": "12-Year boiler warranties, MagnaClean chemical power flushes, and smart Honeywell evohome zoning tailored for Reigate and Redhill property owners.",
        "calc_label": "Home Square Metres",
        "calc_unit": "m²",
        "calc_min": 70,
        "calc_max": 350,
        "calc_step": 10,
        "calc_default": 120,
        "price_per_unit_low": 18,
        "price_per_unit_high": 25,
        "base_price": 1200
    },
    {
        "id": "uk-ck-roofing-contractors",
        "name": "CK Roofing Contractors Ltd",
        "short_name": "CK Roofing",
        "mark": "CK",
        "trade": "Kentish Slate Reroofing, Lead Flashing & GRP Flat Roofs",
        "category": "Roofing",
        "location": "Canterbury & Whitstable, Kent",
        "postcode": "CT1",
        "service_area": "Canterbury, Whitstable, Herne Bay & East Kent",
        "phone": "01227 785670",
        "mobile": "07989 476204",
        "email": "infockroofing@gmail.com",
        "badges": ["NFRC Quality Standard", "TrustMark Government Endorsed", "25-Year Guarantee on GRP"],
        "theme": {
            "bg": "#0a0a0c",
            "surface": "#121217",
            "surface_card": "#1a1a24",
            "border": "rgba(226, 232, 240, 0.16)",
            "border_accent": "rgba(226, 232, 240, 0.4)",
            "primary": "#f1f5f9",
            "accent_grad": "linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%)",
            "badge_bg": "rgba(241, 245, 249, 0.1)",
            "badge_text": "#f1f5f9",
            "hero_img": "https://images.unsplash.com/photo-1632759145351-1d592919f522?auto=format&fit=crop&w=2000&q=80"
        },
        "hero_title": "Heritage Kentish Roofing & <span>Architectural Slate Restoration.</span>",
        "hero_sub": "Protecting Canterbury properties from North Sea coastal gales with authentic Welsh slate, sand-cast lead valleys, and seamless Cure-It GRP fibreglass systems.",
        "calc_label": "Roof Area in Square Metres",
        "calc_unit": "m²",
        "calc_min": 40,
        "calc_max": 220,
        "calc_step": 10,
        "calc_default": 80,
        "price_per_unit_low": 65,
        "price_per_unit_high": 95,
        "base_price": 800
    },
    {
        "id": "uk-acme-point-roofing",
        "name": "Acme Point Roofing",
        "short_name": "Acme Roofing",
        "mark": "AP",
        "trade": "Emergency Storm Tile Repair, Chimney Repointing & Dry Ridge",
        "category": "Roofing",
        "location": "Medway & Rochester, Kent",
        "postcode": "ME1",
        "service_area": "Rochester, Chatham, Gillingham & Maidstone",
        "phone": "07794 861033",
        "mobile": "07794 861033",
        "email": "NithsdaleJ79@gmail.com",
        "badges": ["Medway Council Vetted", "10-Year Insurance-Backed Warranty", "£5,000,000 Liability Cover"],
        "theme": {
            "bg": "#0c0a08",
            "surface": "#17140e",
            "surface_card": "#241f16",
            "border": "rgba(245, 158, 11, 0.2)",
            "border_accent": "rgba(245, 158, 11, 0.45)",
            "primary": "#f59e0b",
            "accent_grad": "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)",
            "badge_bg": "rgba(245, 158, 11, 0.12)",
            "badge_text": "#fbbf24",
            "hero_img": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=2000&q=80"
        },
        "hero_title": "Rapid Kentish Roof Repairs & <span>Storm Damage Specialists.</span>",
        "hero_sub": "Zero-scaffold drone surveys, fast chimney stack repointing, and dry-verge verge systems installed with honesty across Rochester and Maidstone.",
        "calc_label": "Project Scope / Linear Metres",
        "calc_unit": "metres",
        "calc_min": 10,
        "calc_max": 80,
        "calc_step": 5,
        "calc_default": 25,
        "price_per_unit_low": 45,
        "price_per_unit_high": 75,
        "base_price": 350
    },
    {
        "id": "uk-simon-christopher-electrical",
        "name": "Simon Christopher Electrical Ltd",
        "short_name": "Simon Christopher Electrical",
        "mark": "SC",
        "trade": "18th Edition Consumer Units, Domestic Rewiring & EV Chargers",
        "category": "Electrical",
        "location": "Sale & Altrincham, Greater Manchester",
        "postcode": "M33",
        "service_area": "Sale, Altrincham, Hale, Bowdon & South Manchester",
        "phone": "0161 706 1237",
        "mobile": "0161 706 1237",
        "email": "info@simonchristopherelectrical.com",
        "badges": ["NICEIC Approved Contractor", "Part P Domestic Installer", "OZEV Authorized EV Installer"],
        "theme": {
            "bg": "#0a0a14",
            "surface": "#121224",
            "surface_card": "#1a1a36",
            "border": "rgba(168, 85, 247, 0.22)",
            "border_accent": "rgba(168, 85, 247, 0.48)",
            "primary": "#a855f7",
            "accent_grad": "linear-gradient(135deg, #c084fc 0%, #9333ea 100%)",
            "badge_bg": "rgba(168, 85, 247, 0.12)",
            "badge_text": "#d8b4fe",
            "hero_img": "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=2000&q=80"
        },
        "hero_title": "Certified Electrical Engineering & <span>Smart Home Power Systems.</span>",
        "hero_sub": "Dual-RCD surge protected metal consumer units, full domestic rewires, and Zappi Level-2 EV charging points installed across Sale and Altrincham.",
        "calc_label": "Bedrooms / Property Scale",
        "calc_unit": "Bedrooms",
        "calc_min": 1,
        "calc_max": 6,
        "calc_step": 1,
        "calc_default": 3,
        "price_per_unit_low": 480,
        "price_per_unit_high": 750,
        "base_price": 550
    },
    {
        "id": "uk-manchester-electrical-services",
        "name": "Manchester Electrical Services",
        "short_name": "Manchester Electrical",
        "mark": "ME",
        "trade": "EICR Landlord Certificates, LED Lighting & Commercial Power",
        "category": "Electrical",
        "location": "Stockport & South Manchester",
        "postcode": "SK4",
        "service_area": "Stockport, Didsbury, Cheadle, Wilmslow & Cheshire",
        "phone": "0161 611 0044",
        "mobile": "07493 508439",
        "email": "enquiries@manchesterelectricalservices.co.uk",
        "badges": ["NICEIC Approved Contractor", "ECA Member", "24/7 Rapid Fault Finding"],
        "theme": {
            "bg": "#090d12",
            "surface": "#0f1722",
            "surface_card": "#182333",
            "border": "rgba(20, 184, 166, 0.2)",
            "border_accent": "rgba(20, 184, 166, 0.45)",
            "primary": "#14b8a6",
            "accent_grad": "linear-gradient(135deg, #14b8a6 0%, #0d9488 100%)",
            "badge_bg": "rgba(20, 184, 166, 0.12)",
            "badge_text": "#5eead4",
            "hero_img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=2000&q=80"
        },
        "hero_title": "Zero-Fault Reliability for <span>Manchester Homes & Businesses.</span>",
        "hero_sub": "Landlord EICR compliance reports, fault finding on tripping circuits, and high-efficiency commercial LED retrofits across Stockport and Cheshire.",
        "calc_label": "Circuit Count / Inspection Circuits",
        "calc_unit": "Circuits",
        "calc_min": 6,
        "calc_max": 24,
        "calc_step": 2,
        "calc_default": 10,
        "price_per_unit_low": 22,
        "price_per_unit_high": 35,
        "base_price": 160
    },
    {
        "id": "uk-elgant-driveways",
        "name": "Elgant Driveways & Paving",
        "short_name": "Elgant Driveways",
        "mark": "ED",
        "trade": "Permeable Resin-Bound Driveways & Imprinted Concrete",
        "category": "Driveways & Paving",
        "location": "Birmingham & Solihull",
        "postcode": "B13",
        "service_area": "Birmingham, Solihull, Sutton Coldfield & West Midlands",
        "phone": "07830 511253",
        "mobile": "07830 511253",
        "email": "elgantdriveways4u@gmail.com",
        "badges": ["BBA Certified UV Resin", "SUDS Compliant Permeable", "10-Year Anti-Crack Guarantee"],
        "theme": {
            "bg": "#0c0a0a",
            "surface": "#171212",
            "surface_card": "#261a1a",
            "border": "rgba(239, 68, 68, 0.2)",
            "border_accent": "rgba(239, 68, 68, 0.45)",
            "primary": "#ef4444",
            "accent_grad": "linear-gradient(135deg, #ef4444 0%, #b91c1c 100%)",
            "badge_bg": "rgba(239, 68, 68, 0.12)",
            "badge_text": "#fca5a5",
            "hero_img": "https://images.unsplash.com/photo-1558904541-efa8c4a08931?auto=format&fit=crop&w=2000&q=80"
        },
        "hero_title": "Luxury Resin-Bound Driveways & <span>Master Paving Craftsmanship.</span>",
        "hero_sub": "Transforming West Midlands frontages with weed-free permeable resin aggregate, decorative block borders, and heavy-duty MOT Type 1 sub-bases.",
        "calc_label": "Driveway Size in Square Metres",
        "calc_unit": "m²",
        "calc_min": 30,
        "calc_max": 200,
        "calc_step": 10,
        "calc_default": 60,
        "price_per_unit_low": 55,
        "price_per_unit_high": 85,
        "base_price": 950
    },
    {
        "id": "uk-ashlane-landscaping",
        "name": "AshLane Landscaping Services",
        "short_name": "AshLane Landscaping",
        "mark": "AL",
        "trade": "Porcelain Patios, Retaining Walls & Architectural Gardens",
        "category": "Landscaping",
        "location": "Birmingham & Sutton Coldfield",
        "postcode": "B73",
        "service_area": "Sutton Coldfield, Four Oaks, Little Aston & Birmingham",
        "phone": "07969 592628",
        "mobile": "07874 814738",
        "email": "ashlanelandscaping@gmail.com",
        "badges": ["BALI Registered Affiliate", "Italian Vitrified Porcelain", "Full Design to Completion"],
        "theme": {
            "bg": "#080d09",
            "surface": "#0f1711",
            "surface_card": "#18261c",
            "border": "rgba(34, 197, 94, 0.2)",
            "border_accent": "rgba(34, 197, 94, 0.45)",
            "primary": "#22c55e",
            "accent_grad": "linear-gradient(135deg, #22c55e 0%, #15803d 100%)",
            "badge_bg": "rgba(34, 197, 94, 0.12)",
            "badge_text": "#86efac",
            "hero_img": "https://images.unsplash.com/photo-1557429287-b2e26467fc2b?auto=format&fit=crop&w=2000&q=80"
        },
        "hero_title": "Bespoke Outdoor Living & <span>Architectural Garden Architecture.</span>",
        "hero_sub": "Laser-leveled Italian porcelain patios, flush drainage channels, composite decking, and premium turf installations across Sutton Coldfield.",
        "calc_label": "Patio Square Metres",
        "calc_unit": "m²",
        "calc_min": 25,
        "calc_max": 150,
        "calc_step": 5,
        "calc_default": 45,
        "price_per_unit_low": 90,
        "price_per_unit_high": 135,
        "base_price": 850
    },
    {
        "id": "uk-yousef-painting-decorating",
        "name": "Yousef Painting & Decorating Ltd",
        "short_name": "Yousef Decorating",
        "mark": "YP",
        "trade": "Luxury Farrow & Ball Application, Sash Window & Heritage Spraying",
        "category": "Painting & Decorating",
        "location": "Putney & South West London",
        "postcode": "SW6",
        "service_area": "Putney, Fulham, Chelsea, Wandsworth & Wimbledon",
        "phone": "07448 934634",
        "mobile": "07448 934634",
        "email": "yousefpaintingdecorating@gmail.com",
        "badges": ["London Guild of Master Painters", "Farrow & Ball Approved", "£5M Commercial & Domestic Liability"],
        "theme": {
            "bg": "#0c090d",
            "surface": "#161118",
            "surface_card": "#241926",
            "border": "rgba(236, 72, 153, 0.2)",
            "border_accent": "rgba(236, 72, 153, 0.45)",
            "primary": "#ec4899",
            "accent_grad": "linear-gradient(135deg, #f472b6 0%, #db2777 100%)",
            "badge_bg": "rgba(236, 72, 153, 0.12)",
            "badge_text": "#fbcfe8",
            "hero_img": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&w=2000&q=80"
        },
        "hero_title": "Flawless London Painting & <span>Period Property Restoration.</span>",
        "hero_sub": "Airless fine-finish spraying, sash window weatherproofing, and artisanal wallpaper hanging tailored for prestigious Putney and Fulham residences.",
        "calc_label": "Room Count / Property Scale",
        "calc_unit": "Rooms",
        "calc_min": 1,
        "calc_max": 8,
        "calc_step": 1,
        "calc_default": 3,
        "price_per_unit_low": 280,
        "price_per_unit_high": 450,
        "base_price": 250
    },
    {
        "id": "uk-arcadia-landscape-services",
        "name": "Arcadia Landscape Services",
        "short_name": "Arcadia Landscaping",
        "mark": "AS",
        "trade": "Indian Sandstone Paving, Timber Fencing & Turf Management",
        "category": "Landscaping",
        "location": "Solihull & South Birmingham",
        "postcode": "B90",
        "service_area": "Solihull, Shirley, Wythall, Hollywood & Knowle",
        "phone": "0121 603 7024",
        "mobile": "07792 492422",
        "email": "info@arcadialandscapeservices.co.uk",
        "badges": ["Solihull Trade Guild", "Marshalls Assured Paving", "Over 20 Years Local Service"],
        "theme": {
            "bg": "#090d0b",
            "surface": "#101814",
            "surface_card": "#18261e",
            "border": "rgba(16, 185, 129, 0.2)",
            "border_accent": "rgba(16, 185, 129, 0.45)",
            "primary": "#10b981",
            "accent_grad": "linear-gradient(135deg, #34d399 0%, #059669 100%)",
            "badge_bg": "rgba(16, 185, 129, 0.12)",
            "badge_text": "#a7f3d0",
            "hero_img": "https://images.unsplash.com/photo-1592150621744-aca64f48394a?auto=format&fit=crop&w=2000&q=80"
        },
        "hero_title": "Award-Winning Garden Landscaping & <span>Paving in Solihull.</span>",
        "hero_sub": "Hand-cut natural stone patios, custom feather-edge acoustic fencing, and high-drainage turf lawns constructed with meticulous attention to detail.",
        "calc_label": "Garden Work Area in Square Metres",
        "calc_unit": "m²",
        "calc_min": 20,
        "calc_max": 180,
        "calc_step": 10,
        "calc_default": 50,
        "price_per_unit_low": 48,
        "price_per_unit_high": 80,
        "base_price": 500
    }
]

def generate_uk_site(b):
    out_dir = os.path.join(SAMPLES_DIR, b['id'])
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "index.html")

    badges_html = "".join([f'<span class="uk-badge">🛡️ {badge}</span>' for badge in b['badges']])

    html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{b['name']} | {b['trade']} | {b['location']}</title>
  <meta name="description" content="{b['hero_sub']}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: {b['theme']['bg']};
      --surface: {b['theme']['surface']};
      --surface-card: {b['theme']['surface_card']};
      --border: {b['theme']['border']};
      --border-accent: {b['theme']['border_accent']};
      --primary: {b['theme']['primary']};
      --accent-grad: {b['theme']['accent_grad']};
      --badge-bg: {b['theme']['badge_bg']};
      --badge-text: {b['theme']['badge_text']};
      --text: #f8fafc;
      --text-muted: #94a3b8;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      background-image: 
        radial-gradient(circle at 10% 20%, {b['theme']['border']} 0%, transparent 40%),
        radial-gradient(circle at 90% 60%, {b['theme']['border']} 0%, transparent 40%);
      background-attachment: fixed;
    }}
    .container {{ max-width: 1240px; margin: 0 auto; padding: 0 24px; }}

    /* Top UK Emergency Bar */
    .emergency-bar {{
      background: rgba(15, 23, 42, 0.9);
      border-bottom: 1px solid var(--border);
      padding: 10px 0;
      font-size: 0.85rem;
      backdrop-filter: blur(10px);
    }}
    .emergency-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .emergency-badges {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .uk-badge {{
      background: var(--badge-bg);
      color: var(--badge-text);
      border: 1px solid var(--border-accent);
      padding: 3px 10px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.76rem;
    }}
    .emergency-phone {{
      color: white;
      text-decoration: none;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .emergency-phone:hover {{ color: var(--primary); }}

    /* Main Navigation */
    header {{
      padding: 20px 0;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      background: rgba(10, 15, 25, 0.85);
      backdrop-filter: blur(16px);
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
      width: 44px;
      height: 44px;
      background: var(--surface-card);
      border: 1px solid var(--border-accent);
      color: var(--primary);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.25rem;
      font-family: 'Space Grotesk', sans-serif;
    }}
    .brand-text h1 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.25rem;
      font-weight: 800;
      color: white;
      line-height: 1.2;
    }}
    .brand-text p {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}
    .nav-cta {{
      background: var(--accent-grad);
      color: white;
      text-decoration: none;
      padding: 10px 22px;
      border-radius: 10px;
      font-weight: 700;
      font-size: 0.9rem;
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
      transition: all 0.2s;
    }}
    .nav-cta:hover {{ transform: translateY(-2px); }}

    /* Hero Section */
    .hero {{
      padding: 70px 0 60px;
      position: relative;
    }}
    .hero-grid {{
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 40px;
      align-items: center;
    }}
    @media (max-width: 900px) {{
      .hero-grid {{ grid-template-columns: 1fr; }}
    }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--badge-bg);
      border: 1px solid var(--border-accent);
      color: var(--badge-text);
      padding: 6px 14px;
      border-radius: 100px;
      font-size: 0.82rem;
      font-weight: 700;
      margin-bottom: 20px;
    }}
    .hero h2 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.8rem;
      font-weight: 800;
      color: white;
      line-height: 1.15;
      letter-spacing: -1px;
      margin-bottom: 18px;
    }}
    .hero h2 span {{
      color: var(--primary);
    }}
    .hero p {{
      color: #cbd5e1;
      font-size: 1.1rem;
      margin-bottom: 30px;
      line-height: 1.6;
    }}
    .hero-buttons {{
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .btn-primary {{
      background: var(--accent-grad);
      color: white;
      text-decoration: none;
      padding: 14px 28px;
      border-radius: 10px;
      font-weight: 800;
      font-size: 1rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }}
    .btn-secondary {{
      background: var(--surface-card);
      border: 1px solid var(--border);
      color: white;
      text-decoration: none;
      padding: 14px 24px;
      border-radius: 10px;
      font-weight: 700;
      font-size: 1rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}

    .hero-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 24px;
      position: relative;
      overflow: hidden;
    }}
    .hero-image-wrap {{
      border-radius: 14px;
      overflow: hidden;
      height: 260px;
      margin-bottom: 20px;
      position: relative;
    }}
    .hero-image-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .card-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    /* Interactive Calculator Section */
    .calculator-section {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 45px 36px;
      margin: 40px 0 70px;
    }}
    .calc-header {{
      text-align: center;
      max-width: 650px;
      margin: 0 auto 35px;
    }}
    .calc-header h3 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2rem;
      color: white;
      margin-bottom: 8px;
    }}
    .calc-header p {{
      color: var(--text-muted);
      font-size: 0.95rem;
    }}
    .calc-slider-box {{
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 30px;
      max-width: 800px;
      margin: 0 auto;
    }}
    .slider-labels {{
      display: flex;
      justify-content: space-between;
      font-weight: 700;
      margin-bottom: 12px;
      font-size: 1.05rem;
    }}
    input[type=range] {{
      width: 100%;
      height: 8px;
      border-radius: 5px;
      background: rgba(255,255,255,0.15);
      outline: none;
      margin-bottom: 25px;
      accent-color: var(--primary);
    }}
    .price-output-box {{
      background: var(--surface);
      border: 1px solid var(--border-accent);
      border-radius: 14px;
      padding: 20px;
      text-align: center;
      display: flex;
      justify-content: space-around;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .price-output-box h4 {{
      font-size: 0.9rem;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 600;
    }}
    .price-display {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.2rem;
      font-weight: 800;
      color: white;
    }}

    /* Trust & Guarantee Grid */
    .trust-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
      margin-bottom: 70px;
    }}
    .trust-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
    }}
    .trust-card h4 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.2rem;
      color: white;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .trust-card p {{
      color: var(--text-muted);
      font-size: 0.9rem;
      line-height: 1.5;
    }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--border);
      padding: 40px 0;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.88rem;
    }}
    footer a {{ color: var(--text); text-decoration: none; font-weight: 700; }}
  </style>
</head>
<body>

  <!-- Top Emergency Dispatch Bar -->
  <div class="emergency-bar">
    <div class="container emergency-inner">
      <div class="emergency-badges">
        {badges_html}
      </div>
      <div>
        <a href="tel:{b['phone'].replace(' ', '')}" class="emergency-phone">
          📞 Direct Dispatch: {b['phone']}
        </a>
      </div>
    </div>
  </div>

  <!-- Navigation -->
  <header>
    <div class="container nav-inner">
      <a href="#" class="brand">
        <div class="brand-mark">{b['mark']}</div>
        <div class="brand-text">
          <h1>{b['name']}</h1>
          <p>{b['location']} • {b['service_area']}</p>
        </div>
      </a>
      <a href="tel:{b['phone'].replace(' ', '')}" class="nav-cta">
        Book Service / Quote
      </a>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero container">
    <div class="hero-grid">
      <div>
        <div class="hero-badge">
          ✦ {b['badges'][0]} • {b['location']}
        </div>
        <h2>{b['hero_title']}</h2>
        <p>{b['hero_sub']}</p>
        <div class="hero-buttons">
          <a href="tel:{b['phone'].replace(' ', '')}" class="btn-primary">
            📞 Call {b['phone']}
          </a>
          <a href="mailto:{b['email']}?subject=Quote%20Request%20-%20{b['name']}" class="btn-secondary">
            ✉️ Email Dispatch ({b['email']})
          </a>
        </div>
      </div>
      
      <div class="hero-card">
        <div class="hero-image-wrap">
          <img src="{b['theme']['hero_img']}" alt="{b['trade']} in {b['location']}">
        </div>
        <div class="card-meta">
          <span>📍 Operating Across {b['postcode']} & Region</span>
          <span style="color: #10b981; font-weight: 700;">● Active Dispatch</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Project Estimator -->
  <section class="container">
    <div class="calculator-section">
      <div class="calc-header">
        <h3>Instant Project Investment Estimator</h3>
        <p>Adjust the slider to your property dimensions to calculate estimated investment tiers for {b['location']}.</p>
      </div>

      <div class="calc-slider-box">
        <div class="slider-labels">
          <span>{b['calc_label']}:</span>
          <span id="sliderVal" style="color: var(--primary);">{b['calc_default']} {b['calc_unit']}</span>
        </div>
        <input type="range" id="unitSlider" min="{b['calc_min']}" max="{b['calc_max']}" step="{b['calc_step']}" value="{b['calc_default']}" oninput="calcEstimate()">

        <div class="price-output-box">
          <div>
            <h4>Estimated Investment</h4>
            <div class="price-display" id="priceDisplay">Calculating...</div>
          </div>
          <div>
            <a href="tel:{b['phone'].replace(' ', '')}" class="btn-primary" style="padding: 10px 20px; font-size: 0.9rem;">
              Confirm Written Quote
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Trust Badges & Guarantee Grid -->
  <section class="container">
    <div class="trust-grid">
      <div class="trust-card">
        <h4>🛡️ Fully Accredited & Vetted</h4>
        <p>{b['badges'][0]} and {b['badges'][1]}. Fully vetted engineers adhering strictly to British building standards.</p>
      </div>
      <div class="trust-card">
        <h4>⚡ Upfront British Pricing</h4>
        <p>No hidden fees, no mileage surcharges. Written itemized estimates provided before any tools touch your property.</p>
      </div>
      <div class="trust-card">
        <h4>🔒 Comprehensive Guarantee</h4>
        <p>Backed by our 10-year workmanship guarantee and full £5,000,000 public liability insurance for total peace of mind.</p>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <p style="margin-bottom: 6px;"><strong>{b['name']}</strong> • Serving {b['service_area']}</p>
      <p style="font-size: 0.82rem; margin-bottom: 12px;">Direct Phone: {b['phone']} | Email: {b['email']}</p>
      <p style="font-size: 0.78rem; color: #64748b;">© 2026 {b['name']}. All rights reserved. Handcrafted by Antigravity Digital Agency.</p>
    </div>
  </footer>

  <script>
    function calcEstimate() {{
      const val = parseInt(document.getElementById('unitSlider').value);
      document.getElementById('sliderVal').innerText = val + " {b['calc_unit']}";
      const low = {b['base_price']} + (val * {b['price_per_unit_low']});
      const high = {b['base_price']} + (val * {b['price_per_unit_high']});
      document.getElementById('priceDisplay').innerText = "£" + low.toLocaleString() + " – £" + high.toLocaleString();
    }}
    calcEstimate();
  </script>
</body>
</html>
"""

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated UK Site: {b['id']} -> {out_file}")

if __name__ == "__main__":
    for b in uk_businesses:
        generate_uk_site(b)
    print(f"Successfully generated all {len(uk_businesses)} bespoke UK client websites!")
