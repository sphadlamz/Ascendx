import streamlit as st
import streamlit.components.v1 as components

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="AscendX",
    layout="wide"
)

# ---------------------------
# Get page from URL
# ---------------------------
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

# ---------------------------
# Global CSS (UNCHANGED)
# ---------------------------
st.markdown("""
<style>
body {
    background: #ffffff;
}

.nav-bar {
    display: flex;
    gap: 16px;
    justify-content: center;
    padding: 20px 0;
}

.nav-html-btn {
    padding: 12px 28px;
    border-radius: 18px;
    border: 1px solid #d1cfd8;
    background: #ffffff;
    color: #6b3f8c;
    font-weight: 600;
    cursor: pointer;
}

.nav-html-btn:hover {
    background: #f5f3fa;
}

.home-container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 80px 40px;
    text-align: center;
}

.home-title {
    font-size: 64px;
    font-weight: 800;
    line-height: 1.2;
}

.dark { color: #0f172a; }
.purple { color: #6b3f8c; }
.peach { color: #f2997a; }

.home-subtitle {
    margin-top: 24px;
    font-size: 18px;
    color: #475569;
    max-width: 720px;
    margin-left: auto;
    margin-right: auto;
}

.home-actions {
    margin-top: 48px;
    display: flex;
    justify-content: center;
    gap: 24px;
}

.cta-btn {
    padding: 18px 36px;
    border-radius: 16px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
}

.cta-primary {
    background: #7a5c99;
    color: #ffffff;
    border: none;
}

.cta-outline {
    background: transparent;
    color: #f2997a;
    border: 2px solid #f2997a;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Top Navigation (FIXED)
# ---------------------------
components.html("""
<div class="nav-bar">
    <button class="nav-html-btn" onclick="location.search='?page=home'">Home</button>
    <button class="nav-html-btn" onclick="location.search='?page=mentors'">Find Mentors</button>
    <button class="nav-html-btn" onclick="location.search='?page=clients'">Find Clients</button>
    <button class="nav-html-btn" onclick="location.search='?page=login'">Sign In</button>
</div>
""", height=80)

# ---------------------------
# HOME PAGE
# ---------------------------
# --- HOME PAGE ---
if st.session_state.page == "home":

    st.markdown("""
    <div class="hero-container">

        <div class="hero-pill">✨ Empowering Women in Business</div>

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

    # BUTTONS (Streamlit-native)
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Find a Mentor", use_container_width=True):
            st.session_state.page = "mentors"
            st.rerun()

    with col2:
        if st.button("Find Clients", use_container_width=True):
            st.session_state.page = "clients"
            st.rerun()
