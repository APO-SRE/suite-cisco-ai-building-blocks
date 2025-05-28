#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## ai-building-blocks-agent/app/routers/_domain_keywords.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
 
"""
DISCLAIMER: USE AT YOUR OWN RISK

This software is provided "as is", without any express or implied warranties, including, but not limited to,
the implied warranties of merchantability and fitness for a particular purpose. In no event shall the authors or
contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits;
or business interruption) however caused and on any theory of liability, whether in contract, strict liability,
or tort (including negligence or otherwise) arising in any way out of the use of this software.

This script is provided for demonstration and development purposes only and is not intended for use in production
environments. You are solely responsible for any modifications or adaptations made for your specific use case.

By using this code, you agree that you have read, understood, and accept these terms.
"""

import os

# ---------------------------------------------------------------------------
# FULL_MAP :  complete list (keys are the domain names, minus the 'lob-' prefix)
# ---------------------------------------------------------------------------
FULL_MAP = {
    "aerospace": [
        "satellite launch", "LEO", "GEO", "sun-synchronous orbit", "lunar orbiter",
        "Mars relay", "weather satellite", "communications satellite", "heavy-lift rocket",
        "rideshare", "launch date", "mission control", "telemetry checkpoint", "supersonic test",
        "noise compliance", "FAA certification", "emissions check", "airworthiness approval",
        "tilt-rotor", "cargo plane", "UAV permit", "prototype flight", "hybrid engine test",
        "wind tunnel calibration", "hydraulic maintenance", "solar panel test",
        "composite fuselage", "urban air mobility", "payload capacity", "assembly hangar"
  ],
    "agriculture": [
        "soil", "sandy", "clay", "ph", "cover crop", "crop rotation",
        "pest", "rootworm", "alfalfa", "soybeans", "wheat", "sulfur application",
        "livestock", "cows", "goats", "barn", "milk", "harvest", "hay",
        "water retention", "irrigation", "flooding", "hail damage", "orchard",
        "farm", "pasture", "fields", "crop cycle", "organic spray", "cutworm"
    ],
    "airline": [
        "airport", "airportcode", "airportname", "flight", "fl-", "baggage",
        "carry-on", "checked bag", "overweight fee", "crew base", "pilot",
        "first officer", "gate", "maintenance", "mt-", "tail #", "tail number",
        "A320", "737", "boarding", "departure", "arrival", "short haul",
        "long haul", "runway", "tire change", "hub", "aircraft", "capacity",
        "red-eye", "code share", "connecting flight", "economy", "business class",
        "lounge access", "frequent flyer", "altitudemiles", "recurrent training",
        "load factor", "delay", "weather issues"
    ],
    "automotive": [
        "production line", "battery supply", "EV", "electric vehicle", "hybrid",
        "sedan", "truck", "SUV", "infotainment", "warranty", "recall",
        "diesel", "towing", "emission", "maintenance records", "dealership feedback",
        "factory ramp", "chassis", "over-the-air updates", "fast-charging",
        "crossover", "fuel efficiency", "model specs", "hydrogen concept",
        "service center"
    ],
    "biotechnology": [
        "CRISPR", "CAR-T", "mRNA", "scaffolding", "lab experiments",
        "clinical trials", "off-target edits", "immune response", "gene editing",
        "research project", "distribution strategy", "adverse findings", "pre-IND",
        "therapeutic", "lymphoma", "inflammation", "lab data", "biosafety",
        "regulatory submission", "exemption request", "probiotic", "microbiome"
    ],
    "construction": [
        "foundation", "framing", "piling", "geotechnical", "concrete",
        "materials inventory", "crew scheduling", "building codes",
        "steel erection", "warehouse expansion", "school renovation",
        "project phases", "drywall", "rebar", "inspection", "subcontractor",
        "LEED-compliant", "fire-rated", "excavation", "basement"
    ],
    "consumer-electronics": [
        "smartphone", "smartwatch", "wireless earbuds", "4K TV", "gaming console",
        "RMA", "warranty", "accidental coverage", "battery drain", "sales invoice",
        "promotional discount", "earbuds", "repair ticket", "bundle deal",
        "customer feedback", "invoice", "TV upgrade event"
    ],
    "cybersecurity": [
        "phishing", "ransomware", "LockBox", "SQL injection", "DDoS", "APT",
        "zero-day", "threat intel", "incident", "remediation", "compromise",
        "firewall", "endpoint security", "MSSP coverage", "malware",
        "botnet", "intrusion", "breach", "SOC", "IR retainer", "spam filter",
        "threat detection", "vulnerability scanning"
    ],
    "e-commerce": [
        "order", "cart", "refund", "coupon", "promo code", "discount",
        "bulk purchase", "shipping", "inventory", "SKU", "fulfillment",
        "payment", "logistics", "tracking", "delivery", "checkout",
        "returns", "RMA", "priority shipping", "customer feedback"
    ],
    "education": [
        "course enrollment", "faculty", "exam schedule", "syllabus",
        "student advising", "academic probation", "lab practical",
        "bio 310", "math 201", "office hours", "professor", "tutoring",
        "essay", "incomplete course", "minor", "cs 420", "gpa"
    ],
    "energy-utilities": [
        "plant outage", "maintenance_outages", "battery storage", "wind farm",
        "transmission line", "time-of-use tariff", "coal station", "net metering",
        "renewables", "capacity reduction", "power factor", "grid infrastructure",
        "hydro upgrade", "turbine", "solar farm", "kWh", "battery pilot",
        "emissions retrofit", "billing"
    ],
    "entertainment-media": [
        "streaming", "season", "episode", "reality show", "viewership",
        "movie", "post-production", "children's show", "documentary",
        "music festival", "concert series", "venue", "advertising campaign",
        "licensing", "talent roster", "brand sponsor", "ticket vendor",
        "broadcast", "box office", "merchandise"
    ],
    "financial": [
        "investment portfolio", "equities", "bonds", "municipal bonds", "wire transfer",
        "AML", "compliance checks", "Q4 earnings", "profit margin", "revenue",
        "crypto", "BTC", "ETH", "retirement contributions", "mortgage",
        "loans", "interest-only", "cost-cutting", "operational expense",
        "merger", "due diligence", "shareholders meeting", "corporate report",
        "high-yield", "KYC", "dividends", "asset allocation", "rebalance"
    ],
    "food-and-beverage": [
        "menu item", "cheeseburger", "vegan wrap", "IPA beer", "organic salad",
        "cheesecake", "supplier", "food safety", "salmonella test", "keg",
        "catering order", "production record", "beef patties", "GreenLeaf produce",
        "strawberry", "dessert trays", "brew master", "batches", "sales orders"
    ],
    "gaming": [
        "fantasy rpg", "co-op", "level cap", "arcade flight sim", "leaderboard",
        "futuristic fps", "clan territory", "sandbox building", "turn-based strategy",
        "patch notes", "in-game transactions", "skin bundle", "mod expansions",
        "wizard", "battlequest", "skyracer", "cyberstrike", "citycraft",
        "tactical legends", "tournament", "clan war", "e-sports"
    ],
    "government-national-security": [
        "extremist activity", "sector", "cyber threat", "redcipher", "maritime security",
        "bomb threat", "capitol complex", "smuggling", "defense appropriations",
        "special operations", "firewallnext", "agency operations", "security events",
        "border security", "top secret", "national broadcasting continuity",
        "data privacy", "bill", "legislation", "task force", "strategic plan", "ops code"
    ],
    "healthcare": [
        "patient", "appointment", "physician", "nurse", "lab test", "cardiology",
        "pediatrics", "hematology", "billing codes", "policy on cancellations",
        "allergy appointment", "fasting", "diabetes follow-up", "neurology",
        "blood pressure", "A1C", "vaccine updates", "medical record",
        "pending confirmation", "hospital", "clinic", "doctor", "nurse"
    ],
    "hospitality": [
        "conference hall", "booking", "housekeeping", "inn", "family suite",
        "ski package", "airport suite", "loyalty tier", "spa facility",
        "wedding block", "complaint", "property listings", "meeting room discount",
        "silver tier", "basic tier", "housekeeping schedule", "off-season closure",
        "corporate booking", "post-event cleanup"
    ],
    "human-resources": [
        "employee", "manager", "performance review", "recent hires", "finance department",
        "sales commission", "training", "hr analytics", "referral applicant",
        "leadership essentials", "payroll", "recruitment", "applicant",
        "performance rating", "salary", "base salary", "stock options",
        "interview feedback"
    ],
    "information-technology-and-services": [
        "managed it", "cloud migration", "devops pipeline", "cybersecurity assessment",
        "data analytics", "etl pipeline", "BI dashboards", "service offerings",
        "compliance audits", "iso 27001", "pci-dss", "aws architecture",
        "azure baseline", "rmm", "patch scheduling", "project tasks",
        "pen testing", "vulnerability scanning"
    ],
    "insurance": [
        "policy", "coverage limit", "claims", "deductible", "premium payment",
        "homeowners", "auto coverage", "collision claim", "life insurance",
        "commercial property", "underwriting rules", "storm damage", "health plan",
        "out-of-pocket", "claim timeline", "complaint about claims", "kitchen fire",
        "policy renewal", "term life", "premium", "oop limit", "feedback on claim"
    ],
        "legal-services": [
        "case records", "contract dispute", "estate probate", "personal injury",
        "mergers and acquisitions", "patent infringement", "retainer agreement",
        "court filings", "client_contracts", "motion to compel", "compliance policies",
        "billing_invoices", "flat fee", "contingency", "probate", "demand letter"
    ],

    "manufacturing": [
        "injection molding", "metal stamping", "welding run", "assembly line",
        "paint defects", "quality inspections", "production plans", "supplier invoices",
        "maintenance schedules", "inventory records", "defect rate", "robotic welding",
        "resin pellets", "spot welds", "conveyor", "drip marks"
    ],

    "marketing-and-advertising": [
        "digital ads campaign", "tv spot", "email campaign", "direct mail",
        "influencer collaboration", "billboards", "client budget", "creative assets",
        "ad spend invoices", "performance metrics", "brand recall", "CTR", "ROI",
        "comedic angle", "social media push", "out-of-home ads"
    ],

    "mining-and-natural-resources": [
        "iron ore project", "open-pit copper", "coal mining", "gold project",
        "rare earth", "tailings pond", "equipment maintenance", "environmental audits",
        "drill rig", "haul truck", "extraction site", "deep boreholes", "borehole",
        "methane ventilation", "water discharge permit"
    ],

    "non-profit": [
        "fundraising_campaigns", "donor records", "corporate pledge", "food drive",
        "scholarship fund", "clean water initiative", "volunteer activities",
        "impact_reports", "community health fair", "winter coat drive",
        "project_funding", "monthly donor", "bulk food", "coats distribution"
    ],

    "oil-and-gas": [
        "offshore exploration", "onshore exploration", "shalepeak", "arctic shelf",
        "sour gas", "HSE", "production field", "drilling rig", "top drive overhaul",
        "fracking pump", "NGL shipment", "BOP test", "condensate", "ice management",
        "wellhead inspection"
    ],

    "pharmaceuticals": [
        "neocure", "viraxin", "analge-patch", "generic antibiotic", "phase ii",
        "adverse_events", "distribution_logistics", "production_batches",
        "regulatory_submissions", "injectable device", "glucose monitor",
        "IND application", "ANDA", "stability data", "patch reformulation"
    ],

    "professional-services": [
        "management consulting", "financial advisory", "HR talent solutions",
        "IT & digital transformation", "marketing & brand advisory",
        "compliance_standards", "ISO 9001", "peer review", "client deliverables",
        "M&A due diligence", "org design", "valuation model", "recruitment strategy"
    ],

    "real-estate": [
        "property listing", "tenant records", "commercial unit", "condo",
        "luxury penthouse", "maintenance requests", "property sales", "lease",
        "rent invoice", "HVAC repair", "suburban house", "downtown apartment",
        "partial rent payment", "property listing id"
    ],

    "retail": [
        "men’s running shoes", "yoga pants", "headphones", "smartwatch",
        "store inventory", "loyalty tier", "sales transactions", "returns_exchanges",
        "cash purchase", "promotions", "defective item", "discount code",
        "refund", "platinum loyalty", "unisex hoodie"
    ],

    "social-services": [
        "youth mentorship", "elderly assistance", "job training", "homeless outreach",
        "family counseling", "intake forms", "outcome_reports", "client_cases",
        "staff_records", "volunteer activities", "academic challenges",
        "daily meal distribution", "case coordinator"
    ],

    "state-local-government": [
        "neighborhood safety", "council_meetings", "permits_licenses",
        "small business growth", "public transportation", "community health outreach",
        "public projects", "resident_records", "ward", "green energy initiative",
        "solar permit", "road widening", "city council"
    ],

    "telecommunications": [
        "mobile plan", "family plan", "fiber internet", "business broadband",
        "unlimited data", "combined billing", "network outages", "support ticket",
        "LTE upgrade", "international calls", "invoice", "bundling discount",
        "late payment", "overseas call glitch"
    ],

    "transportation-and-logistics": [
        "truck route", "van shuttle", "rail freight", "ship cargo", "air cargo flight",
        "shipment id", "freight invoice", "warehouse inventory", "maintenance records",
        "port terminal", "distribution center", "driver", "fleet schedules",
        "cargo hub", "daily express packages"
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# Choose slice based on env-var
# ─────────────────────────────────────────────────────────────────────────────
_active = os.getenv("DOMAIN_SAMPLES_INDEX_FOLDER_NAME", "").strip().lower()

# • If `_active` is blank or not in FULL_MAP  → expose the whole map  
# • If it matches a key (e.g. "airline")      → expose only that slice
DOMAIN_KEYWORDS_MAP = (
    FULL_MAP if not _active or _active not in FULL_MAP
    else { _active: FULL_MAP[_active] }
)