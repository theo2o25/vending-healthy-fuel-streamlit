"""VHF — Vending Healthy Fuel landing page (Streamlit).

Locally owned & operated healthy snack vending in Tucson, AZ.
Edit content in data.py. Email via SendGrid (secrets: .streamlit/secrets.toml).
"""

import streamlit as st

from data import (
    SNACKS, STATS, HERO_TAGS, SPOTLIGHT_LOGOS, BENEFITS, STEPS,
    COMPANY_NAME, CONTACT_EMAIL, CONTACT_PHONE, CONTACT_PHONE_HREF, LOCATION,
    HERO_PHOTO, FAQ, FAQ_FALLBACK,
)

st.set_page_config(
    page_title="Vending Healthy Fuel (VHF) — Healthy Snacks for Students in Tucson, AZ",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# STYLING
# ---------------------------------------------------------------------------
CSS = """
<style>
:root{
  --leaf:#3f9d4f; --leaf-dark:#2f7a3c; --leaf-soft:#e4f1e0; --sun:#f2b33d;
  --sky:#2f9fb6; --berry:#e0536f; --ink:#1d2b22; --muted:#5c6b5e; --bg:#ffffff;
  --surface:#ffffff; --surface-2:#eef5ea; --line:rgba(29,43,34,0.12);
}
/* Remove Streamlit chrome so the page feels like a real site */
#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {visibility:hidden;}
[data-testid="stHeader"] { background: #ffffff; }
[data-testid="stAppViewContainer"] { background: #ffffff; }
[data-testid="stMainBlockContainer"] { background: #ffffff; }
.block-container { padding-top: 2rem; padding-bottom: 4rem; max-width: 1120px; }
body { background: #ffffff; color: var(--ink); }

h1, h2, h3 { color: var(--ink); letter-spacing:-0.02em; }
.kicker{ font-weight:800; text-transform:uppercase; letter-spacing:.16em;
         font-size:.72rem; color:var(--leaf-dark); margin-bottom:.2rem; }
.sect-title{ font-size:clamp(1.8rem,4vw,2.7rem); line-height:1.1; margin:0; }
.sect-title .g{ color:var(--leaf); }
.lede{ color:var(--muted); font-size:1.05rem; max-width:760px; margin-top:.6rem; }

/* Hero */
.hero-badge{ display:inline-block; font-weight:700; font-size:.82rem; color:var(--leaf-dark);
  background:var(--leaf-soft); border:1px solid rgba(63,157,79,.25);
  padding:8px 14px; border-radius:999px; margin-bottom:1rem; }
.brand-title{ font-size:clamp(1.6rem,3.4vw,2.4rem); font-weight:800; letter-spacing:-.01em;
  color:#000000; margin:0 0 .2rem; line-height:1.1; }
.brand-title .bt-v{ color:#000000; }
.brand-title .bt-h{ color:var(--leaf); }
.brand-title .bt-f{ color:var(--sun); }
.hero-title{ font-size:clamp(2.6rem,7vw,4.6rem); line-height:1.02; margin:0; }
.hero-title .g{ color:var(--leaf);} .hero-title .sun{ color:var(--sun);}
.hero-sub{ max-width:640px; font-size:clamp(1.05rem,1.6vw,1.2rem); color:var(--muted); margin:1.2rem 0 1.6rem; }

.chip-row{ display:flex; flex-wrap:wrap; gap:.6rem; }
.chip{ font-weight:600; font-size:.82rem; color:var(--ink); background:var(--surface);
  border:1px solid var(--line); padding:8px 14px; border-radius:999px; }

/* Cards */
.grid{ display:grid; grid-template-columns:repeat(4,1fr); gap:18px; }
.grid-2{ display:grid; grid-template-columns:repeat(2,1fr); gap:16px; }
.grid-3{ display:grid; grid-template-columns:repeat(3,1fr); gap:18px; }
.card{ background:var(--surface); border:1px solid var(--line); border-radius:16px; padding:26px 24px; }
.card.ctr{ text-align:center; }
/* Compact snack info boxes under each product image */
.snack{ padding:10px 10px; border-radius:12px; }
.snack .emoji{ font-size:1.5rem; }
.snack h3{ font-size:.9rem; margin:.35rem 0 .2rem; }
.snack p{ font-size:.78rem; line-height:1.35; }
.snack .tag{ margin-top:.5rem; font-size:.62rem; padding:3px 8px; }
.card .emoji{ font-size:2.4rem; line-height:1; }
.card h3{ font-size:1.02rem; font-weight:700; margin:.5rem 0 .25rem; }
.card p{ font-size:.86rem; color:var(--muted); margin:0; }
.card .tag{ display:inline-block; margin-top:.8rem; font-size:.68rem; font-weight:800;
  color:var(--leaf-dark); background:var(--leaf-soft); padding:4px 10px; border-radius:999px;
  letter-spacing:.04em; text-transform:uppercase; }
.benefit{ display:flex; gap:16px; }
.benefit .ico{ flex:none; width:44px; height:44px; border-radius:12px; background:var(--leaf-soft);
  display:grid; place-items:center; font-size:1.3rem; }
.benefit h3{ font-size:1rem; font-weight:700; margin:0 0 2px; }
.benefit p{ font-size:.9rem; color:var(--muted); margin:0; }

/* Host-a-machine callout */
.cta-card{ display:flex; gap:22px; align-items:center; justify-content:space-between;
  flex-wrap:wrap; background:linear-gradient(135deg,var(--leaf),var(--leaf-dark));
  color:#fff; border-radius:18px; padding:28px 30px; margin-top:1.5rem; }
.cta-card .cta-title{ font-size:clamp(1.3rem,2.6vw,1.8rem); font-weight:800; color:#fff; }
.cta-card .cta-title .g{ color:var(--sun); }
.cta-card p{ margin:.4rem 0 0; font-size:1rem; opacity:.95; max-width:36rem; }
.cta-link{ display:inline-block; background:var(--sun); color:#141a12; font-weight:800;
  font-size:1.05rem; padding:.85rem 1.6rem; border-radius:12px; text-decoration:none;
  box-shadow:0 4px 14px rgba(0,0,0,.18); transition:transform .12s ease; }
.cta-link:hover{ transform:translateY(-2px); color:#141a12; }
.step .n{ font-size:2rem; font-weight:800; color:var(--sun); line-height:1;
  text-transform:uppercase; letter-spacing:.04em; }
.step{ text-align:center; }
.step h3{ font-size:1.1rem; font-weight:700; margin-top:.4rem; }
.step p{ font-size:.92rem; color:var(--muted); }

/* Stats */
.stat .num{ font-size:clamp(1.9rem,3.4vw,2.6rem); font-weight:800; color:var(--leaf); }
.stat .num.sun{ color:var(--sun);} .stat .num.sky{ color:var(--sky);} .stat .num.berry{ color:var(--berry);}
.stat .lbl{ margin-top:.4rem; font-size:.86rem; color:var(--muted); font-weight:600; }

/* Spotlight */
.spotlight{ display:flex; gap:30px; align-items:center; background:linear-gradient(135deg,var(--leaf),var(--leaf-dark));
  color:#fff; border-radius:22px; padding:46px 44px; }
.spotlight .badge-big{ flex:none; width:88px; height:88px; border-radius:20px; background:rgba(255,255,255,.16);
  display:grid; place-items:center; font-size:2.4rem; }
.spotlight h3{ color:#fff; font-size:clamp(1.4rem,3vw,2rem); margin:0 0 .5rem; }
.spotlight p{ opacity:.94; font-size:1.02rem; margin:0 0 1rem; }
.logos{ display:flex; flex-wrap:wrap; gap:.5rem; }
.logos span{ background:rgba(255,255,255,.16); border-radius:999px; padding:6px 12px; font-size:.8rem; font-weight:700; }

/* Contact cards */
.c-card{ display:flex; gap:14px; align-items:center; background:var(--surface);
  border:1px solid var(--line); border-radius:14px; padding:18px 20px; margin-bottom:.8rem; }
.c-card .ico{ flex:none; width:42px; height:42px; border-radius:11px; background:var(--leaf-soft);
  display:grid; place-items:center; font-size:1.2rem; }
.c-card .lbl{ font-size:.72rem; font-weight:700; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); }
.c-card a{ color:var(--ink); font-weight:700; text-decoration:none; }
.c-card a:hover{ color:var(--leaf-dark); }

/* Buttons */
.stButton > button{ border-radius:12px; font-weight:700; }
div[data-testid="stForm"] { background:var(--surface); border:1px solid var(--line);
  border-radius:16px; padding:1.5rem 1.5rem 1rem; }
footer-note{margin-top:3rem;border-top:1px dashed var(--line);padding-top:1.2rem;
  font-size:.82rem;color:var(--muted);}

/* FAQ / chatbot */
.chat-card{ background:var(--surface); border:1px solid var(--line); border-radius:16px; padding:20px; }
.chat-q{ font-weight:600; margin-bottom:.3rem; }
.chat-qa{ background:var(--surface-2); border:1px solid var(--line); border-radius:12px;
  padding:12px 14px; margin-bottom:.6rem; }
.chat-qa .a{ color:var(--muted); font-size:.9rem; margin-top:.2rem; }
.chat-pill{ display:inline-block; background:var(--leaf-soft); border:1px solid rgba(63,157,79,.25);
  color:var(--leaf-dark); font-weight:700; font-size:.78rem; padding:8px 14px; border-radius:999px;
  margin:0 .5rem .5rem 0; cursor:pointer; }
.note{ font-size:.86rem; color:var(--muted); margin-top:.4rem; }

@media (max-width:900px){ .grid{grid-template-columns:repeat(2,1fr);} .grid-3{grid-template-columns:1fr;}
  .spotlight{flex-direction:column;align-items:flex-start;padding:34px 28px;} }
@media (max-width:520px){ .grid{grid-template-columns:1fr;} .grid-2{grid-template-columns:1fr;} }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def section_heading(kicker, title_html, lede=None):
    html = f'<div class="kicker">{kicker}</div><h2 class="sect-title">{title_html}</h2>'
    if lede:
        html += f'<p class="lede">{lede}</p>'
    st.markdown(html, unsafe_allow_html=True)
    st.write("")


def go_to(target: str):
    """Set a session flag that scrolls to an element id on the next rerun."""
    st.session_state["go"] = target


def handle_scroll():
    """Scroll to a section after the page renders (runs once per target)."""
    target = st.session_state.pop("go", None)
    if not target:
        return
    st.html(
        f"""
        <script>
        window.setTimeout(function(){{
            var el = document.getElementById('{target}');
            if (el) {{ el.scrollIntoView({{behavior:'smooth', block:'start'}}); }}
        }}, 250);
        </script>
        """
    )


def answer_question(text: str) -> str:
    """Return a FAQ answer for a free-text question, or the fallback."""
    t = text.lower()
    for item in FAQ:
        if any(k in t for k in [k.lower() for k in item["keywords"]]):
            return item["answer"]
    return FAQ_FALLBACK


# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------
col_l, col_r = st.columns([3, 2], vertical_alignment="center")
with col_l:
    st.markdown(
        f'<div class="hero-badge">Locally owned &amp; operated · {LOCATION}</div>'
        '<h1 class="hero-title">Healthy <span class="g">fuel</span> for student life — '
        '<span class="sun">one vending machine</span> at a time.</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p class='hero-sub'>VHF brings fresh, real snacks to the places students live and train — "
        "high schools, gyms, studios, and beyond. Better choices, right where they already are.</p>",
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        st.button("See the snacks", use_container_width=True, on_click=go_to, args=("snacks",))
    with c2:
        st.button("Host a machine", use_container_width=True, on_click=go_to, args=("contact",))
    chips = "".join(f'<span class="chip">{t}</span>' for t in HERO_TAGS)
    st.markdown(f'<div class="chip-row">{chips}</div>', unsafe_allow_html=True)
with col_r:
    st.markdown(
        '<div class="brand-title"><span class="bt-v">Vending</span> '
        '<span class="bt-h">Healthy</span> <span class="bt-f">Fuel</span></div>',
        unsafe_allow_html=True,
    )
    st.image(HERO_PHOTO, width="stretch")

st.write("")
st.write("")

# ---------------------------------------------------------------------------
# STATS
# ---------------------------------------------------------------------------
cards = ["".join(f'<div class="card ctr stat"><div class="num {s.get("accent","")}">{s["num"]}</div>'
                 f'<div class="lbl">{s["label"]}</div></div>') for s in STATS]
st.markdown(f'<div class="grid">{"".join(cards)}</div>', unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------------------------------------------------------------------
# SNACKS
# ---------------------------------------------------------------------------
st.markdown('<div id="snacks"></div>', unsafe_allow_html=True)
section_heading("What's inside", "Real snacks, <span class='g'>no junk.</span>",
                "Every machine is stocked with treats students actually want — heat-safe and "
                "weather-proof for Arizona, so nothing melts, sours, or goes stale in the machine.")

# Render snacks 4-per-row with Streamlit columns so local images display correctly.
COLS_PER_ROW = 4
for i in range(0, len(SNACKS), COLS_PER_ROW):
    row = SNACKS[i:i + COLS_PER_ROW]
    cols = st.columns(len(row))
    for col, s in zip(cols, row):
        with col:
            st.image(s["photo"], width="stretch")
            st.markdown(
                f'<div class="card ctr snack">'
                f'<div class="emoji">{s["emoji"]}</div>'
                f'<h3>{s["name"]}</h3><p>{s["desc"]}</p>'
                f'<span class="tag">{s["tag"]}</span></div>',
                unsafe_allow_html=True,
            )

st.write("")
st.write("")

# ---------------------------------------------------------------------------
# SPOTLIGHT (TUSD + locations)
# ---------------------------------------------------------------------------
logos = "".join(f"<span>{l}</span>" for l in SPOTLIGHT_LOGOS)
st.markdown(
    '<div class="spotlight"><div class="badge-big">🏫</div><div>'
    "<h3>Serving Tucson's students today.</h3>"
    "<p>VHF holds the vending contract for the Tucson Unified School District, and Tucson High just "
    "came on board — with machines live at BC Dance Studio and rolling out at private schools, the YMCA, "
    "gyms, hospitals, and commercial areas across the region.</p>"
    f'<div class="logos">{logos}</div></div></div>',
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# ---------------------------------------------------------------------------
# FOR PARTNERS
# ---------------------------------------------------------------------------
section_heading("For partners", "Bring better snacking <span class='g'>to your space.</span>",
                "Schools, gyms, studios, hospitals and community centers — VHF handles everything "
                "so you can offer your students and members a healthy choice.")
benefits = "".join(
    f'<div class="card benefit"><div class="ico">{b["emoji"]}</div><div>'
    f'<h3>{b["title"]}</h3><p>{b["desc"]}</p></div></div>'
    for b in BENEFITS
)
st.markdown(f'<div class="grid">{benefits}</div>', unsafe_allow_html=True)

# Host-a-machine callout (full width below the benefits)
st.markdown(
    '<div class="cta-card">'
    '<div><div class="cta-title">Host a <span class="g">machine.</span></div>'
    "<p>Tell us about your location and we'll take it from there — installation, stocking, "
    "and service all handled by VHF.</p></div>"
    '<a class="cta-link" href="#contact">Request a placement</a></div>',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
section_heading("How it works", "Simple from <span class='g'>start to snack.</span>")
steps = "".join(
    f'<div class="card step"><div class="n">Step {s["n"]}</div><h3>{s["title"]}</h3><p>{s["desc"]}</p></div>'
    for s in STEPS
)
st.markdown(f'<div class="grid-3">{steps}</div>', unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------------------------------------------------------------------
# FAQ / CHATBOT
# ---------------------------------------------------------------------------
st.markdown('<div id="faq"></div>', unsafe_allow_html=True)
section_heading("Quick answers", "Got questions? <span class='g'>We've got you.</span>",
                "Ask away, or tap a common question below. This little helper answers instantly "
                "from our knowledge base.")

chat_l, chat_r = st.columns([3, 2])
with chat_l:
    st.markdown('<div class="chat-card">', unsafe_allow_html=True)
    qtext = st.text_input("Your question", placeholder='e.g. "How much does it cost to host?"',
                          key="faq_input", label_visibility="collapsed")
    if st.button("Ask", type="primary"):
        if qtext.strip():
            st.session_state["faq_answer"] = answer_question(qtext.strip())
        else:
            st.session_state["faq_answer"] = "Please type a question first! 👇"
    if "faq_answer" in st.session_state:
        st.markdown(f'<div class="chat-qa"><div class="a">{st.session_state["faq_answer"]}</div></div>',
                    unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with chat_r:
    # Common questions as quick-tap pills
    pills = ["How much does it cost?", "How do I host a machine?",
             "What snacks do you sell?", "How do I contact you?"]
    st.markdown('<div class="note">Common questions:</div>', unsafe_allow_html=True)
    for p in pills:
        if st.button(p, key=f"pill_{p}"):
            st.session_state["faq_answer"] = answer_question(p)

st.write("")
st.write("")

# ---------------------------------------------------------------------------
# CONTACT + ENQUIRY FORM
# ---------------------------------------------------------------------------
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
section_heading("Get in touch", "Let's talk <span class='g'>healthy fuel.</span>",
                "Questions, placement requests, or partnership ideas — send a note and we'll get back to you.")

left, right = st.columns(2)

with left:
    st.markdown(
        f'<div class="c-card"><div class="ico">✉️</div><div><div class="lbl">Email</div>'
        f'<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></div></div>'
        f'<div class="c-card"><div class="ico">📞</div><div><div class="lbl">Phone</div>'
        f'<a href="{CONTACT_PHONE_HREF}">{CONTACT_PHONE}</a></div></div>'
        f'<div class="c-card"><div class="ico">📍</div><div><div class="lbl">Location</div>'
        f'<div style="font-weight:700">{LOCATION}</div></div></div>',
        unsafe_allow_html=True,
    )

with right:
    with st.form("enquiry_form"):
        st.write("**Send us a message**")
        name = st.text_input("Name", placeholder="Your name")
        email = st.text_input("Email", placeholder="you@email.com")
        org = st.text_input("Organization / location (optional)", placeholder="e.g. Sunrise High School")
        enquiry_type = st.selectbox(
            "I'm interested in…",
            ["Hosting a machine at my location", "Placing a machine somewhere",
             "A partnership inquiry", "General question"],
        )
        message = st.text_area("Message", placeholder="Tell us a little about your location or question...")
        submitted = st.form_submit_button("Send Message →", type="primary")

# ---------------------------------------------------------------------------
# EMAIL SEND (SendGrid)
# ---------------------------------------------------------------------------
def email_configured():
    """True if the SendGrid secrets are set (not the placeholders)."""
    try:
        s = st.secrets["sendgrid"]
        api = s.get("api_key", "")
        fr = s.get("from_email", "")
        return bool(api and fr and "YOUR_" not in api and "YOUR_" not in fr)
    except Exception:  # noqa: BLE001  (no secrets file / missing key)
        return False


def send_enquiry(name, email, org, enquiry_type, message):
    """Send the enquiry via SendGrid using Streamlit secrets."""
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    api_key = st.secrets["sendgrid"]["api_key"]
    _from = st.secrets["sendgrid"]["from_email"]
    _to = st.secrets["sendgrid"].get("to_email", CONTACT_EMAIL)

    body = (
        f"New VHF website enquiry\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Organization/Location: {org or '—'}\n"
        f"Interested in: {enquiry_type}\n\n"
        f"Message:\n{message}\n"
    )
    mail = Mail(from_email=_from, to_emails=_to,
                subject=f"VHF enquiry from {name} ({enquiry_type})", plain_text_content=body)
    sg = SendGridAPIClient(api_key)
    sg.send(mail)


if submitted:
    if not name or not email or not message:
        st.error("Please fill in your name, email, and message.")
    elif not email_configured():
        st.warning(
            "Thanks — we got your message! Our email sender isn't configured yet, "
            "so this wasn't delivered. Add your SendGrid key (see the README / "
            ".streamlit/secrets.toml.example) to start receiving enquiries."
        )
    else:
        try:
            send_enquiry(name, email, org, enquiry_type, message)
            st.success("Thanks! Your message is on its way — we'll reply shortly.")
        except Exception as exc:  # noqa: BLE001
            st.error(f"Something went wrong sending your message. Please email {CONTACT_EMAIL} directly.")
            st.caption(f"Details: {exc}")

st.markdown(
    f'<div class="footer-note"><span>© 2026 {COMPANY_NAME}. All rights reserved. '
    f'Locally owned &amp; operated in {LOCATION}.</span></div>',
    unsafe_allow_html=True,
)

handle_scroll()
