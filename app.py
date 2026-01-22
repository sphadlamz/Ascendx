import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AscendX",
    layout="wide"
)

# --------------------------------------------------
# GLOBAL STYLES (Base44-inspired)
# --------------------------------------------------
st.markdown("""
<style>
/* Page background */
.stApp {
    background-color: #FAF7F5;
}

/* Hero badge */
.hero-badge {
    display: inline-block;
    padding: 8px 18px;
    background: rgba(107, 78, 138, 0.12);
    color: #6B4E8A;
    border-radius: 999px;
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 30px;
}

/* Hero title */
.hero-title {
    font-size: 64px;
    font-weight: 800;
    line-height: 1.1;
    color: #1F2937;
}

.hero-title .mentor {
    color: #6B4E8A;
}

.hero-title .grow {
    color: #F2A07B;
}

/* Hero text */
.hero-text {
    font-size: 18px;
    color: #6B7280;
    max-width: 720px;
    margin-top: 20px;
    margin-bottom: 40px;
}

/* Buttons */
.primary-btn button {
    background-color: #6B4E8A !important;
    color: white !important;
    border-radius: 14px;
    padding: 14px 28px;
    font-size: 16px;
    font-weight: 600;
    border: none;
}

.secondary-btn button {
    background-color: transparent !important;
    color: #F2A07B !important;
    border: 2px solid #F2A07B !important;
    border-radius: 14px;
    padding: 14px 28px;
    font-size: 16px;
    font-weight: 600;
}

/* Button spacing fix */
div.stButton > button {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO SECTION (Centered)
# --------------------------------------------------
left, center, right = st.columns([1, 2, 1])

with center:

    # Badge
    st.markdown(
        '<div class="hero-badge">✨ Empowering Women in Business</div>',
        unsafe_allow_html=True
    )

    # Title
    st.markdown(
        """
        <div class="hero-title">
            Connect. <span class="mentor">Mentor.</span><br>
            <span class="grow">Grow Together.</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Description
    st.markdown(
        """
        <div class="hero-text">
            Find mentors who share your business interests, discover clients near you,
            and build meaningful connections with fellow women entrepreneurs.
        </div>
        """,
        unsafe_allow_html=True
    )

    # CTA Buttons
    btn1, btn2 = st.columns(2)

    with btn1:
        st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
        st.button("Find a Mentor")
        st.markdown('</div>', unsafe_allow_html=True)

    with btn2:
        st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
        st.button("Find Clients")
        st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER (Optional, clean)
# --------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<center style='color:#9CA3AF;'>Built by students • Powered by Huawei Cloud</center>",
    unsafe_allow_html=True
)
