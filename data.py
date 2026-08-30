"""Editable content for the VHF (Vending Healthy Fuel) landing page.

Edit the lists below and redeploy — the change goes live instantly.
Snacks are shown in-order on the page.
"""

# ---------------------------------------------------------------------------
# SNAPSHOT CATALOG
# ---------------------------------------------------------------------------
# Each snack: emoji, name, short description, and a category tag.
SNACKS = [
    {"emoji": "🥜", "name": "Trail Mix & Nuts", "desc": "Crispy, salty, energy-packed handfuls.", "tag": "Protein"},
    {"emoji": "🌾", "name": "Granola & Seed Bars", "desc": "Chewy, filling bars made from real whole grains.", "tag": "Fiber"},
    {"emoji": "🍿", "name": "Popcorn & Crisps", "desc": "Light, crunchy snacks that won't weigh you down.", "tag": "Better Snack"},
    {"emoji": "🥕", "name": "Veggie Chips", "desc": "Crunchy, colorful chips packed with real vegetables.", "tag": "Heat-Safe"},
    {"emoji": "🍫", "name": "Dark Chocolate", "desc": "Rich 70%+ cacao — a better treat that's more heat-tolerant.", "tag": "Better Treat"},
    {"emoji": "⚡", "name": "Healthy Energy Drinks", "desc": "Clean, low-sugar boosts to fuel busy students.", "tag": "Energy"},
    {"emoji": "💧", "name": "Water & Hydration", "desc": "Hydrating drinks to go with every snack.", "tag": "Hydrate"},
    {"emoji": "🥨", "name": "More Better Choices", "desc": "Curated options that hit the spot — minus the junk.", "tag": "Curated"},
]

# ---------------------------------------------------------------------------
# TRUST / STATS
# ---------------------------------------------------------------------------
STATS = [
    {"num": "TUSD", "label": "Active school district contract"},
    {"num": "HS+", "label": "High schools served", "accent": "sun"},
    {"num": "7+", "label": "Types of locations", "accent": "sky"},
    {"num": "100%", "label": "Locally owned & operated", "accent": "berry"},
]

# ---------------------------------------------------------------------------
# LOCATIONS (hero chips, spotlight + partner paths)
# ---------------------------------------------------------------------------
HERO_TAGS = [
    "🏫 TUSD high schools",
    "🏛️ Private schools",
    "💃 Dance academies",
    "🎓 Juijitsu schools",
    "💪 Gyms",
    "🏥 Hospitals",
    "🤸 YMCA",
]

SPOTLIGHT_LOGOS = [
    "Tucson Unified School District",
    "Private schools",
    "BC Dance Studio",
    "YMCA",
    "Gyms",
    "Hospitals",
    "Jiujitsu & Dance",
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
