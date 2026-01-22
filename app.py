import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AscendX",
    layout="centered"
)

# --------------------------------------------------
# NAVIGATION STATE (STEP 1)
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# --------------------------------------------------
# CUSTOM CSS (Base44-inspired styling)
# --------------------------------------------------
st.markdown("""
<style>
body {
    background: #fafafa;
}

.hero-pill {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    background: #f1e9f6;
    color: #6B4C7A;
    font-size: 14px;
    font-weight: 500;
}

.hero-title {
    font-size: 56px;
    font-weight: 800;
    line-height: 1.1;
}

.hero-title span.connect { color: #111827; }
.hero-title span.mentor { color: #6B4C7A; }
.hero-title span.grow { color: #E8927C; }

.hero-subtitle {
    font-size: 18px;
    color: #4b5563;
    max-width: 720px;
    margin: 20px auto;
}

.primary-btn button {
    background: linear-gradient(to right, #6B4C7A, #8B6B9B);
    color: white;
    border-radius: 12px;
    padding: 12px 28px;
    font-size: 16px;
    border: none;
}

.secondary-btn button {
    background: white;
    color: #E8927C;
    border: 2px solid #E8927C;
    border-radius: 12px;
    padding: 12px 28px;
    font-size: 16px;
}

.card {
    padding: 20px;
    border-radius: 16px;
    background: white;
    border: 1px solid #e5e7eb;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HOME PAGE (STEP 2 & 3)
# --------------------------------------------------
if st.session_state.page == "home":

    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)

    st.markdown("<div class='hero-pill'>✨ Empowering Women in Business</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-title">
        <span class="connect">Connect.</span>
        <span class="mentor"> Mentor.</span><br>
        <span class="grow">Grow Together.</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="hero-subtitle">
        Find mentors who share your business interests, discover clients near you,
        and build meaningful connections with fellow women entrepreneurs.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # Buttons (STEP 2)
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

# --------------------------------------------------
# FIND MENTORS PAGE (STEP 4)
# --------------------------------------------------
elif st.session_state.page == "mentors":

    st.markdown("## 🤝 Find a Mentor")
    st.write("Connect with experienced women mentors near you.")

    mentors = [
        {
            "name": "Nandi Mokoena",
            "industry": "Agribusiness",
            "location": "Soweto"
        },
        {
            "name": "Thabo Khumalo",
            "industry": "Retail",
            "location": "Durban"
        }
    ]

    for mentor in mentors:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {mentor['name']}")
        st.write(f"**Industry:** {mentor['industry']}")
        st.write(f"📍 {mentor['location']}")
        if st.button(f"Request Session – {mentor['name']}"):
            st.success("Session request sent!")
            st.info("📩 SMS & Email notification will be sent via Huawei Cloud")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"

# --------------------------------------------------
# FIND CLIENTS PAGE (STEP 5)
# --------------------------------------------------
elif st.session_state.page == "clients":

    st.markdown("## 🎯 Find Clients")
    st.write("Discover local women-led businesses offering services.")

    entrepreneurs = [
        {
            "name": "Lerato Foods",
            "service": "Catering"
        },
        {
            "name": "Sipho Repairs",
            "service": "Phone & Laptop Repair"
        }
    ]

    for biz in entrepreneurs:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {biz['name']}")
        st.write(f"🛠 Service: {biz['service']}")
        if st.button(f"Book Service – {biz['name']}"):
            st.success("Booking confirmed!")
            st.info("📩 Customer & entrepreneur notified via Huawei Cloud")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"
