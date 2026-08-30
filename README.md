# VHF — Vending Healthy Fuel (Streamlit)

A real Streamlit app for the **Vending Healthy Fuel** landing page — complete with a working
enquiry form that emails you, and an editable snack catalog.

- **Business:** Locally owned & operated healthy snack vending — Tucson, Arizona
- **App:** [Streamlit Community Cloud](https://streamlit.io/cloud)
- **Files:**
  - `streamlit_app.py` — the app (landing page + enquiry form)
  - `data.py` — edit the snack catalog, stats, locations, and copy here
  - `.streamlit/secrets.toml.example` — template for email secrets (README below)

---

## Deploy (easy mode) 🚀

1. **Push this repo to GitHub** (already done → `theo2o25/vending-healthy-fuel-streamlit`).
2. **Connect GitHub → Streamlit:**
   - (If you don't have one, create a free account at https://streamlit.io/cloud)
   - Sign in with your GitHub account so Streamlit can see your repos.
3. **Create the app:**
   - Go to **streamlit.io/cloud** → **New app**.
   - Pick repo `vending-healthy-fuel-streamlit`, branch `main`, file `streamlit_app.py`.
   - Click **Deploy**.
4. In a minute or two your app is live at:
   `https://<account>-vending-healthy-fuel-streamlit.streamlit.app`

**To update the site:** edit `data.py` or `streamlit_app.py`, commit, and push to `main`.
Streamlit redeploys automatically.

---

## Enquiry form → your email (SendGrid)

The form emails enquiries to your inbox. Set up once:

1. Create a free **SendGrid** account (https://signup.sendgrid.com). Free tier = 100 emails/day.
2. In SendGrid: **Settings → Sender Authentication** → verify a sender email
   (e.g. `no-reply@vendinghealthyfuel.com`).
3. In SendGrid: **Settings → API Keys → Create API Key** — copy the key.
4. Back in this repo, fill in the secrets:
   - On **local**: copy `.streamlit/secrets.toml.example` → `.streamlit/secrets.toml`
     and paste your key + verified sender + your recipient (`info@vendinghealthyfuel.com`).
   - On **Streamlit Cloud**: in your app dashboard → **Settings → Secrets**, paste:
     ```toml
     [sendgrid]
     api_key = "YOUR_KEY"
     from_email = "no-reply@vendinghealthyfuel.com"
     to_email = "info@vendinghealthyfuel.com"
     ```
5. Redeploy / restart the app. Enquiries will now email you.

> The app works even without email configured — it warns the sender and falls back gracefully.

---

## Editing the snack catalog

Open **`data.py`**. Each snack is one line, e.g.:

```python
{"emoji": "🥜", "name": "Trail Mix & Nuts", "desc": "Crispy, salty, energy-packed handfuls.", "tag": "Protein",
 "photo": "images/trail-mix.jpg"},
```

Add, remove, or reorder — push to `main` and the site updates. Same file holds stats,
locations, partner benefits, the hero photo (`HERO_PHOTO`), and contact details.

**Photos (real images):** photos are local files in the **`images/`** folder. To change a
picture, just replace the file (keeping the same filename — e.g. `images/trail-mix.jpg`) —
no code edit needed. Reference hero via `HERO_PHOTO` and each snack via its `photo` key.
Because they're bundled with the repo, the same files serve locally and on Streamlit Cloud.

## FAQ chatbot

The page has a small rule-based FAQ helper (not an AI / LLM — a keyword matcher). Answers live in
the `FAQ` list at the bottom of **`data.py`** — edit the `keywords` and `answer` freely. It matches
free-text questions and the quick-tap pills, and falls back to `FAQ_FALLBACK` when nothing matches.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
