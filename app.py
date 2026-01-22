import streamlit as st

st.set_page_config(
    page_title="AscendX",
    layout="centered"
)

st.title("AscendLink")

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
    st.info("Map view will appear here (Huawei MapKit)")

elif menu == "Training":
    st.subheader("Training Videos")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
