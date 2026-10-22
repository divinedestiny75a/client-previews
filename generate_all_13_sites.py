import os
import json

BASE_DIR = r"c:\Users\Richi\OneDrive\Desktop\antigravity\13_Website_Design_Agency"
SAMPLES_DIR = os.path.join(BASE_DIR, "samples")

businesses = [
    {
        "id": "larry-dickerson-roofing",
        "name": "Larry Dickerson Roofing LLC",
        "short_name": "Dickerson Roofing",
        "mark": "LD",
        "trade": "Architectural Roofing & Storm Restoration",
        "category": "Roofing Contractor",
        "location": "Plainview, TX",
        "service_area": "Plainview, Hale County & South Plains",
        "source": "Plainview Texas Chamber of Commerce",
        "phone": "(806) 429-5009",
        "email": "larrydickersonroofing@gmail.com",
        "theme": {
            "bg": "#090b0e",
            "surface": "#10141b",
            "surface_card": "#151b24",
            "border": "rgba(226, 232, 240, 0.12)",
            "border_accent": "rgba(226, 232, 240, 0.32)",
            "primary": "#e2e8f0",
            "primary_dim": "#94a3b8",
            "accent_grad": "linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%)",
            "badge_bg": "rgba(226, 232, 240, 0.08)",
            "badge_text": "#e2e8f0",
            "hero_img": "https://images.unsplash.com/photo-1632759145351-1d592919f522?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1632759145351-1d592919f522?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1541888946425-d0fbb186c5f8?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Master Titanium & Texas Hail Storm Protection",
        "hero_title": "Master Craftsmanship Built to <span>Withstand Texas Weather.</span>",
        "hero_sub": "From high-impact hail storm restoration to complete architectural replacements, Larry Dickerson Roofing LLC delivers commercial-grade durability with honest Plainview pricing.",
        "stats": [
            {"val": "4.9★", "label": "Google Rating Across Plainview"},
            {"val": "100%", "label": "Owens Corning Certified Materials"},
            {"val": "10-Yr", "label": "Comprehensive Workmanship Guarantee"},
            {"val": "$0", "label": "Inspection Fee & Itemized Estimate"}
        ],
        "tool_type": "calculator",
        "tool_title": "Instant Roof Investment Calculator",
        "tool_sub": "Drag the slider to your home's square footage to estimate architectural shingle replacement investment.",
        "services": [
            {
                "title": "Architectural Shingle Replacement",
                "desc": "Heavy-duty Class 4 impact shingles engineered to resist 130 MPH winds and extreme Panhandle heat cycles.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/><path d="M2 10.5 12 3l10 7.5"/></svg>'
            },
            {
                "title": "Hail & Wind Damage Restoration",
                "desc": "Detailed 21-point photo documentation and insurance adjuster advocacy to ensure complete claim payouts.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/><path d="m13 13-3 5h4l-3 5"/></svg>'
            },
            {
                "title": "Commercial Flat & Standing Seam",
                "desc": "Durable TPO membrane systems, agricultural barn roofing, and standing seam steel built for zero leaks.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01M16 6h.01M12 6h.01M8 10h.01M12 10h.01M16 10h.01"/></svg>'
            }
        ],
        "faqs": [
            {"q": "How quickly can Larry Dickerson Roofing inspect after a storm?", "a": "We dispatch within 24 hours across Plainview and Hale County to provide tarping and full photographic drone documentation for your insurance company."},
            {"q": "Do you help homeowners with insurance claims?", "a": "Yes! We meet directly with your insurance adjuster on-site to verify all hail hits, perimeter flashing damage, and gutter impacts so your claim covers full replacement costs."},
            {"q": "What warranties come with your installations?", "a": "We provide a 10-year written workmanship warranty backed by Owens Corning and GAF lifetime manufacturer shingle warranties."}
        ]
    },
    {
        "id": "blue-haven-plumbing",
        "name": "Blue Haven Plumbing LLC",
        "short_name": "Blue Haven Plumbing",
        "mark": "BH",
        "trade": "Precision Plumbing & Emergency Drain Services",
        "category": "Plumbing & Drain Services",
        "location": "Tillamook, OR",
        "service_area": "Tillamook County & Oregon Coast",
        "source": "Tillamook Area Chamber of Commerce",
        "phone": "(503) 842-8877",
        "email": "bluehavenplumbing@gmail.com",
        "theme": {
            "bg": "#080c14",
            "surface": "#0d1422",
            "surface_card": "#121b2d",
            "border": "rgba(56, 189, 248, 0.14)",
            "border_accent": "rgba(56, 189, 248, 0.35)",
            "primary": "#38bdf8",
            "primary_dim": "#7dd3fc",
            "accent_grad": "linear-gradient(135deg, #38bdf8 0%, #0284c7 50%, #0369a1 100%)",
            "badge_bg": "rgba(56, 189, 248, 0.1)",
            "badge_text": "#38bdf8",
            "hero_img": "https://images.unsplash.com/photo-1585704032915-c3400ca199e7?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1585704032915-c3400ca199e7?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Licensed Master Plumber • 24/7 Coastal Emergency Dispatch",
        "hero_title": "Rapid Coastal Plumbing & <span>Zero-Surprise Pricing.</span>",
        "hero_sub": "From middle-of-the-night burst pipes to high-efficiency tankless water heaters, Blue Haven Plumbing delivers guaranteed craftsmanship across Tillamook County.",
        "stats": [
            {"val": "45m", "label": "Average Emergency Response Time"},
            {"val": "100%", "label": "Upfront Flat-Rate Guaranteed Pricing"},
            {"val": "24/7", "label": "On-Call Coastal Service Technicians"},
            {"val": "100%", "label": "Licensed, Bonded & Insured"}
        ],
        "tool_type": "diagnostic",
        "tool_title": "Emergency Diagnostic & Priority Booking",
        "tool_sub": "Select your issue below for instant diagnostic guidelines and immediate service truck dispatch.",
        "services": [
            {
                "title": "24/7 Emergency Burst Pipe Repair",
                "desc": "Immediate main shutoff, thermal leak pinpointing, and surgical pipe repair to stop flooding in its tracks.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
            },
            {
                "title": "Tankless & Hybrid Water Heaters",
                "desc": "High-efficiency Rinnai and Navien installations engineered for endless hot water and coastal salt-air longevity.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>'
            },
            {
                "title": "Hydro-Jetting & Sewer Camera Audits",
                "desc": "4,000 PSI high-velocity line scouring and full HD optical camera inspections to eliminate tree root intrusions.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24"/><path d="m14.83 9.17 4.24-4.24"/><path d="m14.83 14.83 4.24 4.24"/><path d="m9.17 14.83-4.24 4.24"/></svg>'
            }
        ],
        "faqs": [
            {"q": "Do you charge extra for weekend or night emergency calls?", "a": "Blue Haven provides upfront, transparent flat rates before any work starts. No hidden surcharges or surprise billing."},
            {"q": "Can you install water heaters suited for coastal water quality?", "a": "Yes! We specialize in stainless steel and high-recovery anode rods formulated specifically to protect against coastal corrosion."},
            {"q": "What areas in Tillamook County do you cover?", "a": "We service Tillamook, Bay City, Garibaldi, Rockaway Beach, Pacific City, and surrounding coastal communities."}
        ]
    },
    {
        "id": "gurda-landscaping",
        "name": "Gurda Landscaping LLC",
        "short_name": "Gurda Landscaping",
        "mark": "GL",
        "trade": "Luxury Outdoor Living & Architectural Hardscaping",
        "category": "Landscaping & Hardscaping",
        "location": "Pine Island, NY",
        "service_area": "Pine Island, Warwick & Hudson Valley",
        "source": "Pine Island Chamber of Commerce",
        "phone": "(845) 683-1314",
        "email": "gurdalandscape@gmail.com",
        "theme": {
            "bg": "#070c09",
            "surface": "#0c1510",
            "surface_card": "#111f17",
            "border": "rgba(74, 222, 128, 0.14)",
            "border_accent": "rgba(74, 222, 128, 0.35)",
            "primary": "#4ade80",
            "primary_dim": "#86efac",
            "accent_grad": "linear-gradient(135deg, #4ade80 0%, #16a34a 50%, #15803d 100%)",
            "badge_bg": "rgba(74, 222, 128, 0.1)",
            "badge_text": "#4ade80",
            "hero_img": "https://images.unsplash.com/photo-1557429287-b2e26467fc2b?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1558904541-efa8c4a08931?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1592150621744-aca64f48394a?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Premier Hudson Valley Hardscape Artisans • Pine Island Black Dirt Specialists",
        "hero_title": "Architectural Outdoor Living & <span>Master Stone Craftsmanship.</span>",
        "hero_sub": "From custom Unilock stone patios and outdoor kitchens to comprehensive estate turf management, Gurda Landscaping elevates Warwick Valley properties.",
        "stats": [
            {"val": "15+", "label": "Years Cultivating Hudson Valley Properties"},
            {"val": "100%", "label": "Turnkey 3D Design to Final Build"},
            {"val": "Unilock", "label": "Authorized Contract Partner"},
            {"val": "$0", "label": "On-Site Design Consultation"}
        ],
        "tool_type": "calculator",
        "tool_title": "Outdoor Living Project Estimator",
        "tool_sub": "Select patio square footage and outdoor elements to view ballpark investment tiers.",
        "services": [
            {
                "title": "Custom Paver Patios & Walkways",
                "desc": "Laser-leveled aggregate bases, polymeric joint sand, and lifetime-guaranteed architectural paving stones.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg>'
            },
            {
                "title": "Natural Stone Retaining Walls & Steps",
                "desc": "Engineered structural boulder walls, bluestone coping, and integrated low-voltage LED landscape lighting.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><path d="m4.93 4.93 14.14 14.14"/><path d="m4.93 19.07 14.14-14.14"/></svg>'
            },
            {
                "title": "Estate Turf Care & Seasonal Cleanups",
                "desc": "Full-season mowing programs, deep core aeration, organic fertilization, and crisp spring/fall leaf clearing.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>'
            }
        ],
        "faqs": [
            {"q": "Do you provide 3D visual mockups before breaking ground?", "a": "Yes! Our design team creates photorealistic 3D renderings of your patio, fire pit, and plantings before any excavation begins."},
            {"q": "How do you guarantee patio pavers won't shift in winter freezes?", "a": "We excavate 8 to 10 inches below grade, install geotextile separation fabric, and pack dense crushed aggregate to withstand deep Hudson Valley frost heaves."},
            {"q": "What areas around Pine Island do you service?", "a": "We serve Pine Island, Warwick, Florida, Goshen, Chester, and surrounding Orange County towns."}
        ]
    },
    {
        "id": "red-cap-electrical",
        "name": "Red Cap Electrical Services LLC",
        "short_name": "Red Cap Electrical",
        "mark": "RC",
        "trade": "Industrial Power, 200A Panels & Smart EV Automation",
        "category": "Electrical Services",
        "location": "Dumas, TX",
        "service_area": "Dumas, Moore County & Panhandle",
        "source": "Dumas Area Chamber of Commerce",
        "phone": "(806) 935-4421",
        "email": "redcelectricservs@gmail.com",
        "theme": {
            "bg": "#0c0a09",
            "surface": "#17120e",
            "surface_card": "#211914",
            "border": "rgba(239, 68, 68, 0.18)",
            "border_accent": "rgba(239, 68, 68, 0.4)",
            "primary": "#ef4444",
            "primary_dim": "#f87171",
            "accent_grad": "linear-gradient(135deg, #ef4444 0%, #b91c1c 50%, #991b1b 100%)",
            "badge_bg": "rgba(239, 68, 68, 0.12)",
            "badge_text": "#fca5a5",
            "hero_img": "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Master Electrician License • Texas Panhandle Precision Wiring",
        "hero_title": "Heavy-Duty Electrical Engineering & <span>Zero-Fault Reliability.</span>",
        "hero_sub": "From 200-Amp main breaker service upgrades to high-speed Level-2 EV chargers and agricultural pump power, Red Cap delivers master-grade code compliance in Dumas.",
        "stats": [
            {"val": "100%", "label": "Texas Master Electrician Inspected"},
            {"val": "200A", "label": "Full Modern Breaker Modernization"},
            {"val": "Fast", "label": "Permit Pulling & Utility Coordination"},
            {"val": "1-Yr", "label": "Comprehensive Warranty on All Work"}
        ],
        "tool_type": "diagnostic",
        "tool_title": "Electrical Load & Safety Assessment",
        "tool_sub": "Identify symptoms of overloaded circuits and calculate panel replacement urgency.",
        "services": [
            {
                "title": "200A Breaker Panel Modernization",
                "desc": "Eliminate dangerous Zinsco/Federal Pacific fire hazards with Square D and Siemens surge-protected panels.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>'
            },
            {
                "title": "Level 2 EV Charging Station Circuits",
                "desc": "Dedicated 50A/240V lines for Tesla, Rivian, and Universal J1772 chargers with surge suppression.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/></svg>'
            },
            {
                "title": "Agricultural, Ranch & Generator Power",
                "desc": "Automatic transfer switches, irrigation pump wiring, and emergency backup power configurations.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
            }
        ],
        "faqs": [
            {"q": "How do I know if my electrical panel needs a 200A upgrade?", "a": "If your breakers trip when running your AC and dryer, or your panel is under 100A and lacks slots for EV chargers or hot tubs, an upgrade is recommended."},
            {"q": "Do you pull City of Dumas permits and coordinate with the electric utility?", "a": "Yes, we handle all city paperwork, permits, and power disconnect/reconnect coordination with the utility provider seamlessly."},
            {"q": "Do you handle farm and industrial 3-phase wiring?", "a": "Yes, Red Cap handles residential, commercial, and agricultural pump and grain elevator electrical systems."}
        ]
    },
    {
        "id": "four-families-roofing",
        "name": "Four Families Roofing LLC",
        "short_name": "Four Families Roofing",
        "mark": "4F",
        "trade": "High-Elevation Mountain Roofing & Standing Seam Metal",
        "category": "Roofing & Metal Roofs",
        "location": "Highlands, NC",
        "service_area": "Highlands, Cashiers & Western NC Mountains",
        "source": "Highlands Chamber of Commerce",
        "phone": "(828) 634-1664",
        "email": "letmeroofme@gmail.com",
        "theme": {
            "bg": "#080c0a",
            "surface": "#0f1713",
            "surface_card": "#16231c",
            "border": "rgba(52, 211, 153, 0.14)",
            "border_accent": "rgba(52, 211, 153, 0.35)",
            "primary": "#34d399",
            "primary_dim": "#6ee7b7",
            "accent_grad": "linear-gradient(135deg, #34d399 0%, #059669 50%, #047857 100%)",
            "badge_bg": "rgba(52, 211, 153, 0.1)",
            "badge_text": "#34d399",
            "hero_img": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1632759145351-1d592919f522?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1541888946425-d0fbb186c5f8?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Family-Owned Alpine Roofing • High-Elevation Ice & Heavy Snow Defense",
        "hero_title": "Mountain-Tested Roofs Engineered for <span>Highlands Elevations.</span>",
        "hero_sub": "From architectural standing seam steel to cedar shake conversions and chimney saddle leak prevention, Four Families Roofing protects Blue Ridge Mountain estates.",
        "stats": [
            {"val": "4,118'", "label": "Engineered for Highlands High Elevation"},
            {"val": "50-Yr", "label": "Standing Seam Metal Lifespan"},
            {"val": "100%", "label": "Family-Owned Mountain Pride"},
            {"val": "$0", "label": "Detailed Drone Roof Video Audit"}
        ],
        "tool_type": "calculator",
        "tool_title": "Highlands Metal & Shingle Estimator",
        "tool_sub": "Calculate investment ranges for heavy snow-load standing seam and impact architectural shingles.",
        "services": [
            {
                "title": "Standing Seam Metal Roofing",
                "desc": "Concealed fastener 24-gauge steel designed to shed heavy Appalachian snow loads and withstand mountain freeze cycles.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>'
            },
            {
                "title": "Chimney Flashing & Ice Dam Repair",
                "desc": "Custom fabricated copper crickets, ice and water shield membranes, and chimney counter-flashing reseals.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>'
            },
            {
                "title": "Architectural Shingle Installations",
                "desc": "Algae-resistant, heavy-laminated shingles designed to maintain vivid curb appeal in damp mountain climates.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
            }
        ],
        "faqs": [
            {"q": "Why is standing seam metal better for Highlands homes?", "a": "Highlands receives heavy snowfall and ice. Standing seam metal sheds snow naturally and prevents ice damming that destroys traditional shingles."},
            {"q": "Can you inspect hard-to-reach steep pitch mountain roofs?", "a": "Yes! We deploy high-resolution drone cameras to safely capture 4K footage of every valley, chimney, and ridge."},
            {"q": "Do you serve Cashiers and Lake Toxaway?", "a": "Yes, we serve Highlands, Cashiers, Scaly Mountain, and Lake Toxaway across Macon and Jackson counties."}
        ]
    },
    {
        "id": "aim-plumbing",
        "name": "AIM Plumbing Services",
        "short_name": "AIM Plumbing",
        "mark": "AP",
        "trade": "Residential Plumbing, Slab Leak Pinpointing & Water Heaters",
        "category": "Plumbing & Pipe Repair",
        "location": "Refugio County, TX",
        "service_area": "Refugio, Woodsboro & Coastal Bend",
        "source": "Refugio County Chamber of Commerce",
        "phone": "(361) 526-7890",
        "email": "aimplumbingservices@gmail.com",
        "theme": {
            "bg": "#080d16",
            "surface": "#0e1726",
            "surface_card": "#152238",
            "border": "rgba(14, 165, 233, 0.16)",
            "border_accent": "rgba(14, 165, 233, 0.38)",
            "primary": "#0ea5e9",
            "primary_dim": "#38bdf8",
            "accent_grad": "linear-gradient(135deg, #0ea5e9 0%, #0284c7 50%, #0369a1 100%)",
            "badge_bg": "rgba(14, 165, 233, 0.1)",
            "badge_text": "#38bdf8",
            "hero_img": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1585704032915-c3400ca199e7?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Reliable Coastal Bend Master Plumbers • Honest Local Rates",
        "hero_title": "Direct Honest Plumbing for <span>Refugio County Families.</span>",
        "hero_sub": "From slab leak acoustic detection to water heater replacements and sewer line video inspections, AIM Plumbing delivers fast, dependable local solutions.",
        "stats": [
            {"val": "100%", "label": "Family Owned in Refugio County"},
            {"val": "Fast", "label": "Same-Day Priority Dispatch"},
            {"val": "0%", "label": "No Hidden Travel or Trip Surcharges"},
            {"val": "100%", "label": "Fully Insured Master Plumber"}
        ],
        "tool_type": "diagnostic",
        "tool_title": "Plumbing Diagnostic & Direct Dispatch",
        "tool_sub": "Choose your plumbing concern to see recommended next steps and arrange a technician visit.",
        "services": [
            {
                "title": "Acoustic Under-Slab Leak Detection",
                "desc": "Pinpoint hot spots and hidden line fractures beneath concrete foundations without tearing up flooring.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24"/><path d="m14.83 9.17 4.24-4.24"/></svg>'
            },
            {
                "title": "Water Heater Repair & Replacement",
                "desc": "Energy-efficient traditional gas and electric tank units, along with tankless upgrades for endless supply.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>'
            },
            {
                "title": "Sewer Line Cleaning & Root Removal",
                "desc": "Heavy-duty drain cabling, optical video line inspections, and durable cleanout installations.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
            }
        ],
        "faqs": [
            {"q": "What are the warning signs of a slab leak?", "a": "Warm spots on your floor tiles, unexplained spikes in your water bill, low water pressure, or the sound of rushing water when taps are turned off."},
            {"q": "Do you repair both gas and electric water heaters?", "a": "Yes! We stock replacement elements, thermostats, gas valves, and complete new units on our trucks."},
            {"q": "Do you service Woodsboro and Bayside?", "a": "Yes, we proudly serve all of Refugio, Woodsboro, Bayside, Austwell, and Tivoli."}
        ]
    },
    {
        "id": "ave-electric",
        "name": "AVE. Electric LLC",
        "short_name": "AVE. Electric",
        "mark": "AE",
        "trade": "Commercial LED Lighting, Power Distribution & Smart Automation",
        "category": "Licensed Electrical Contractor",
        "location": "Pomona, CA",
        "service_area": "Pomona, Inland Empire & San Gabriel Valley",
        "source": "Pomona Chamber of Commerce",
        "phone": "(909) 620-1940",
        "email": "ave.3lectric@gmail.com",
        "theme": {
            "bg": "#0a0a14",
            "surface": "#121226",
            "surface_card": "#1a1a36",
            "border": "rgba(139, 92, 246, 0.18)",
            "border_accent": "rgba(139, 92, 246, 0.4)",
            "primary": "#a78bfa",
            "primary_dim": "#c4b5fd",
            "accent_grad": "linear-gradient(135deg, #a78bfa 0%, #7c3aed 50%, #6d28d9 100%)",
            "badge_bg": "rgba(139, 92, 246, 0.12)",
            "badge_text": "#c4b5fd",
            "hero_img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ California C-10 Electrical Contractor • Title 24 Compliance Specialists",
        "hero_title": "Modern Commercial Power & <span>Architectural Lighting Design.</span>",
        "hero_sub": "From retail LED retrofits and warehouse high-bay power to residential panel replacements, AVE. Electric delivers precision engineering across the San Gabriel Valley.",
        "stats": [
            {"val": "C-10", "label": "Licensed California Electrical Contractor"},
            {"val": "Title 24", "label": "Full Energy Compliance Certification"},
            {"val": "100%", "label": "Commercial & Residential Coverage"},
            {"val": "5-Yr", "label": "Workmanship Warranty On Installations"}
        ],
        "tool_type": "calculator",
        "tool_title": "Commercial Lighting & Power Calculator",
        "tool_sub": "Estimate energy cost savings and project scope for commercial LED retrofits and sub-panel installations.",
        "services": [
            {
                "title": "Commercial High-Bay LED Retrofits",
                "desc": "Drop operational utility overhead by up to 65% with DLC-certified smart sensor industrial lighting.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>'
            },
            {
                "title": "Power Distribution & Dedicated Circuits",
                "desc": "Step-down transformers, 3-phase machinery hookups, and isolated ground circuits for sensitive electronics.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/></svg>'
            },
            {
                "title": "Smart Building Automation & Controls",
                "desc": "Lutron and Leviton automated dimming, occupancy sensors, and remote power management systems.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
            }
        ],
        "faqs": [
            {"q": "Do you handle Title 24 acceptance testing and certification?", "a": "Yes! Our technicians ensure all lighting and automatic shutoff controls comply with California Title 24 standards."},
            {"q": "Can you handle emergency commercial power outages?", "a": "Yes, we prioritize commercial clients with critical machinery, server rooms, or retail display downtime."},
            {"q": "What cities do you serve?", "a": "We cover Pomona, Ontario, Chino, Claremont, Montclair, and surrounding Inland Empire areas."}
        ]
    },
    {
        "id": "elite-roofing",
        "name": "Elite Roofing",
        "short_name": "Elite Roofing",
        "mark": "ER",
        "trade": "Desert Heat-Reflective Roofing & Spanish Tile Restoration",
        "category": "Roofing & Desert Coatings",
        "location": "Yucca Valley, CA",
        "service_area": "Yucca Valley, Joshua Tree & Morongo Basin",
        "source": "Yucca Valley Chamber of Commerce",
        "phone": "(760) 449-6835",
        "email": "phil.eliteroofing@gmail.com",
        "theme": {
            "bg": "#0c0a08",
            "surface": "#18140f",
            "surface_card": "#241e16",
            "border": "rgba(251, 146, 60, 0.16)",
            "border_accent": "rgba(251, 146, 60, 0.38)",
            "primary": "#fb923c",
            "primary_dim": "#fdba74",
            "accent_grad": "linear-gradient(135deg, #fb923c 0%, #ea580c 50%, #c2410c 100%)",
            "badge_bg": "rgba(251, 146, 60, 0.1)",
            "badge_text": "#fed7aa",
            "hero_img": "https://images.unsplash.com/photo-1541888946425-d0fbb186c5f8?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1632759145351-1d592919f522?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1541888946425-d0fbb186c5f8?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ High Desert UV Thermal Defense • Cool Roof Certified",
        "hero_title": "Thermal-Reflective Roofing Engineered for <span>High Desert Extremes.</span>",
        "hero_sub": "From elastomeric silicone cool roof coatings that slash AC electric bills to Spanish concrete tile resets, Elite Roofing shields Yucca Valley and Joshua Tree homes.",
        "stats": [
            {"val": "-25°F", "label": "Drop in Rooftop Surface Heat"},
            {"val": "100%", "label": "Cool Roof Title 24 Compliant"},
            {"val": "50-Yr", "label": "Tile & Underlayment Durability"},
            {"val": "$0", "label": "Free On-Site Drone Roof Audit"}
        ],
        "tool_type": "calculator",
        "tool_title": "Desert Thermal Cool-Roof Estimator",
        "tool_sub": "Estimate square footage cost and electric bill savings for silicone white elastomeric coatings.",
        "services": [
            {
                "title": "Elastomeric Silicone Cool Roof Coatings",
                "desc": "Seamless 95% UV reflective monolithic waterproof barrier that drops indoor temperatures dramatically in summer.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><path d="m4.93 4.93 14.14 14.14"/><path d="m4.93 19.07 14.14-14.14"/></svg>'
            },
            {
                "title": "Spanish Tile Lift & Relay Services",
                "desc": "Preserve existing historic clay and concrete tiles while installing premium high-temp ice & water synthetic underlayments.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>'
            },
            {
                "title": "Wind-Resistant Asphalt Shingle Upgrades",
                "desc": "Extra-strength nailing and Class 4 impact shingles engineered for ferocious Morongo Basin windstorms.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
            }
        ],
        "faqs": [
            {"q": "How does a silicone cool roof coating save on electric bills in the desert?", "a": "Standard roofs absorb over 150°F of radiant heat, forcing your AC to run nonstop. A reflective coating bounces 90%+ of that solar radiation away, keeping your attic cool."},
            {"q": "Do you repair Airbnb and short-term rental roofs quickly?", "a": "Yes! We work with Joshua Tree vacation rental owners to execute fast repairs without disrupting guest bookings."},
            {"q": "What areas in the Morongo Basin do you cover?", "a": "We service Yucca Valley, Joshua Tree, Twentynine Palms, Landers, and Pioneertown."}
        ]
    },
    {
        "id": "doctor-electrical",
        "name": "Doctor Electrical Services Inc.",
        "short_name": "Doctor Electrical",
        "mark": "DE",
        "trade": "Island Coastal Power, Marine Docks & Backup Generators",
        "category": "Electrical Inspections & Repairs",
        "location": "Camano Island, WA",
        "service_area": "Camano Island, Stanwood & Puget Sound",
        "source": "Camano Island Chamber of Commerce",
        "phone": "(360) 387-9912",
        "email": "doctorelectricalservices@gmail.com",
        "theme": {
            "bg": "#060c12",
            "surface": "#0c1722",
            "surface_card": "#132334",
            "border": "rgba(20, 184, 166, 0.16)",
            "border_accent": "rgba(20, 184, 166, 0.38)",
            "primary": "#14b8a6",
            "primary_dim": "#5eead4",
            "accent_grad": "linear-gradient(135deg, #14b8a6 0%, #0d9488 50%, #0f766e 100%)",
            "badge_bg": "rgba(20, 184, 166, 0.1)",
            "badge_text": "#5eead4",
            "hero_img": "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Licensed Island Electrical Specialists • Salt-Air Corrosion Defense",
        "hero_title": "Coastal Island Electrical & <span>Emergency Generator Reliability.</span>",
        "hero_sub": "From automatic standby generator transfer switches during winter storms to marine dock shore power and complete panel diagnostics, Doctor Electrical keeps Camano Island energized.",
        "stats": [
            {"val": "100%", "label": "Local Camano Island Technicians"},
            {"val": "< 10s", "label": "Automatic Generator Switchover Time"},
            {"val": "IP66", "label": "Salt-Air Corrosion Sealed Enclosures"},
            {"val": "$0", "label": "Comprehensive Safety Electrical Audit"}
        ],
        "tool_type": "diagnostic",
        "tool_title": "Island Power & Generator Diagnostic",
        "tool_sub": "Calculate your home's kilowatt requirements during severe Puget Sound winter power outages.",
        "services": [
            {
                "title": "Whole-Home Standby Generator Systems",
                "desc": "Kohler and Generac automatic transfer systems that power your heat pump, well pump, and fridge the second island power drops.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>'
            },
            {
                "title": "Marine Shore Power & Boat Lift Wiring",
                "desc": "Marine-grade stainless pedestals, GFCI dock wiring, and submersible conduit built to withstand corrosive saltwater tides.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
            },
            {
                "title": "Coastal Weatherproof Panel Upgrades",
                "desc": "NEMA 3R/4X rated outdoor breaker enclosures with heavy-duty surge protection against coastal lightning strikes.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/></svg>'
            }
        ],
        "faqs": [
            {"q": "Can you wire my generator to power both my house and well pump?", "a": "Yes! Well pumps require high startup surge amps, so we configure automatic priority load shedding to ensure your water and heat run reliably."},
            {"q": "How do you protect island electrical panels from rust?", "a": "We install marine-grade stainless hardware, silicone conformal gaskets, and antioxidant terminal coatings tailored for salt spray."},
            {"q": "Do you travel across both North and South Camano Island?", "a": "Yes, we are stationed directly on the island and provide fast local service without ferry delays."}
        ]
    },
    {
        "id": "nuco-electric",
        "name": "NuCo Electric",
        "short_name": "NuCo Electric",
        "mark": "NC",
        "trade": "Residential Remodel Wiring, Smart Home & EV Charging",
        "category": "Residential & Commercial Electric",
        "location": "Oswego, IL",
        "service_area": "Oswego, Naperville & Fox Valley",
        "source": "Oswego Area Chamber of Commerce",
        "phone": "(630) 554-7100",
        "email": "nucoelectric@gmail.com",
        "theme": {
            "bg": "#0a0a0c",
            "surface": "#141418",
            "surface_card": "#1e1e24",
            "border": "rgba(234, 179, 8, 0.16)",
            "border_accent": "rgba(234, 179, 8, 0.38)",
            "primary": "#eab308",
            "primary_dim": "#fde047",
            "accent_grad": "linear-gradient(135deg, #eab308 0%, #ca8a04 50%, #a16207 100%)",
            "badge_bg": "rgba(234, 179, 8, 0.1)",
            "badge_text": "#fef08a",
            "hero_img": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Fox Valley Certified Electricians • Oswego Home Remodel Specialists",
        "hero_title": "Smart Residential Electrical & <span>Basement Remodel Power.</span>",
        "hero_sub": "From finished basement recessed lighting and theater wiring to 240V Tesla/EV garage chargers and modern subpanels, NuCo Electric powers Oswego homes.",
        "stats": [
            {"val": "100%", "label": "Chicagoland Code Conduit Compliance"},
            {"val": "240V", "label": "Fast Overnight EV Charger Setup"},
            {"val": "Clean", "label": "Zero Drywall Mess Guarantee"},
            {"val": "$0", "label": "In-Home Remodel Estimate"}
        ],
        "tool_type": "calculator",
        "tool_title": "Basement & EV Project Estimator",
        "tool_sub": "Calculate approximate wiring costs for can lights, sub-panels, and Level 2 EV charging lines.",
        "services": [
            {
                "title": "Finished Basement Electrical Buildouts",
                "desc": "Dedicated circuits for home theaters, wet bars, sauna heaters, and ultra-quiet canless LED fixtures.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>'
            },
            {
                "title": "Level-2 Electric Vehicle Charging",
                "desc": "Clean EMT conduit runs to your garage with heavy-duty 50-amp breakers for Tesla Wall Connectors and ChargePoint stations.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/></svg>'
            },
            {
                "title": "Smart Home Lighting & Panel Surges",
                "desc": "Whole-home surge protection to protect $20,000+ in electronics, plus Lutron Caseta smart dimmers.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
            }
        ],
        "faqs": [
            {"q": "Do you install electrical using metallic conduit as required by Illinois code?", "a": "Yes! We specialize in clean, precise EMT conduit bending adhering strictly to the Chicagoland/Illinois electrical code."},
            {"q": "Can my existing electrical panel handle an EV charger?", "a": "We run an instant load calculation. If you have a 100A panel that is maxed out, we can install a modern 200A upgrade or smart energy management switch."},
            {"q": "What areas do you service?", "a": "We service Oswego, Montgomery, Yorkville, Aurora, Plainfield, and Naperville."}
        ]
    },
    {
        "id": "apm-painting",
        "name": "APM Painting & Design",
        "short_name": "APM Painting",
        "mark": "AP",
        "trade": "Luxury Interior/Exterior Painting & Fine Cabinet Spraying",
        "category": "Painting & Design",
        "location": "Bethel, CT",
        "service_area": "Bethel, Danbury & Fairfield County",
        "source": "Bethel Chamber of Commerce",
        "phone": "(203) 791-8844",
        "email": "apmpainting25@gmail.com",
        "theme": {
            "bg": "#0c0b0a",
            "surface": "#161311",
            "surface_card": "#211c18",
            "border": "rgba(244, 63, 94, 0.16)",
            "border_accent": "rgba(244, 63, 94, 0.38)",
            "primary": "#fb7185",
            "primary_dim": "#fda4af",
            "accent_grad": "linear-gradient(135deg, #fb7185 0%, #e11d48 50%, #be123c 100%)",
            "badge_bg": "rgba(244, 63, 94, 0.1)",
            "badge_text": "#fecdd3",
            "hero_img": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1562259949-e8e7689d7828?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Fairfield County Premier Finish Artisans • Dustless Sanding Technology",
        "hero_title": "Flawless Architectural Painting & <span>Factory-Finish Cabinets.</span>",
        "hero_sub": "From high-end interior millwork and Benjamin Moore color consultations to complete exterior weatherproofing, APM Painting transforms fine Fairfield County residences.",
        "stats": [
            {"val": "100%", "label": "HEPA Dustless Sanding Systems"},
            {"val": "Factory", "label": "Mirror-Smooth Cabinet Spray Finishes"},
            {"val": "Zero", "label": "Paint Splatter & Drip Guarantee"},
            {"val": "$0", "label": "In-Home Color Consultation"}
        ],
        "tool_type": "calculator",
        "tool_title": "Interior Painting & Cabinet Cost Estimator",
        "tool_sub": "Estimate room counts, square footage, and cabinet door refinishing investment.",
        "services": [
            {
                "title": "Kitchen Cabinet Spray Refinishing",
                "desc": "Off-site spray booth industrial conversion varnish finishes that give 20-year-old oak cabinets a showroom new look.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg>'
            },
            {
                "title": "Interior Walls, Trim & Coffered Ceilings",
                "desc": "Surgical masking, Level-5 drywall smoothing, and ultra-crisp cut lines using Benjamin Moore Aura paints.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="m14 12-8.5 8.5a2.12 2.12 0 1 1-3-3L11 9"/><path d="M18 16l4-4-7.5-7.5-4 4"/></svg>'
            },
            {
                "title": "Exterior Siding & Historic Trim Protection",
                "desc": "Gentle soft-washing, rotary scraped bare wood priming, and elastomeric sealants built for New England freeze cycles.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
            }
        ],
        "faqs": [
            {"q": "How do you eliminate fine dust when sanding inside our home?", "a": "We use Festool HEPA-certified dust extraction sanders connected directly to each tool, capturing 99.9% of all airborne particles."},
            {"q": "Will cabinet spray paint chip over time?", "a": "No. We apply industrial-grade Italian polyurethane wood coatings that cure into an ultra-hard, wipeable surface that resists grease and steam."},
            {"q": "What areas in Fairfield County do you cover?", "a": "We service Bethel, Danbury, Newtown, Ridgefield, Brookfield, and Redding."}
        ]
    },
    {
        "id": "wake-forest-hvac",
        "name": "Wake Forest HVAC Company",
        "short_name": "Wake Forest HVAC",
        "mark": "WF",
        "trade": "High-Efficiency Heat Pumps, AC Repairs & Air Quality",
        "category": "Heating, AC & Heat Pumps",
        "location": "Rolesville & Wake Forest, NC",
        "service_area": "Wake Forest, Rolesville & Greater Raleigh",
        "source": "Rolesville Chamber of Commerce",
        "phone": "(919) 556-9180",
        "email": "wafohvac@gmail.com",
        "theme": {
            "bg": "#070c14",
            "surface": "#0d1726",
            "surface_card": "#132138",
            "border": "rgba(14, 165, 233, 0.16)",
            "border_accent": "rgba(14, 165, 233, 0.38)",
            "primary": "#38bdf8",
            "primary_dim": "#7dd3fc",
            "accent_grad": "linear-gradient(135deg, #38bdf8 0%, #0284c7 50%, #0369a1 100%)",
            "badge_bg": "rgba(14, 165, 233, 0.1)",
            "badge_text": "#38bdf8",
            "hero_img": "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Carolina Climate Specialists • 24/7 Same-Day AC & Heat Repair",
        "hero_title": "Precision Home Climate & <span>High-Efficiency Heat Pumps.</span>",
        "hero_sub": "From middle-of-summer AC compressor failures to 18+ SEER2 variable-speed heat pump installations, Wake Forest HVAC guarantees Carolina comfort.",
        "stats": [
            {"val": "24/7", "label": "Emergency No-Cool Dispatch"},
            {"val": "18+", "label": "SEER2 Ultra-Efficiency Heat Pumps"},
            {"val": "$0", "label": "Free Second Opinion on System Replacements"},
            {"val": "10-Yr", "label": "Parts & Compressor Warranty"}
        ],
        "tool_type": "diagnostic",
        "tool_title": "AC & Heating System Diagnostic",
        "tool_sub": "Troubleshoot common symptoms like frozen coils, lukewarm air, or constant short cycling.",
        "services": [
            {
                "title": "High-Efficiency Inverter Heat Pumps",
                "desc": "Cut electricity costs up to 40% with variable-capacity Trane and Bosch inverter heat pump systems.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="4"/></svg>'
            },
            {
                "title": "24/7 Emergency AC Diagnostic & Repair",
                "desc": "Stocked service vans with capacitors, fan motors, contactors, and eco-friendly R-454B/R-410A refrigerants.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
            },
            {
                "title": "Whole-Home Dehumidifiers & Air Filtration",
                "desc": "Eliminate sticky southern humidity and allergens with Aprilaire whole-home central dehumidification.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
            }
        ],
        "faqs": [
            {"q": "Why is my AC running but blowing room-temperature air?", "a": "This usually indicates a failed capacitor, a refrigerant leak, or a dirty outside condenser coil. We offer prompt same-day diagnostics."},
            {"q": "Are there Duke Energy rebates for upgrading to high-efficiency heat pumps?", "a": "Yes! Duke Energy offers rebates up to $600–$1,200 on qualified heat pump systems, and we process the paperwork for you."},
            {"q": "What areas do you serve?", "a": "We service Wake Forest, Rolesville, Youngsville, Knightdale, and North Raleigh."}
        ]
    },
    {
        "id": "big-ts-painting",
        "name": "Big T's Painting & Construction",
        "short_name": "Big T's Painting",
        "mark": "BT",
        "trade": "Rural Barn Restoration, Exterior Siding & Timber Deck Staining",
        "category": "Painting & Construction",
        "location": "Spring Grove, MN",
        "service_area": "Spring Grove, Houston County & Driftless Region",
        "source": "Spring Grove Chamber of Commerce",
        "phone": "(507) 498-5520",
        "email": "ladsten1@gmail.com",
        "theme": {
            "bg": "#0c0908",
            "surface": "#181210",
            "surface_card": "#241a17",
            "border": "rgba(249, 115, 22, 0.16)",
            "border_accent": "rgba(249, 115, 22, 0.38)",
            "primary": "#f97316",
            "primary_dim": "#fb923c",
            "accent_grad": "linear-gradient(135deg, #f97316 0%, #ea580c 50%, #c2410c 100%)",
            "badge_bg": "rgba(249, 115, 22, 0.1)",
            "badge_text": "#fed7aa",
            "hero_img": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=2000&q=80",
            "card_imgs": [
                "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1558904541-efa8c4a08931?auto=format&fit=crop&w=600&q=80",
                "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=600&q=80"
            ]
        },
        "badge_text": "✦ Driftless Area Rural Specialists • Heavy-Duty Weather-Proof Coatings",
        "hero_title": "Heavy-Duty Exterior Painting & <span>Barn Restoration Craft.</span>",
        "hero_sub": "From agricultural pole barn spray painting and historic cedar siding restoration to deck re-staining, Big T's protects Minnesota properties against punishing winters.",
        "stats": [
            {"val": "100%", "label": "Minnesota Winter Weather Shield"},
            {"val": "High-PSI", "label": "Deep Wash & Millwork Prep"},
            {"val": "Heavy", "label": "Commercial-Grade Exterior Coatings"},
            {"val": "$0", "label": "On-Site Farm & Home Estimate"}
        ],
        "tool_type": "calculator",
        "tool_title": "Barn & Exterior Siding Calculator",
        "tool_sub": "Estimate square footage coating costs for agricultural pole barns, machine sheds, and residential decks.",
        "services": [
            {
                "title": "Agricultural Barn & Metal Building Spraying",
                "desc": "Heavy-build direct-to-metal acrylic enamels that seal rusted corrugated roofs and protect wooden grain silos.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>'
            },
            {
                "title": "Exterior Home Siding & Fascia Painting",
                "desc": "Thorough scraping, exterior caulking, and mold-resistant paints engineered to endure -25°F Minnesota snow.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="m14 12-8.5 8.5a2.12 2.12 0 1 1-3-3L11 9"/><path d="M18 16l4-4-7.5-7.5-4 4"/></svg>'
            },
            {
                "title": "Cedar Deck & Fence Deep Staining",
                "desc": "High-pressure wash, natural wood brightening, and deep penetrating UV oil stains that prevent wood warping and decay.",
                "svg": '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
            }
        ],
        "faqs": [
            {"q": "Can you paint rusted tin roofs on barns and sheds?", "a": "Yes! We prep the metal with rust-converting primers before airless spraying heavy-duty commercial acrylic coatings."},
            {"q": "What paint brands do you use for exterior Minnesota homes?", "a": "We use premium Sherwin-Williams SuperPaint and Duration coatings specifically formulated for high freeze-thaw cycles."},
            {"q": "What areas in Houston County do you serve?", "a": "We serve Spring Grove, Caledonia, Houston, Mabel, and surrounding Driftless farms."}
        ]
    }
]

def generate_html(b):
    theme = b["theme"]
    
    # tool html
    if b["tool_type"] == "calculator":
        tool_html = f"""
        <!-- Interactive Investment Estimator -->
        <div class="calculator-outer" id="calculator">
          <div class="calc-card">
            <div class="calc-tag">{b["tool_title"]}</div>
            <h2>Transparent Ballpark Estimator</h2>
            <p class="sub">{b["tool_sub"]}</p>

            <div class="slider-container">
              <div class="slider-labels">
                <span>Estimated Project Size:</span>
                <span id="sqftLabel">2,400 sq. ft.</span>
              </div>
              <input type="range" id="sqftSlider" min="1000" max="5000" step="100" value="2400" oninput="updateCost()">
            </div>

            <div class="calc-result-box">
              <div class="label">Estimated Investment Range:</div>
              <div class="val" id="priceDisplay">$4,800 – $6,500</div>
            </div>
          </div>
        </div>
        """
    else:
        tool_html = f"""
        <!-- Interactive Diagnostic Selector -->
        <div class="calculator-outer" id="calculator">
          <div class="calc-card">
            <div class="calc-tag">{b["tool_title"]}</div>
            <h2>Immediate Diagnostic Selector</h2>
            <p class="sub">{b["tool_sub"]}</p>

            <div class="diag-tabs">
              <button class="diag-tab active" onclick="setDiag(0)">{b['services'][0]['title'].split()[0]} Issue</button>
              <button class="diag-tab" onclick="setDiag(1)">{b['services'][1]['title'].split()[0]} Issue</button>
              <button class="diag-tab" onclick="setDiag(2)">{b['services'][2]['title'].split()[0]} Issue</button>
            </div>

            <div class="calc-result-box" id="diagOutput">
              <div class="label">Diagnostic Status: Priority Dispatch Available</div>
              <div class="val" id="diagText">Immediate response truck equipped with testing gear ready in {b['location']}.</div>
            </div>
          </div>
        </div>
        """

    # services html
    services_cards = ""
    for idx, s in enumerate(b["services"]):
        card_img = theme["card_imgs"][idx % len(theme["card_imgs"])]
        services_cards += f"""
        <div class="service-card" style="--bg-job: url('{card_img}');">
          <div class="card-icon">
            {s['svg']}
          </div>
          <h3>{s['title']}</h3>
          <p>{s['desc']}</p>
          <a href="#quote" class="card-link">Request Service Option →</a>
        </div>
        """

    # stats html
    stats_chips = ""
    for st in b["stats"]:
        stats_chips += f"""
        <div class="stat-chip">
          <div class="stat-num">{st['val']}</div>
          <div class="stat-desc">{st['label']}</div>
        </div>
        """

    # faq html
    faq_items = ""
    for f in b["faqs"]:
        faq_items += f"""
        <div class="faq-item">
          <div class="faq-question" onclick="toggleFaq(this)">
            <span>{f['q']}</span>
            <span style="font-size: 18px; color: {theme['primary']};">+</span>
          </div>
          <div class="faq-answer">
            {f['a']}
          </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{b['name']} | {b['trade']}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Syne:wght@700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: {theme['bg']};
      --surface: {theme['surface']};
      --surface-card: {theme['surface_card']};
      --surface-hover: rgba(255,255,255,0.04);
      --border: {theme['border']};
      --border-accent: {theme['border_accent']};
      --primary: {theme['primary']};
      --primary-dim: {theme['primary_dim']};
      --accent-grad: {theme['accent_grad']};
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --radius: 14px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background-color: var(--bg); color: var(--text); line-height: 1.6; overflow-x: hidden; }}
    h1, h2, h3, h4, .display-font {{ font-family: 'Syne', sans-serif; letter-spacing: -0.03em; }}

    /* Top Live Status Bar */
    .status-bar {{
      background: rgba(9, 11, 14, 0.9);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 10px 24px;
      font-size: 13px;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .status-pulse {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: var(--primary);
      font-weight: 600;
    }}
    .pulse-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--primary);
      box-shadow: 0 0 10px var(--primary);
      animation: pulse 2s infinite;
    }}
    @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.35; }} 100% {{ opacity: 1; }} }}

    /* Floating Navigation */
    .nav-container {{
      position: sticky;
      top: 16px;
      z-index: 100;
      padding: 0 24px;
      max-width: 1320px;
      margin: 0 auto;
    }}
    nav {{
      background: rgba(16, 20, 27, 0.85);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border-accent);
      border-radius: 100px;
      padding: 12px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1);
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
    }}
    .brand-mark {{
      width: 38px;
      height: 38px;
      background: var(--accent-grad);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #090b0e;
      font-weight: 900;
      font-size: 16px;
      box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
    }}
    .brand-name {{
      color: var(--text);
      font-size: 15.5px;
      font-weight: 700;
      letter-spacing: -0.02em;
    }}
    .brand-name span {{ color: var(--primary-dim); }}
    .nav-links {{
      display: flex;
      gap: 28px;
      list-style: none;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 14px;
      font-weight: 500;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}
    
    .btn-nav {{
      background: var(--accent-grad);
      color: #090b0e;
      padding: 10px 22px;
      border-radius: 100px;
      font-size: 13.5px;
      font-weight: 800;
      text-decoration: none;
      transition: all 0.2s;
      border: 1px solid rgba(255,255,255,0.4);
      box-shadow: 0 0 15px rgba(255,255,255,0.15);
    }}
    .btn-nav:hover {{
      transform: translateY(-1px);
      box-shadow: 0 0 25px rgba(255,255,255,0.3);
    }}

    /* Hero Section with Faded Job Background */
    .hero-outer {{
      position: relative;
      background: 
        linear-gradient(180deg, rgba(9, 11, 14, 0.88) 0%, rgba(9, 11, 14, 0.95) 100%),
        url('{theme["hero_img"]}') center/cover no-repeat;
      border-bottom: 1px solid var(--border);
    }}
    .hero {{
      padding: 90px 24px 90px;
      max-width: 1320px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 60px;
      align-items: center;
      position: relative;
      z-index: 2;
    }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: {theme["badge_bg"]};
      border: 1px solid var(--border-accent);
      padding: 6px 16px;
      border-radius: 100px;
      font-size: 13px;
      color: {theme["badge_text"]};
      font-weight: 600;
      margin-bottom: 24px;
      backdrop-filter: blur(8px);
    }}
    .hero h1 {{
      font-size: 52px;
      line-height: 1.1;
      margin-bottom: 24px;
      color: #ffffff;
    }}
    .hero h1 span {{
      background: var(--accent-grad);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero-lead {{
      font-size: 17.5px;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 36px;
      max-width: 560px;
    }}
    .hero-cta-group {{
      display: flex;
      gap: 16px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .btn-hero-primary {{
      background: var(--accent-grad);
      color: #090b0e;
      padding: 16px 32px;
      border-radius: 12px;
      font-size: 15px;
      font-weight: 800;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      border: 1px solid rgba(255,255,255,0.4);
      box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }}
    .btn-hero-primary:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 35px rgba(255,255,255,0.25);
    }}
    .btn-hero-secondary {{
      background: var(--surface-card);
      border: 1px solid var(--border-accent);
      color: var(--primary);
      padding: 16px 28px;
      border-radius: 12px;
      font-size: 15px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .btn-hero-secondary:hover {{
      background: var(--surface-hover);
      border-color: rgba(255,255,255,0.4);
    }}

    /* Quote Card */
    .quote-card {{
      background: rgba(16, 20, 27, 0.92);
      backdrop-filter: blur(20px);
      border: 1px solid var(--border-accent);
      border-radius: 24px;
      padding: 36px;
      box-shadow: 0 30px 60px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.12);
      position: relative;
    }}
    .quote-card::before {{
      content: '';
      position: absolute;
      top: -1px;
      left: 20%;
      right: 20%;
      height: 2px;
      background: var(--accent-grad);
    }}
    .quote-card h3 {{
      font-size: 22px;
      margin-bottom: 8px;
      color: #ffffff;
    }}
    .quote-card p {{
      color: var(--text-muted);
      font-size: 14px;
      margin-bottom: 24px;
    }}
    .input-box {{
      margin-bottom: 16px;
    }}
    .input-box label {{
      display: block;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--primary-dim);
      margin-bottom: 6px;
    }}
    .input-box input, .input-box select {{
      width: 100%;
      background: #090b0e;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 13px 16px;
      color: white;
      font-size: 14px;
      transition: border-color 0.2s;
    }}
    .input-box input:focus, .input-box select:focus {{
      outline: none;
      border-color: var(--primary);
      box-shadow: 0 0 15px rgba(255,255,255,0.1);
    }}
    .btn-submit-card {{
      width: 100%;
      background: var(--accent-grad);
      color: #090b0e;
      border: 1px solid rgba(255,255,255,0.4);
      padding: 15px;
      border-radius: 10px;
      font-size: 15px;
      font-weight: 800;
      cursor: pointer;
      margin-top: 8px;
      transition: all 0.2s;
    }}
    .btn-submit-card:hover {{
      transform: translateY(-2px);
    }}

    /* Trust Strip */
    .trust-strip {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 30px 24px;
    }}
    .trust-wrap {{
      max-width: 1320px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
    }}
    .stat-chip {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      border-left: 2px solid var(--primary);
    }}
    .stat-num {{
      font-family: 'Syne', sans-serif;
      font-size: 28px;
      font-weight: 800;
      color: var(--primary);
      white-space: nowrap;
    }}
    .stat-desc {{
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.4;
    }}

    /* Section Structure */
    .section-wrap {{
      padding: 90px 24px;
      max-width: 1320px;
      margin: 0 auto;
    }}
    .section-head {{
      text-align: center;
      max-width: 700px;
      margin: 0 auto 50px;
    }}
    .section-head h2 {{
      font-size: 38px;
      color: white;
      margin-bottom: 14px;
    }}
    .section-head p {{
      color: var(--text-muted);
      font-size: 16px;
    }}

    /* Grid 3 */
    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;
    }}
    .service-card {{
      position: relative;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 36px 30px;
      overflow: hidden;
      transition: all 0.3s;
      z-index: 1;
    }}
    .service-card::before {{
      content: '';
      position: absolute;
      inset: 0;
      background-image: var(--bg-job);
      background-size: cover;
      background-position: center;
      opacity: 0.12;
      filter: grayscale(80%);
      transition: opacity 0.3s, transform 0.5s;
      z-index: -1;
    }}
    .service-card:hover {{
      transform: translateY(-6px);
      border-color: var(--border-accent);
      box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }}
    .service-card:hover::before {{
      opacity: 0.22;
      transform: scale(1.05);
    }}
    .card-icon {{
      width: 56px;
      height: 56px;
      border-radius: 14px;
      background: var(--surface-card);
      border: 1px solid var(--border-accent);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--primary);
      margin-bottom: 24px;
    }}
    .service-card h3 {{
      font-size: 20px;
      color: white;
      margin-bottom: 12px;
    }}
    .service-card p {{
      color: var(--text-muted);
      font-size: 14.5px;
      line-height: 1.6;
      margin-bottom: 24px;
    }}
    .card-link {{
      color: var(--primary);
      font-weight: 700;
      font-size: 14px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: gap 0.2s;
    }}
    .card-link:hover {{ gap: 10px; color: #ffffff; }}

    /* Calculator & Diagnostic Component */
    .calculator-outer {{
      padding: 60px 24px;
      max-width: 1100px;
      margin: 0 auto;
    }}
    .calc-card {{
      background: linear-gradient(180deg, var(--surface) 0%, #080b0f 100%);
      border: 1px solid var(--border-accent);
      border-radius: 24px;
      padding: 50px 40px;
      text-align: center;
      box-shadow: 0 30px 60px rgba(0,0,0,0.4);
    }}
    .calc-tag {{
      display: inline-block;
      padding: 5px 14px;
      border-radius: 100px;
      background: {theme["badge_bg"]};
      border: 1px solid var(--border-accent);
      color: var(--primary);
      font-size: 12.5px;
      font-weight: 700;
      margin-bottom: 16px;
    }}
    .calc-card h2 {{
      font-size: 32px;
      color: white;
      margin-bottom: 12px;
    }}
    .calc-card .sub {{
      color: var(--text-muted);
      font-size: 15px;
      max-width: 650px;
      margin: 0 auto 36px;
    }}
    .slider-container {{
      max-width: 600px;
      margin: 0 auto 30px;
      text-align: left;
    }}
    .slider-labels {{
      display: flex;
      justify-content: space-between;
      color: var(--primary-dim);
      font-weight: 700;
      font-size: 15px;
      margin-bottom: 10px;
    }}
    input[type=range] {{
      width: 100%;
      height: 8px;
      border-radius: 5px;
      background: #1c2430;
      outline: none;
      accent-color: var(--primary);
      cursor: pointer;
    }}
    .calc-result-box {{
      background: var(--surface-card);
      border: 1px solid var(--border-accent);
      border-radius: 16px;
      max-width: 480px;
      margin: 0 auto;
      padding: 24px;
    }}
    .calc-result-box .label {{
      font-size: 13px;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
    }}
    .calc-result-box .val {{
      font-family: 'Syne', sans-serif;
      font-size: 28px;
      font-weight: 800;
      color: var(--primary);
    }}
    .diag-tabs {{
      display: flex;
      justify-content: center;
      gap: 12px;
      margin-bottom: 28px;
      flex-wrap: wrap;
    }}
    .diag-tab {{
      background: var(--surface-card);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 10px 20px;
      border-radius: 100px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .diag-tab.active, .diag-tab:hover {{
      background: var(--accent-grad);
      color: #090b0e;
      border-color: rgba(255,255,255,0.5);
    }}

    /* FAQ */
    .faq-container {{
      max-width: 850px;
      margin: 0 auto;
    }}
    .faq-item {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      margin-bottom: 16px;
      overflow: hidden;
      transition: border-color 0.2s;
    }}
    .faq-item:hover {{ border-color: var(--border-accent); }}
    .faq-question {{
      padding: 22px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      font-weight: 600;
      font-size: 16px;
    }}
    .faq-answer {{
      display: none;
      padding: 0 28px 22px;
      color: var(--text-muted);
      font-size: 14.5px;
      line-height: 1.6;
    }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--border);
      padding: 80px 24px 40px;
      background: #060709;
      color: var(--text-muted);
    }}
    .footer-wrap {{
      max-width: 1320px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 50px;
      padding-bottom: 60px;
      border-bottom: 1px solid var(--border);
    }}
    .footer-brand h2 {{
      font-size: 22px;
      color: white;
      margin-bottom: 12px;
    }}

    @media (max-width: 960px) {{
      .hero {{ grid-template-columns: 1fr; padding-top: 40px; }}
      .grid-3 {{ grid-template-columns: 1fr; }}
      .trust-wrap {{ grid-template-columns: 1fr 1fr; }}
      .footer-wrap {{ grid-template-columns: 1fr; }}
      .nav-links {{ display: none; }}
      .hero h1 {{ font-size: 38px; }}
    }}
  </style>
</head>
<body>

  <!-- Top Live Status Bar -->
  <div class="status-bar">
    <div class="status-pulse">
      <div class="pulse-dot"></div>
      Available for Appointments & Emergency Calls in {b['location']}
    </div>
    <div>
      {b['source']} • Direct: <strong>{b['phone']}</strong>
    </div>
  </div>

  <!-- Floating Navigation -->
  <div class="nav-container">
    <nav>
      <a href="#" class="brand">
        <div class="brand-mark">{b['mark']}</div>
        <div class="brand-name">{b['short_name'].split()[0]}<span>{b['short_name'].split()[1] if len(b['short_name'].split()) > 1 else 'Pro'}</span></div>
      </a>
      <ul class="nav-links">
        <li><a href="#services">Services</a></li>
        <li><a href="#calculator">Estimator & Diagnostics</a></li>
        <li><a href="#faq">FAQ</a></li>
      </ul>
      <a href="#quote" class="btn-nav">Get Free Estimate</a>
    </nav>
  </div>

  <!-- Hero Section with Faded Job Background -->
  <div class="hero-outer">
    <section class="hero">
      <div>
        <div class="hero-badge">
          {b['badge_text']}
        </div>
        <h1>{b['hero_title']}</h1>
        <p class="hero-lead">{b['hero_sub']}</p>
        
        <div class="hero-cta-group">
          <a href="#quote" class="btn-hero-primary">
            Schedule Free Estimate
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
          <a href="tel:{b['phone'].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')}" class="btn-hero-secondary">
            Call {b['phone']}
          </a>
        </div>
      </div>

      <!-- Right Lead Capture -->
      <div class="quote-card" id="quote">
        <h3>Request Direct Service</h3>
        <p>Comprehensive photo assessment and itemized proposal sent to your email.</p>
        <form onsubmit="event.preventDefault(); alert('Request submitted! Our team will contact you within 30 minutes.');">
          <div class="input-box">
            <label>Your Name</label>
            <input type="text" placeholder="First & Last Name" required>
          </div>
          <div class="input-box">
            <label>Phone Number</label>
            <input type="tel" placeholder="{b['phone']}" required>
          </div>
          <div class="input-box">
            <label>Service Needed</label>
            <select>
              <option>{b['services'][0]['title']}</option>
              <option>{b['services'][1]['title']}</option>
              <option>{b['services'][2]['title']}</option>
            </select>
          </div>
          <button type="submit" class="btn-submit-card">Schedule Consultation ›</button>
        </form>
      </div>
    </section>
  </div>

  <!-- Trust Stats Strip -->
  <div class="trust-strip">
    <div class="trust-wrap">
      {stats_chips}
    </div>
  </div>

  {tool_html}

  <!-- Services Grid with Faded Job-Site Overlays -->
  <section class="section-wrap" id="services">
    <div class="section-head">
      <h2>Engineered for Long-Term Value</h2>
      <p>Precision craftsmanship tailored specifically for {b['service_area']} properties.</p>
    </div>

    <div class="grid-3">
      {services_cards}
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="section-wrap" id="faq">
    <div class="section-head">
      <h2>Frequently Asked Questions</h2>
      <p>Clear, direct answers for homeowners and property managers across {b['location']}.</p>
    </div>
    <div class="faq-container">
      {faq_items}
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-wrap">
      <div class="footer-brand">
        <h2>{b['name']}</h2>
        <p style="margin-bottom: 16px;">Dedicated service contractor serving {b['service_area']}. Backed by verified local licensing, insured technicians, and transparent pricing.</p>
        <p style="font-size: 13.5px; color: var(--primary);">Listed on {b['source']}</p>
      </div>
      <div>
        <h4 style="color: white; margin-bottom: 14px;">Contact Us</h4>
        <p style="margin-bottom: 8px;">Phone: <strong>{b['phone']}</strong></p>
        <p style="margin-bottom: 8px;">Email: <strong>{b['email']}</strong></p>
        <p>Service: {b['location']}</p>
      </div>
      <div>
        <h4 style="color: white; margin-bottom: 14px;">Operating Hours</h4>
        <p style="margin-bottom: 8px;">Mon – Fri: 7:00 AM – 6:00 PM</p>
        <p style="margin-bottom: 8px;">Saturday: 8:00 AM – 2:00 PM</p>
        <p>Sunday: Emergency Dispatch</p>
      </div>
    </div>
    <div style="text-align: center; padding-top: 30px; font-size: 13px;">
      © 2026 {b['name']}. All rights reserved. Handcrafted by Antigravity Digital Agency.
    </div>
  </footer>

  <script>
    function updateCost() {{
      const sqft = document.getElementById('sqftSlider').value;
      document.getElementById('sqftLabel').innerText = parseInt(sqft).toLocaleString() + ' sq. ft.';
      const low = Math.round(sqft * 2.1);
      const high = Math.round(sqft * 2.9);
      document.getElementById('priceDisplay').innerText = '$' + low.toLocaleString() + ' – $' + high.toLocaleString();
    }}

    function setDiag(idx) {{
      const tabs = document.querySelectorAll('.diag-tab');
      tabs.forEach((t, i) => t.classList.toggle('active', i === idx));
      const diagMessages = [
        "Immediate response team available in {b['location']}. Standard dispatch turnaround < 45 mins.",
        "Priority scheduling open for full system replacement and itemized estimate.",
        "Comprehensive diagnostic assessment available with transparent flat rates."
      ];
      document.getElementById('diagText').innerText = diagMessages[idx];
    }}

    function toggleFaq(el) {{
      const ans = el.nextElementSibling;
      const isOpen = ans.style.display === 'block';
      ans.style.display = isOpen ? 'none' : 'block';
      el.querySelector('span:last-child').innerText = isOpen ? '+' : '−';
    }}
  </script>

</body>
</html>
"""
    return html

def main():
    os.makedirs(SAMPLES_DIR, exist_ok=True)
    
    # Generate each site
    for b in businesses:
        site_folder = os.path.join(SAMPLES_DIR, b["id"])
        os.makedirs(site_folder, exist_ok=True)
        file_path = os.path.join(site_folder, "index.html")
        content = generate_html(b)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {b['id']} -> {file_path}")

    print(f"Successfully generated all {len(businesses)} bespoke websites!")

if __name__ == "__main__":
    main()
