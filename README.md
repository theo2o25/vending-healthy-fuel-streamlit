# VHF — Streamlit Deployment

Source of the live landing page: [https://theo2o25.github.io/vending-healthy-fuel/](https://theo2o25.github.io/vending-healthy-fuel/)

This Streamlit app renders that page full-screen via an iframe. It's hosted through **Streamlit Community Cloud** (https://share.streamlit.io / https://streamlit.io/cloud).

## Deploy

1. Push this repo to GitHub (the `streamlit_app.py` at the repo root).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app** → pick this repo → branch `main` → main file `streamlit_app.py`.
4. Click **Deploy**.

The app will be live at `https://<you>-<repo>.streamlit.app`.

## Update

To change the site, edit the landing page in the GitHub Pages repo (theo2o25/vending-healthy-fuel). The Streamlit app always loads the latest version from there.
