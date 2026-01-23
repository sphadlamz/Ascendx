import streamlit as st

st.set_page_config(page_title="AscendX", layout="wide")

# --------------------------------------------------
# SESSION STATE INIT
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "user" not in st.session_state:
    st.session_state.user = None


# --------------------------------------------------
# URL PAGE HANDLING
# --------------------------------------------------
query_params = st.query_params
if "page" in query_params:
    st.session_state.page = query_params["page"]


# --------------------------------------------------
# GLOBAL CSS
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
   HEADER BAR
================================ */
.header {
    position: sticky;
    top: 0;
    z-index: 999;
    background: white;
    padding: 12px 24px;
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
    font-weight: 700;
    color: #111827;
}

.logo-badge {
    background: #6B4C7A;
    color: white;
    padding: 6px 10px;
    border-radius: 10px;
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

/* Same style as Home CTA */
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

/* Hover */
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
    padding: 80px 20px;
    text-align: center;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
}

.hero span {
    color: #6B4C7A;
}

.hero p {
    margin-top: 12px;
    font-size: 17px;
    color: #6b7280;
}

/* ================================
   CTA BUTTONS
================================ */
.cta-btn {
    min-width: 220px;
    height: 52px;
    border-radius: 16px;
    font-size: 15px;
    font-weight: 700;
    border: none;
    cursor: pointer;
}

.cta-primary {
    background: #6B4C7A;
    color: white;
}

.cta-outline {
    background: white;
    border: 1px solid #6B4C7A;
    color: #6B4C7A;
}

.cta-primary:hover {
    background: #5a3e66;
}

.cta-outline:hover {
    background: #6B4C7A;
    color: white;
}

/* ================================
   CARDS
================================ */
.card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    transition: all 0.2s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 35px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER NAVIGATION
# --------------------------------------------------
st.markdown("<div class='header'>", unsafe_allow_html=True)
with st.container():
    col1, col2, col3 = st.columns([3, 6, 3])

    # LOGO
    with col1:
        st.markdown("""
        <div class="logo">
            <div class="logo-badge">✨</div>
            AscendX
        </div>
        """, unsafe_allow_html=True)

    # NAV BUTTONS (HTML)
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
            st.markdown(
                f"""
                <div class="user-info">
                    👤 <strong>{st.session_state.user['name']}</strong><br>
                    <span>{st.session_state.user['role']}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown("</div>", unsafe_allow_html=True)
st.write("")


# --------------------------------------------------
# PAGE: HOME
# --------------------------------------------------
if st.session_state.page == "home":
    st.markdown("""
    <div class="hero">
        <h1>Connect. <span>Mentor.</span><br>Grow Together.</h1>
        <p>Find mentors, connect with entrepreneurs, and grow women-led businesses.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Find a Mentor"):
            st.session_state.page = "mentors"

    with c2:
        if st.button("Find Clients"):
            st.session_state.page = "clients"


# --------------------------------------------------
# PAGE: MENTORS
# --------------------------------------------------
elif st.session_state.page == "mentors":
    st.subheader("🌍 Mentors Near You")

    mentors = [
        {"name": "Nomsa Dlamini", "skill": "Business Strategy"},
        {"name": "Lerato Molefe", "skill": "Marketing"},
        {"name": "Ayanda Khumalo", "skill": "Finance"}
    ]

    cols = st.columns(3)
    for i, m in enumerate(mentors):
        with cols[i]:
            st.markdown(f"""
            <div class="card">
                <h4>{m['name']}</h4>
                <p>{m['skill']}</p>
                <button class="cta-btn cta-primary">Book Session</button>
            </div>
            """, unsafe_allow_html=True)


# --------------------------------------------------
# PAGE: CLIENTS
# --------------------------------------------------
elif st.session_state.page == "clients":
    st.subheader("📍 Entrepreneurs Near You")

    clients = [
        {"name": "Thandi Beauty", "service": "Salon"},
        {"name": "Zanele Catering", "service": "Food Services"},
        {"name": "Mpho Fashion", "service": "Clothing"}
    ]

    cols = st.columns(3)
    for i, c in enumerate(clients):
        with cols[i]:
            st.markdown(f"""
            <div class="card">
                <h4>{c['name']}</h4>
                <p>{c['service']}</p>
                <button class="cta-btn cta-outline">Book Service</button>
            </div>
            """, unsafe_allow_html=True)


# --------------------------------------------------
# PAGE: LOGIN
# --------------------------------------------------
elif st.session_state.page == "login":
    st.subheader("🔐 Sign In")

    name = st.text_input("Full Name")
    role = st.selectbox("Role", ["Entrepreneur", "Mentor", "Customer"])

    if st.button("Login"):
        st.session_state.user = {"name": name, "role": role}
        st.session_state.page = "home"
        st.success("Logged in successfully!")
