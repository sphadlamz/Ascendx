import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AscendX",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "home"

# --------------------------------------------------
# URL PAGE HANDLING (HTML BUTTON NAV)
# --------------------------------------------------
query_params = st.query_params
if "page" in query_params:
    st.session_state.page = query_params["page"]

# --------------------------------------------------
# CSS (GLOBAL STYLES)
# --------------------------------------------------
st.markdown("""
<style>

/* ================================
   GLOBAL
================================ */
html, body {
    background-color: #f7f7fb;
    font-family: "Inter", sans-serif;
}

/* ================================
   HEADER
================================ */
.header {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: white;
    padding: 14px 28px;
    border-bottom: 1px solid #e5e7eb;
}

/* ================================
   LOGO
================================ */
.logo {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 22px;
    font-weight: 800;
    color: #111827;
}

.logo-badge {
    background: #6B4C7A;
    color: white;
    padding: 8px 12px;
    border-radius: 12px;
    font-size: 14px;
}

/* ================================
   NAV BAR (MATCH HOME BUTTONS)
================================ */
.nav-bar {
    display: flex;
    gap: 14px;
    justify-content: center;
}

.nav-html-btn {
    min-width: 160px;
    height: 48px;
    border-radius: 14px;

    background: white;
    border: 1px solid #d1d5db;

    font-size: 14px;
    font-weight: 600;
    color: #6B4C7A;

    cursor: pointer;
    transition: all 0.2s ease-in-out;
}

.nav-html-btn:hover {
    background: #6B4C7A;
    color: white;
    border-color: #6B4C7A;
}

/* ================================
   USER INFO
================================ */
.user-info {
    text-align: right;
    font-size: 14px;
    color: #111827;
}

.user-info span {
    font-size: 12px;
    color: #6b7280;
}

/* ================================
   HERO
================================ */
.hero {
    padding: 80px 40px;
    text-align: center;
}

.hero-tag {
    display: inline-block;
    background: #f1e8f5;
    color: #6B4C7A;
    padding: 8px 16px;
    border-radius: 999px;
    font-weight: 600;
    margin-bottom: 20px;
}

.hero h1 {
    font-size: 64px;
    font-weight: 800;
    margin: 0;
}

.hero h1 span {
    color: #6B4C7A;
}

.hero p {
    max-width: 800px;
    margin: 24px auto;
    font-size: 18px;
    color: #4b5563;
}

/* ================================
   CTA BUTTONS
================================ */
.cta-bar {
    margin-top: 40px;
    display: flex;
    justify-content: center;
    gap: 20px;
}

.cta-primary {
    background: #6B4C7A;
    color: white;
    border-radius: 14px;
    padding: 14px 28px;
    font-size: 16px;
    font-weight: 700;
    border: none;
    cursor: pointer;
}

.cta-outline {
    background: white;
    color: #6B4C7A;
    border-radius: 14px;
    padding: 14px 28px;
    font-size: 16px;
    font-weight: 700;
    border: 1px solid #6B4C7A;
    cursor: pointer;
}

/* ================================
   CARDS
================================ */
.card {
    background: white;
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

/* ================================
   LOCATION CARD
================================ */
.location-card {
    background: white;
    border-radius: 16px;
    padding: 18px;
    border: 1px solid #e5e7eb;
    margin-bottom: 16px;
    transition: all 0.2s ease-in-out;
}

.location-card:hover {
    border-color: #6B4C7A;
    box-shadow: 0 10px 25px rgba(107, 76, 122, 0.15);
}

/* ================================
   FOOTER SPACING
================================ */
.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MOCK DATA
# --------------------------------------------------
MENTORS = [
    {"name": "Nandi Mokoena", "industry": "Agribusiness", "location": "Soweto", "lat": -26.2485, "lon": 27.8540},
    {"name": "Thabo Khumalo", "industry": "Retail", "location": "Durban", "lat": -29.8587, "lon": 31.0218},
]

CLIENTS = [
    {"name": "Lerato Foods", "service": "Catering", "lat": -26.2041, "lon": 28.0473},
    {"name": "Sipho Repairs", "service": "Phone & Laptop Repair", "lat": -29.8587, "lon": 31.0218},
]

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("<div class='header'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([3, 6, 3])

# LOGO
with col1:
    st.markdown("""
    <div class="logo">
        <div class="logo-badge">✨</div>
        AscendX
    </div>
    """, unsafe_allow_html=True)

# NAV
with col2:
    st.markdown("""
    <div class="nav-bar">
        <button class="nav-html-btn" onclick="window.location.href='?page=home'">Home</button>
        <button class="nav-html-btn" onclick="window.location.href='?page=mentors'">Find Mentors</button>
        <button class="nav-html-btn" onclick="window.location.href='?page=clients'">Find Clients</button>
        <button class="nav-html-btn" onclick="window.location.href='?page=login'">Sign In</button>
    </div>
    """, unsafe_allow_html=True)

# USER INFO
with col3:
    if st.session_state.user:
        st.markdown(f"""
        <div class="user-info">
            👤 <strong>{st.session_state.user['name']}</strong><br>
            <span>{st.session_state.user['role']}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# PAGES
# --------------------------------------------------

# HOME
if st.session_state.page == "home":
    st.markdown("""
    <div class="hero">
        <div class="hero-tag">✨ Empowering Women in Business</div>
        <h1>Connect. <span>Mentor.</span><br> Grow Together.</h1>
        <p>
            Find mentors who share your business interests, discover clients near you,
            and build meaningful connections with fellow women entrepreneurs.
        </p>

        <div class="cta-bar">
            <button class="cta-primary" onclick="window.location.href='?page=mentors'">Find a Mentor</button>
            <button class="cta-outline" onclick="window.location.href='?page=clients'">Find Clients</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# LOGIN
elif st.session_state.page == "login":
    st.subheader("Sign In")
    name = st.text_input("Full Name")
    role = st.selectbox("Role", ["Entrepreneur", "Mentor", "Client"])

    if st.button("Login"):
        if name:
            st.session_state.user = {"name": name, "role": role}
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("Please enter your name")

# MENTORS
elif st.session_state.page == "mentors":
    st.subheader("Find Mentors")
    df = pd.DataFrame(MENTORS)
    st.map(df[['lat','lon']])

    for m in MENTORS:
        st.markdown(f"""
        <div class="location-card">
            <h4>{m['name']}</h4>
            <p><strong>Industry:</strong> {m['industry']}</p>
            <p><strong>Location:</strong> {m['location']}</p>
        </div>
        """, unsafe_allow_html=True)

# CLIENTS
elif st.session_state.page == "clients":
    st.subheader("Find Clients")
    df = pd.DataFrame(CLIENTS)
    st.map(df[['lat','lon']])

    for c in CLIENTS:
        st.markdown(f"""
        <div class="location-card">
            <h4>{c['name']}</h4>
            <p><strong>Service:</strong> {c['service']}</p>
        </div>
        """, unsafe_allow_html=True)
