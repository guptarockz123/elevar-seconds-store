import streamlit as st
import streamlit.components.v1 as components

# Configure the Streamlit page to take up the full screen width and hide default UI
st.set_page_config(
    page_title="Elevar Seconds",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove Streamlit's default padding, headers, and footers for a full-bleed app feel
st.markdown("""
    <style>
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    </style>
""", unsafe_allow_html=True)

# 1. Retrieve the password securely from Streamlit Secrets
# If it's missing (e.g. forgot to set up secrets), it falls back safely.
try:
    secure_password = st.secrets["ADMIN_PASSWORD"]
except KeyError:
    secure_password = "admin" # Fallback ONLY for local testing if secrets are missing

# 2. Read the raw HTML file
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_data = f.read()
except FileNotFoundError:
    st.error("Could not find index.html. Ensure it is in the same directory as app.py.")
    st.stop()

# 3. Inject the password dynamically into the JavaScript
# We look for the placeholder in the JS and swap it with our secure password.
html_data = html_data.replace("__INJECTED_ADMIN_PASSWORD__", secure_password)

# 4. Render the HTML using Streamlit Components
# Height is set high enough to accommodate the store page.
components.html(html_data, height=1200, scrolling=True)