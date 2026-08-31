"""Editable content for the VHF (Vending Healthy Fuel) landing page.

Edit the lists below and redeploy — the change goes live instantly.
Snacks are shown in-order on the page.
"""

# ---------------------------------------------------------------------------
# PHOTOS (local images in the app's `images/` folder)
# ---------------------------------------------------------------------------
# Real photo files live in the `images/` directory next to this file. To change
# a photo, replace the file in `images/` (keeping the same name) — no code edit
# needed. `photo` is the relative path used to load each file.
HERO_PHOTO = "images/hero.jpg"

# ---------------------------------------------------------------------------
# SNAPSHOT CATALOG
# ---------------------------------------------------------------------------
# Each snack: emoji, name, short description, category tag, and photo.
SNACKS = [
    {"emoji": "🥜", "name": "Trail Mix & Nuts", "desc": "Crispy, salty, energy-packed handfuls.", "tag": "Protein",
     "photo": "images/trail-mix.jpg"},
    {"emoji": "🌾", "name": "Granola & Seed Bars", "desc": "Chewy, filling bars made from real whole grains.", "tag": "Fiber",
     "photo": "images/granola.jpg"},
    {"emoji": "🍿", "name": "Popcorn & Crisps", "desc": "Light, crunchy snacks that won't weigh you down.", "tag": "Better Snack",
     "photo": "images/popcorn.jpg"},
    {"emoji": "🥕", "name": "Veggie Chips", "desc": "Crunchy, colorful chips packed with real vegetables.", "tag": "Heat-Safe",
     "photo": "images/veggie-chips.jpg"},
    {"emoji": "🍫", "name": "Dark Chocolate Snacks", "desc": "Healthy but sweet chocolatey options.", "tag": "Better Treat",
     "photo": "images/dark-chocolate.jpg"},
    {"emoji": "⚡", "name": "Healthy Energy Drinks", "desc": "Clean, low-sugar boosts to fuel busy students.", "tag": "Energy",
     "photo": "images/energy-drink.jpg"},
    {"emoji": "💧", "name": "Water & Hydration", "desc": "Hydrating drinks to go with every snack.", "tag": "Hydrate",
     "photo": "images/water.jpg"},
    {"emoji": "🥨", "name": "More Better Choices", "desc": "Curated options that hit the spot — minus the junk.", "tag": "Curated",
     "photo": "images/better-choices.jpg"},
]

# ---------------------------------------------------------------------------
# TRUST / STATS
# ---------------------------------------------------------------------------
STATS = [
    {"num": "TUSD", "label": "Vending contract for Tucson Unified School District"},
    {"num": "🏫", "label": "Tucson High just came on board!", "accent": "sun"},
    {"num": "🩰", "label": "BC Dance Studio on board", "accent": "sky"},
    {"num": "100%", "label": "Locally owned & operated", "accent": "berry"},
]

# ---------------------------------------------------------------------------
# LOCATIONS (hero chips, spotlight + partner paths)
# ---------------------------------------------------------------------------
HERO_TAGS = [
    "🏫 TUSD high schools",
    "🏛️ Private schools",
    "💃 Dance academies",
    "🏢 Commercial areas",
    "💪 Gyms",
    "🏥 Hospitals",
    "🤸 YMCA",
]

SPOTLIGHT_LOGOS = [
    "Public schools",
    "Private schools",
    "Dance studios",
    "Gyms",
    "Hospitals",
    "Commercial areas",
]

# ---------------------------------------------------------------------------
# PARTNER BENEFITS
# ---------------------------------------------------------------------------
BENEFITS = [
    {"emoji": "🔌", "title": "We do the work", "desc": "We install, stock, and service the machine. You just host it."},
    {"emoji": "🌿", "title": "Healthy by design", "desc": "Responsible snack options that align with your wellness mission."},
    {"emoji": "🚀", "title": "Zero hassle, real value", "desc": "No overhead, no inventory, no maintenance — just better snacks on site."},
    {"emoji": "🤝", "title": "A local partner", "desc": "Locally owned in Tucson, committed to your community."},
]

# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
STEPS = [
    {"n": "1", "title": "Pick your location", "desc": "Tell us where you'd like a machine — or we find the perfect spot for yours."},
    {"n": "2", "title": "We place & stock it", "desc": "VHF installs the machine and fills it with healthy, wanted snacks."},
    {"n": "3", "title": "We handle the rest", "desc": "Stocking, servicing, and keeping it fresh — done for you, ongoing."},
]

# ---------------------------------------------------------------------------
# CONTACT (public-facing)
# ---------------------------------------------------------------------------
COMPANY_NAME = "Vending Healthy Fuel (VHF)"
CONTACT_EMAIL = "info@vendinghealthyfuel.com"
CONTACT_PHONE = "(520) 710-8264"
CONTACT_PHONE_HREF = "tel:+15207108264"
LOCATION = "Tucson, Arizona"

# ---------------------------------------------------------------------------
# FAQ / CHATBOT KNOWLEDGE BASE
# ---------------------------------------------------------------------------
# Rule-based chatbot answers. Each item has keywords the bot matches against
# and an answer. Edit freely — the bot reads this list on each run.
FAQ = [
    {
        "keywords": ["install", "time", "how long", "duration"],
        "answer": "VHF’s team installs and stocks the machine in about 1‑2 hours, then it’s ready to go. This of course is dependent on the number of machines, machine size and location challenges."
    },
    {
        "keywords": ["price", "cost", "how much", "pricing", "expensive", "fee"],
        "answer": "For you? Nothing. Absolutely nothing — $0, zero, zilch. 🙃 VHF installs, stocks, and "
                  "services the machine, so hosting at your place costs you zero dollars. (The only thing "
                  "with fewer dollars than that is... nothing. And that's exactly what you pay.)",
    },
    {
        "keywords": ["host", "machine", "placement", "my location", "my school"],
        "answer": "Hosting is easy: we handle everything — installation, stocking, and servicing — you just "
                  "provide the space. Use the contact form and we'll take it from there.",
    },
    ...
    {
        "keywords": ["contact", "email", "phone", "call", "reach", "talk", "speak", "number"],
        "answer": f"You can reach us at {CONTACT_PHONE} or {CONTACT_EMAIL}. Or send a message through the "
                  "contact form below and we'll get right back to you.",
    },
    {
        "keywords": ["donate", "donation", "give", "give back", "support", "fund"],
        "answer": "We love giving back to the communities that host us — we're always happy to support the "
                  "schools and clubs we work with. Ask us about it when you reach out.",
    },
    {
        "keywords": ["who", "about", "owned", "local", "tucson", "arizona", "company", "business"],
        "answer": f"Vending Healthy Fuel (VHF) is a locally owned and operated business right here in {LOCATION}. "
                  "We bring healthy snacking to students across the region.",
    },
    {
        "keywords": ["hi", "hello", "hey", "yo"],
"answer": "Hi there! 👋 Ask me about our snacks, where we're located, how to host a machine, or "
                  "anything else — happy to help.",
    },
    {
        "keywords": ["install", "time", "how long", "duration"],
        "answer": "VHF’s team installs and stocks the machine in about 1‑2 hours, then it’s ready to go. This of course is dependent on the number of machines, machine size and location challenges."
    },
    {
        "keywords": ["problem", "solution", "fix", "issue"],
        "answer": "VHF solves the problem of students going hungry between meals by bringing healthy, grab‑and‑go snacks right into their schools and activity spaces — no cost to the host."
    },
    {
        "keywords": ["maintain", "service", "repair", "upkeep"],
        "answer": "Once installed, VHF handles all maintenance and restocking — the machine is serviced regularly so it never runs out of popular items."
    },
    {
        "keywords": ["partnership", "partner", "collab"],
        "answer": "VHF partners with local schools, gyms, and community sites — the host provides the space, VHF supplies and maintains the machine at no cost."
    },
]
# Fallback when no keyword matches.
FAQ_FALLBACK = ("I'm not sure about that one yet — but our team would be happy to help! "
                "Send us a message through the contact form, or email info@vendinghealthyfuel.com.")
