import streamlit as st

def render_navbar():
    st.markdown("""
        <style>
        .brand {
            font-size: 26px;
            font-weight: 800;
            background: linear-gradient(90deg, #6B4C7A, #E8927C);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("### ✨ HerNetwork")

    if st.session_state.get("user"):
        user = st.session_state["user"]

        st.sidebar.markdown(f"""
        **👤 {user.get("name", "User")}**  
        _{user.get("email", "")}_
        """)

        if st.sidebar.button("🚪 Sign Out"):
            st.session_state.clear()
            st.experimental_rerun()
    else:
        st.sidebar.info("Not signed in")
