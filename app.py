import streamlit as st

st.markdown("""
<style>
.home-hero {
    min-height: 75vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: radial-gradient(
        circle at top,
        rgba(243, 232, 255, 0.6),
        rgba(255, 255, 255, 1) 60%
    );
}

.home-hero-inner {
    max-width: 900px;
    text-align: center;
    padding: 40px 20px;
}

.home-title {
    font-size: 64px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 20px;
}

.home-title .dark { color: #111827; }
.home-title .purple { color: #6B4C7A; }
.home-title .peach { color: #F09A7A; }

.home-subtitle {
    font-size: 18px;
    color: #6b7280;
    max-width: 720px;
    margin: 0 auto 40px auto;
    line-height: 1.6;
}

.home-actions {
    display: flex;
    justify-content: center;
    gap: 24px;
}
</style>
""", unsafe_allow_html=True)


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
/* ================================
   HOME HERO (NEW)
================================ */
.home-hero {
    min-height: 75vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: radial-gradient(
        circle at top,
        rgba(243, 232, 255, 0.6),
        rgba(255, 255, 255, 1) 60%
    );
}

.home-hero-inner {
    max-width: 900px;
    text-align: center;
    padding: 40px 20px;
}

.home-title {
    font-size: 64px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 20px;
}

.home-title .dark {
    color: #111827;
}

.home-title .purple {
    color: #6B4C7A;
}

.home-title .peach {
    color: #F09A7A;
}

.home-subtitle {
    font-size: 18px;
    color: #6b7280;
    max-width: 720px;
    margin: 0 auto 40px auto;
    line-height: 1.6;
}

.home-actions {
    display: flex;
    justify-content: center;
    gap: 24px;
    flex-wrap: wrap;
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
# --------------------------------------------------
# PAGE: HOME
# --------------------------------------------------
if st.session_state.page == "home":

    # -------- HERO SECTION --------
    st.markdown("""
    <div style="text-align:center; padding-top:60px; padding-bottom:40px;">

        <div class="hero-pill">
            ✨ Empowering Women in Business
        </div>

        <div class="hero-title">
            <span class="connect">Connect.</span>
            <span class="mentor"> Mentor.</span><br>
            <span class="grow">Grow Together.</span>
        </div>

        <p class="hero-subtitle">
            Find mentors who share your business interests, discover clients near you,
            and build meaningful connections with fellow women entrepreneurs.
        </p>

    </div>
    """, unsafe_allow_html=True)

    # -------- CTA BUTTONS --------
    st.markdown("<div style='max-width:520px; margin:0 auto;'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
        if st.button("Find a Mentor"):
            st.session_state.page = "mentors"
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
        if st.button("Find Clients"):
            st.session_state.page = "clients"
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")  # spacing
