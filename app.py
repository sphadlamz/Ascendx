import streamlit as st
import pandas as pd


# --------------------------------------------------
# USER SESSION
# --------------------------------------------------
if "user" not in st.session_state:
    st.session_state.user = None
 
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
   NAV BUTTONS — STREAMLIT FIX
================================ */

/* Target Streamlit button wrapper */
.nav-btn div[data-testid="stButton"] > button {
    min-width: 160px;
    height: 44px;

    background: transparent;
    border: none;
    border-radius: 10px;

    font-size: 14px;
    font-weight: 500;
    color: #4b5563;

    cursor: pointer;
    transition: all 0.2s ease-in-out;

    /* 🔥 alignment */
    white-space: nowrap;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 18px;
}

/* Hover */
.nav-btn div[data-testid="stButton"] > button:hover {
    background: #6B4C7A;
    color: white;
}

/* Focus cleanup */
.nav-btn div[data-testid="stButton"] > button:focus {
    outline: none;
    box-shadow: none;
}

/* Container alignment */
.nav-btn {
    display: flex;
    justify-content: center;
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
   CARDS (Mentors / Clients)
================================ */
.card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 35px rgba(0,0,0,0.08);
}

/* ================================
   MAPKIT-STYLE LOCATION CARDS
================================ */
.location-card {
    background: white;
    border-radius: 14px;
    padding: 16px;
    border: 1px solid #e5e7eb;
    transition: all 0.2s ease-in-out;
}

.location-card:hover {
    border-color: #6B4C7A;
    box-shadow: 0 10px 25px rgba(107, 76, 122, 0.15);
}

/* ================================
   BUTTONS (PRIMARY)
================================ */
.primary-btn {
    background: #6B4C7A;
    color: white;
    border-radius: 12px;
    padding: 10px 18px;
    font-size: 14px;
    font-weight: 600;
    border: none;
    transition: all 0.2s ease;
}

.primary-btn:hover {
    background: #5a3e66;
}

/* ================================
   FOOTER SPACING FIX
================================ */
.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)
# --------------------------------------------------
# HEADER NAVIGATION (POLISHED)
# --------------------------------------------------
st.markdown("<div class='header'>", unsafe_allow_html=True)
with st.container():
    col1, col2, col3 = st.columns([3, 5, 4])

    # LOGO
    with col1:
        st.markdown("""
        <div class="logo">
            <div class="logo-badge">✨</div>
            AscendX
        </div>
        """, unsafe_allow_html=True)

    # NAV BUTTONS (SAME SIZE)
    with col2:
        b1, b2, b3, b4 = st.columns(4)

        with b1:
            st.markdown("<div class='nav-btn'>", unsafe_allow_html=True)
            if st.button("Home", key="nav_home"):
                st.session_state.page = "home"
            st.markdown("</div>", unsafe_allow_html=True)

        with b2:
            st.markdown("<div class='nav-btn'>", unsafe_allow_html=True)
            if st.button("Find Mentors", key="nav_mentors"):
                st.session_state.page = "mentors"
            st.markdown("</div>", unsafe_allow_html=True)

        with b3:
            st.markdown("<div class='nav-btn'>", unsafe_allow_html=True)
            if st.button("Find Clients", key="nav_clients"):
                st.session_state.page = "clients"
            st.markdown("</div>", unsafe_allow_html=True)

        with b4:
            st.markdown("<div class='nav-btn'>", unsafe_allow_html=True)
            if st.session_state.user:
                if st.button("Sign Out", key="nav_logout"):
                    st.session_state.user = None
                    st.session_state.page = "home"
            else:
                if st.button("Sign In", key="nav_login"):
                    st.session_state.page = "login"
            st.markdown("</div>", unsafe_allow_html=True)

    # USER INFO (AFTER BUTTONS)
    with col3:
        if st.session_state.user:
            st.markdown(
                f"""
                <div style="text-align:right; padding-top:6px;">
                    👤 <strong>{st.session_state.user['name']}</strong><br>
                    <span style="font-size:12px; color:#6b7280;">
                        {st.session_state.user['role']}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

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
# LOGIN
# --------------------------------------------------
elif st.session_state.page == "login":

    st.markdown("## 🔐 Sign In")

    name = st.text_input("Full Name")
    role = st.selectbox("Select your role", [
        "Entrepreneur",
        "Mentor",
        "Customer"
    ])

    if st.button("Continue"):
        if name:
            st.session_state.user = {
                "name": name,
                "role": role
            }
            st.session_state.page = "dashboard"
            st.success(f"Welcome {name}!")
        else:
            st.error("Please enter your name")

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------
elif st.session_state.page == "dashboard":

    if not st.session_state.user:
        st.session_state.page = "login"
        st.stop()

    user = st.session_state.user

    st.markdown(f"## 👋 Welcome, {user['name']}")
    st.caption(f"Role: {user['role']}")

    st.markdown("---")

    if user["role"] == "Entrepreneur":
        st.markdown("### 🚀 Entrepreneur Dashboard")
        st.write("• Find mentors")
        st.write("• Book mentorship sessions")
        st.write("• Watch training content")

        if st.button("Find Mentors"):
            st.session_state.page = "mentors"

    elif user["role"] == "Mentor":
        st.markdown("### 🎓 Mentor Dashboard")
        st.write("• Manage availability")
        st.write("• Accept mentorship requests")

        st.info("Mentor availability will be managed via Huawei FunctionGraph")

    elif user["role"] == "Customer":
        st.markdown("### 🛍 Customer Dashboard")
        st.write("• Discover entrepreneurs")
        st.write("• Book services")

        if st.button("Find Clients"):
            st.session_state.page = "clients"

# --------------------------------------------------
# FIND MENTORS
# --------------------------------------------------
if not st.session_state.user or st.session_state.user["role"] != "Entrepreneur":
    st.warning("Only entrepreneurs can access mentors.")
    st.stop()

elif st.session_state.page == "mentors":

    st.markdown("## 🤝 Find a Mentor")

    mentors = [
        {
            "name": "Nandi Mokoena",
            "industry": "Agribusiness",
            "location": "Soweto",
            "lat": -26.2485,
            "lon": 27.8540
        },
        {
            "name": "Thabo Khumalo",
            "industry": "Retail",
            "location": "Durban",
            "lat": -29.8587,
            "lon": 31.0218
        }
    ]

    st.markdown("### 📍 Mentors Near You")
    df = pd.DataFrame(mentors)
    st.map(df[['lat', 'lon']])

    for m in mentors:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {m['name']}")
        st.write(f"Industry: {m['industry']}")
        st.write(f"📍 {m['location']}")

        cols = st.columns([1, 1])
        with cols[0]:
            if st.button(f"📅 Request session", key=f"mentor_{m['name']}"):
                st.success("Session request sent")
                st.info("📩 SMS via Huawei Cloud")

        with cols[1]:
            st.caption("Location powered by Huawei MapKit")

        st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# FIND CLIENTS
# --------------------------------------------------
if not st.session_state.user or st.session_state.user["role"] != "Customer":
    st.warning("Only customers can access this page.")
    st.stop()

elif st.session_state.page == "clients":

    st.markdown("## 🎯 Find Clients")

    businesses = [
        {
            "name": "Lerato Foods",
            "service": "Catering",
            "location": "Johannesburg",
            "lat": -26.2041,
            "lon": 28.0473
        },
        {
            "name": "Sipho Repairs",
            "service": "Phone & Laptop Repair",
            "location": "Durban",
            "lat": -29.8587,
            "lon": 31.0218
        }
    ]

    st.markdown("### 📍 Entrepreneurs Near You")
    df = pd.DataFrame(businesses)
    st.map(df[['lat', 'lon']])

    for b in businesses:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {b['name']}")
        st.write(f"Service: {b['service']}")
        st.write(f"📍 {b['location']}")

        if st.button(f"🛒 Book service", key=f"biz_{b['name']}"):
            st.success("Booking confirmed")
            st.info("📩 Huawei Cloud notification sent")

        st.caption("Location powered by Huawei MapKit")
        st.markdown("</div>", unsafe_allow_html=True)

