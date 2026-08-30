import streamlit as st

st.set_page_config(
    page_title="Vending Healthy Fuel (VHF) — Tucson, AZ",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PAGE_URL = "https://theo2o25.github.io/vending-healthy-fuel/"

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header[data-testid="stHeader"] {background: transparent;}
    [data-testid="stToolbar"] {visibility: hidden;}
    [data-testid="stDecoration"] {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.components.v1.html(
    f"""
    <iframe
        src="{PAGE_URL}"
        style="position:fixed; top:0; left:0; width:100vw; height:100vh; border:0;"
        title="VHF — Vending Healthy Fuel"
    ></iframe>
    """,
    height=1000,
)
