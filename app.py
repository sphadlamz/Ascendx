import streamlit as st

st.set_page_config(
    page_title="AscendLink",
    layout="mobile"
)

st.title("AscendLink")
st.subheader("Youth & Women Enterprise Empowerment Platform")

st.write("""
Connecting entrepreneurs, mentors, and customers
using Huawei Cloud.
""")

role = st.selectbox(
    "Who are you?",
    ["Entrepreneur", "Mentor", "Customer"]
)

st.success(f"Welcome, {role}!")
