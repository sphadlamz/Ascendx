# --------------------------------------------------
# PAGE: HOME
# --------------------------------------------------
if st.session_state.page == "home":

    st.html("""
    <style>
    .btn-link {
        display: block;
        width: 100%;
        text-align: center;
        text-decoration: none;
        padding: 14px 24px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 12px;
        cursor: pointer;
    }

    .btn-primary {
        background-color: #6f4aa6;
        color: white;
        border: none;
    }

    .btn-secondary {
        background-color: transparent;
        color: #f28c6b;
        border: 2px solid #f28c6b;
    }
    </style>

    <div class="hero-container">

        <div class="hero-pill">
            ✨ Empowering Women in Business
        </div>

        <div class="hero-title">
            <span class="connect">Connect.</span>
            <span class="mentor"> Mentor.</span><br>
            <span class="grow">Grow Together.</span>
        </div>

        <p class="hero-subtitle">
            Find mentors who share your business interests, discover clients near you,
            and build meaningful connections with fellow women entrepreneurs.
        </p>

        <div class="cta-wrapper">

            <a href="?page=mentors" class="btn-link btn-primary">
                Find a Mentor
            </a>

            <div style="height:14px;"></div>

            <a href="?page=clients" class="btn-link btn-secondary">
                Find Clients
            </a>

        </div>

    </div>
    """)
