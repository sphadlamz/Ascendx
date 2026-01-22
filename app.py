import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AscendX",
    layout="centered"
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "user" not in st.session_state:
    st.session_state.user = None

# -----------------------------
# MOCK DATA (Maps to GaussDB)
# -----------------------------
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

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def login_user(name, role):
    st.session_state.user = {
        "name": name,
        "role": role
    }

def require_login():
    if not st.session_state.user:
        st.warning("Please register or login first")
        st.stop()

# -----------------------------
# APP HEADER
# -----------------------------
st.title("🚀 AscendX")
st.subheader("Youth & Women Enterprise Empowerment Platform")
st.write("Built with Huawei Cloud Architecture")

# -----------------------------
# MENU
# -----------------------------
menu = st.radio(
    "Menu",
    [
        "Home",
        "Register / Login",
        "Dashboard",
        "Find Mentors",
        "Find Entrepreneurs",
        "Training"
    ]
)

# -----------------------------
# HOME
# -----------------------------
if menu == "Home":
    st.markdown("""
    ### 🌍 Problem
    Youth and women entrepreneurs struggle to access:
    - Mentorship
    - Skills training
    - Customers
    
    ### 💡 Solution
    AscendX connects entrepreneurs, mentors, and customers
    using a cloud-native Huawei architecture.
    """)

# -----------------------------
# REGISTER / LOGIN
# -----------------------------
elif menu == "Register / Login":
    st.subheader("Register or Login")

    name = st.text_input("Full Name")
    role = st.selectbox("Role", ["Entrepreneur", "Mentor", "Customer"])

    if st.button("Continue"):
        if name:
            login_user(name, role)
            st.success(f"Welcome {name} ({role})")
            st.info("User registration handled via Huawei API Gateway & FunctionGraph")
        else:
            st.error("Please enter your name")

# -----------------------------
# DASHBOARD
# -----------------------------
elif menu == "Dashboard":
    require_login()
    user = st.session_state.user

    st.subheader(f"{user['role']} Dashboard")
    st.write(f"👤 Logged in as: **{user['name']}**")

    if user["role"] == "Entrepreneur":
        st.write("✅ Find nearby mentors")
        st.write("✅ Book mentorship sessions")
        st.write("✅ Watch training content")

    elif user["role"] == "Mentor":
        st.write("✅ Manage availability")
        st.write("✅ Accept mentorship requests")

    elif user["role"] == "Customer":
        st.write("✅ Discover local entrepreneurs")
        st.write("✅ Book services")

# -----------------------------
# FIND MENTORS (MAP + BOOKING)
# -----------------------------
elif menu == "Find Mentors":
    require_login()
    st.subheader("Nearby Mentors")

    df = pd.DataFrame(MENTORS)
    st.map(df[['lat', 'lon']])

    st.markdown("---")

    for mentor in MENTORS:
        with st.container():
            st.markdown(f"### 👤 {mentor['name']}")
            st.write(f"Industry: {mentor['industry']}")
            st.write(f"Location: {mentor['location']}")

            if st.button(f"Book session with {mentor['name']}", key=f"mentor_{mentor['id']}"):
                st.success(f"Session booked with {mentor['name']}")
                st.info("📩 SMS & Email notification sent via Huawei Cloud")

# -----------------------------
# FIND ENTREPRENEURS (CUSTOMERS)
# -----------------------------
elif menu == "Find Entrepreneurs":
    require_login()
    st.subheader("Nearby Entrepreneurs")

    df = pd.DataFrame(ENTREPRENEURS)
    st.map(df[['lat', 'lon']])

    st.markdown("---")

    for ent in ENTREPRENEURS:
        with st.container():
            st.markdown(f"### 🏪 {ent['name']}")
            st.write(f"Service: {ent['service']}")

            if st.button(f"Book service from {ent['name']}", key=f"ent_{ent['id']}"):
                st.success("Service booked successfully")
                st.info("📩 Customer & entrepreneur notified via Huawei Cloud")

# -----------------------------
# TRAINING (OBS + VOD)
# -----------------------------
elif menu == "Training":
    require_login()
    st.subheader("Entrepreneur Training")

    st.markdown("### 📘 How to Start a Small Business")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

    st.markdown("### 📗 Financial Basics for Entrepreneurs")
    st.video("https://www.w3schools.com/html/movie.mp4")

    st.info("Training videos delivered via Huawei OBS & Video on Demand")
