import streamlit as st

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="AscendX",
    layout="wide",
)

# -------------------------------
# Session state init (IMPORTANT)
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------------------
# CSS (NAV ONLY – DOES NOT TOUCH HOME BODY)
# -------------------------------
st.markdown(
    """
    <style>
    /* NAV BAR CONTAINER */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 16px;
        margin-bottom: 30px;
    }

    /* NAV BUTTON BASE */
    div[data-testid="stButton"] > button {
        min-width: 150px;
        height: 44px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: 500;
        border: none;
        background: transparent;
        color: #4b5563;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
    }

    /* HOVER */
    div[data-testid="stButton"] > button:hover {
        background: #6B4C7A;
        color: white;
    }

    /* ACTIVE PAGE */
    .active-nav button {
        background: #6B4C7A !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------
# NAV BAR
# -------------------------------
st.markdown('<div class="nav-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Home"):
        st.session_state.page = "home"
    if st.session_state.page == "home":
        st.markdown('<div class="active-nav"></div>', unsafe_allow_html=True)

with col2:
    if st.button("Mentors"):
        st.session_state.page = "mentors"
    if st.session_state.page == "mentors":
        st.markdown('<div class="active-nav"></div>', unsafe_allow_html=True)

with col3:
    if st.button("Clients"):
        st.session_state.page = "clients"
    if st.session_state.page == "clients":
        st.markdown('<div class="active-nav"></div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# PAGE ROUTER
# -------------------------------
if st.session_state.page == "home":
    # ⚠️ DO NOT TOUCH YOUR HOME BODY
    # Your existing home content stays EXACTLY as-is
    st.markdown("## Connect. Mentor. Grow Together.")
    st.write(
        "Find mentors who share your business interests, "
        "discover clients near you, and build meaningful connections."
    )

elif st.session_state.page == "mentors":
    st.markdown("## Mentors")
    st.info("Mentor listing page coming next (cards + filters).")

elif st.session_state.page == "clients":
    st.markdown("## Clients")
    st.info("Client discovery page coming next.")
