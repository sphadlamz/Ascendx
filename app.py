import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AscendX",
    layout="centered"
)

# --------------------------------------------------
# NAVIGATION STATE
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# --------------------------------------------------
# BASE44-STYLE CSS
# --------------------------------------------------
st.markdown("""
<style>
/* Header */
.header {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid #eee;
    padding: 12px 0;
}

.header-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.logo {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 800;
    font-size: 20px;
}

.logo-badge {
    width: 36px;
    height: 36px;
    border-radius: 12px;
    background: linear-gradient(135deg, #6B4C7A, #E8927C);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}

.nav-btn button {
    background: transparent;
    border: none;
    font-size: 14px;
    padding: 8px 14px;
    border-radius: 10px;
    color: #4b5563;
}

.nav-btn button:hover {
    background: #f3f4f6;
    color: #6B4C7A;
}

/* Hero */
.hero-pill {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    background: #f1e9f6;
    color: #6B4C7A;
    font-size: 14px;
}

.hero-title {
    font-size: 56px;
    font-weight: 800;
    line-height: 1.1;
}

.hero-title .mentor { color: #6B4C7A; }
.hero-title .grow { color: #E8927C; }

.hero-sub {
    font-size: 18px;
    color: #4b5563;
    max-width: 720px;
    margin: 20px auto;
}

/* Cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER (OPTION 1A)
# --------------------------------------------------
st.markdown("<div class='header'>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns([3, 4])

    with col1:
        st.markdown("""
        <div class="logo">
            <div class="logo-badge">✨</div>
            AscendX
        </div>
        """, unsafe_allow_html=True)

    with col2:
        nav1, nav2, nav3 = st.columns(3)

        with nav1:
            if st.button("Home", key="nav_home"):
                st.session_state.page = "home"

        with nav2:
            if st.button("Find Mentors", key="nav_mentors"):
                st.session_state.page = "mentors"

        with nav3:
            if st.button("Find Clients", key="nav_clients"):
                st.session_state.page = "clients"

st.markdown("</div>", unsafe_allow_html=True)

st.write("")  # spacing below header

# --------------------------------------------------
# HOME
# --------------------------------------------------
if st.session_state.page == "home":

    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.markdown("<div class='hero-pill'>✨ Empowering Women in Business</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-title">
        Connect. <span class="mentor">Mentor.</span><br>
        <span class="grow">Grow Together.</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="hero-sub">
        Find mentors who share your business interests, discover clients near you,
        and build meaningful connections with fellow women entrepreneurs.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🤝 Find a Mentor"):
            st.session_state.page = "mentors"
    with c2:
        if st.button("🎯 Find Clients"):
            st.session_state.page = "clients"

# --------------------------------------------------
# FIND MENTORS
# --------------------------------------------------
elif st.session_state.page == "mentors":

    st.markdown("## 🤝 Find a Mentor")

    mentors = [
        {"name": "Nandi Mokoena", "industry": "Agribusiness", "location": "Soweto"},
        {"name": "Thabo Khumalo", "industry": "Retail", "location": "Durban"}
    ]

    for m in mentors:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {m['name']}")
        st.write(f"Industry: {m['industry']}")
        st.write(f"📍 {m['location']}")
        if st.button(f"Request session – {m['name']}"):
            st.success("Session request sent")
            st.info("📩 Notification via Huawei Cloud")
        st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# FIND CLIENTS
# --------------------------------------------------
elif st.session_state.page == "clients":

    st.markdown("## 🎯 Find Clients")

    businesses = [
        {"name": "Lerato Foods", "service": "Catering"},
        {"name": "Sipho Repairs", "service": "Phone & Laptop Repair"}
    ]

    for b in businesses:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {b['name']}")
        st.write(f"Service: {b['service']}")
        if st.button(f"Book service – {b['name']}"):
            st.success("Booking confirmed")
            st.info("📩 Huawei Cloud notification sent")
        st.markdown("</div>", unsafe_allow_html=True)
