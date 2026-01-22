import streamlit as st

# Mock data (temporary)
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


st.set_page_config(
    page_title="AscendX",
    layout="centered"
)

st.title("AscendX")

menu = st.radio(
    "Menu",
    ["Home", "Register", "Find Mentors", "Training"]
)

if menu == "Home":
    st.subheader("Empowering Youth & Women Entrepreneurs")
    st.write("Built on Huawei Cloud")

elif menu == "Register":
    st.subheader("Register")

    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    role = st.selectbox("Role", ["Entrepreneur", "Mentor", "Customer"])

    if st.button("Register"):
        st.success("Registered successfully (API coming next)")

elif menu == "Find Mentors":
    st.subheader("Nearby Mentors")

    for mentor in MENTORS:
        with st.container():
            st.markdown(f"### 👤 {mentor['name']}")
            st.write(f"Industry: {mentor['industry']}")
            st.write(f"Location: {mentor['location']}")

            if st.button(f"Book session with {mentor['name']}", key=mentor["id"]):
                st.success(f"Session request sent to {mentor['name']}")
                st.info("📩 SMS & Email confirmation sent")

elif menu == "Training":
    st.subheader("Entrepreneur Training")

    st.markdown("### 📘 How to Start a Small Business")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

    st.markdown("### 📗 Financial Basics for Entrepreneurs")
    st.video("https://www.w3schools.com/html/movie.mp4")

