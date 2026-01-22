import streamlit as st

st.set_page_config(page_title="HerNetwork", layout="wide")

# -----------------------------
# SESSION STATE (Auth)
# -----------------------------
if "user" not in st.session_state:
    st.session_state.user = None

# -----------------------------
# SIDEBAR = NAVBAR
# -----------------------------
with st.sidebar:
    st.title("✨ HerNetwork")

    if st.session_state.user:
        st.write(f"👤 {st.session_state.user['name']}")

        menu = st.radio(
            "Navigation",
            ["Home", "Find Mentors", "Find Clients", "Discover"]
        )

        if st.button("🚪 Sign Out"):
            st.session_state.user = None
            st.experimental_rerun()
    else:
        menu = "Home"
        if st.button("🔐 Sign In"):
            st.session_state.user = {"name": "Demo User"}
            st.experimental_rerun()

# -----------------------------
# MAIN CONTENT (children)
# -----------------------------
st.markdown("## Page Content")

if menu == "Home":
    st.write("🏠 Home Page")

elif menu == "Find Mentors":
    st.write("🏆 Find Mentors Page")

elif menu == "Find Clients":
    st.write("🎯 Find Clients Page")

elif menu == "Discover":
    st.write("🧭 Discover Page")
