import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="AscendX | HerNetwork",
    page_icon="✨",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================
if "user" not in st.session_state:
    st.session_state.user = None

# =====================================================
# MOCK DATA (Future: Huawei GaussDB)
# =====================================================
MENTORS = [
    {
        "id": 1,
        "name": "Nandi Mokoena",
        "industry": "Agribusiness",
        "location": "Soweto",
        "lat": -26.2485,
        "lon": 27.8540
    },
    {
        "id": 2,
        "name": "Thabo Khumalo",
        "industry": "Retail",
        "location": "Durban",
        "lat": -29.8587,
        "lon": 31.0218
    }
]

ENTREPRENEURS = [
    {
        "id": 101,
        "name": "Lerato Foods",
        "service": "Catering",
        "lat": -26.2041,
        "lon": 28.0473
    },
    {
        "id": 102,
        "name": "Sipho Repairs",
        "service": "Phone & Laptop Repair",
        "lat": -29.8587,
        "lon": 31.0218
    }
]

# =====================================================
# HELPER FUNCTIONS
# =====================================================
def login_user(name, role):
    st.session_state.user = {
        "name": name,
        "role": role
    }

def logout_user():
    st.session_state.user = None
    st.experimental_rerun()

def require_login():
    if not st.session_state.user:
        st.warning("Please register or sign in to continue.")
        st.stop()

# =====================================================
# SIDEBAR (Base44 Layout Equivalent)
# =====================================================
with st.sidebar:
    st.markdown("## ✨ HerNetwork")
    st.caption("Empowering Youth & Women Entrepreneurs")

    if st.session_state.user:
        user = st.session_state.user
        st.markdown(f"**👤 {user['name']}**")
        st.markdown(f"_Role: {user['role']}_")

        st.button("🚪 Sign Out", on_click=logout_user)

        menu = st.radio(
            "Navigation",
            [
                "Home",
                "Dashboard",
                "Find Mentors",
                "Find Entrepreneurs",
                "Training"
            ]
        )
    else:
        menu = st.radio(
            "Navigation",
            [
                "Home",
                "Register / Login"
            ]
        )

# =====================================================
# MAIN CONTENT AREA
# =====================================================
st.markdown(
    """
    <style>
    .title-text {
        font-size: 36px;
        font-weight: 800;
        background: linear-gradient(90deg, #6B4C7A, #E8927C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title-text'>AscendX</div>", unsafe_allow_html=True)
st.subheader("Youth & Women Enterprise Empowerment Platform")
st.caption("Cloud-native architecture powered by Huawei Cloud")

st.markdown("---")

# =====================================================
# HOME
# =====================================================
if menu == "Home":
    st.markdown("""
    ### 🌍 The Challenge
    Youth and women entrepreneurs struggle with:
    - Access to mentors  
    - Digital skills training  
    - Customers & markets  

    ### 💡 Our Solution
    **AscendX (HerNetwork)** connects:
    - 👩🏽‍💼 Entrepreneurs  
    - 🧑🏽‍🏫 Mentors  
    - 🧑🏽‍🤝‍🧑🏽 Customers  

    Using a **scalable Huawei Cloud architecture**.
    """)

# =====================================================
# REGISTER / LOGIN
# =====================================================
elif menu == "Register / Login":
    st.subheader("📝 Register or Sign In")

    name = st.text_input("Full Name")
    role = st.selectbox("Select Role", ["Entrepreneur", "Mentor", "Customer"])

    if st.button("Continue"):
        if name:
            login_user(name, role)
            st.success(f"Welcome, {name}!")
            st.info("Authentication handled via Huawei API Gateway & FunctionGraph (demo)")
            st.experimental_rerun()
        else:
            st.error("Please enter your full name.")

# =====================================================
# DASHBOARD
# =====================================================
elif menu == "Dashboard":
    require_login()
    user = st.session_state.user

    st.subheader(f"📊 {user['role']} Dashboard")

    st.write(f"👤 Logged in as **{user['name']}**")

    if user["role"] == "Entrepreneur":
        st.success("✔ Find nearby mentors")
        st.success("✔ Book mentorship sessions")
        st.success("✔ Watch training videos")

    elif user["role"] == "Mentor":
        st.success("✔ Manage availability")
        st.success("✔ Accept mentorship bookings")

    elif user["role"] == "Customer":
        st.success("✔ Discover local entrepreneurs")
        st.success("✔ Book services")

# =====================================================
# FIND MENTORS
# =====================================================
elif menu == "Find Mentors":
    require_login()

    st.subheader("🏆 Find Mentors Near You")

    df = pd.DataFrame(MENTORS)
    st.map(df[["lat", "lon"]])

    st.markdown("---")

    for mentor in MENTORS:
        with st.container():
            st.markdown(f"### 👤 {mentor['name']}")
            st.write(f"**Industry:** {mentor['industry']}")
            st.write(f"**Location:** {mentor['location']}")

            if st.button(f"Book session with {mentor['name']}", key=f"mentor_{mentor['id']}"):
                st.success(f"Session booked with {mentor['name']}")
                st.info("📩 SMS & Email sent via Huawei Cloud (FunctionGraph + SMS API)")

# =====================================================
# FIND ENTREPRENEURS
# =====================================================
elif menu == "Find Entrepreneurs":
    require_login()

    st.subheader("🏪 Discover Local Entrepreneurs")

    df = pd.DataFrame(ENTREPRENEURS)
    st.map(df[["lat", "lon"]])

    st.markdown("---")

    for ent in ENTREPRENEURS:
        with st.container():
            st.markdown(f"### 🏪 {ent['name']}")
            st.write(f"**Service:** {ent['service']}")

            if st.button(f"Book service from {ent['name']}", key=f"ent_{ent['id']}"):
                st.success("Service booked successfully")
                st.info("📩 Customer & entrepreneur notified via Huawei Cloud")

# =====================================================
# TRAINING
# =====================================================
elif menu == "Training":
    require_login()

    st.subheader("🎥 Skills & Training")

    st.markdown("### 📘 How to Start a Small Business")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

    st.markdown("### 📗 Financial Basics for Entrepreneurs")
    st.video("https://www.w3schools.com/html/movie.mp4")

    st.info("Videos delivered via Huawei OBS & Video on Demand (demo)")

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption("© 2025 HerNetwork | Built by students using Huawei Cloud")
