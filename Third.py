import streamlit as st

# Get screen width and height using Streamlit's experimental get_window_size
window_size = st.get_window_size() if hasattr(st, "get_window_size") else None
if window_size:
    width, height = window_size["width"], window_size["height"]
    st.write(f"Screen width: {width}px, height: {height}px")
else:
    st.info("Streamlit does not provide direct access to screen width and height. Try using st.markdown with custom JS if needed.")

st.title("Streamlit Tabs Example")
st.markdown(
    """
    <style>
        .stTabs [data-baseweb="tab-list"] {
            background-color: #eaf1fb;
            border-radius: 10px 10px 0 0;
            padding: 0.5rem 0.5rem 0 0.5rem;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 18px;
            font-weight: 600;
            color: #4F8BF9;
            padding: 0.5rem 1.5rem;
            border-radius: 8px 8px 0 0;
            margin-right: 2px;
        }
        .stTabs [aria-selected="true"] {
            background: #4F8BF9 !important;
            color: #fff !important;
        }
        .stApp {
            background: linear-gradient(120deg, #c5c9c6ff 0%, #b3b4b5ff 100%);
        }
    </style>
    """,
    unsafe_allow_html=True
)
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("Welcome to Tab 1")
    st.write("This is the content of Tab 1.")

with tab2:
    st.header("Welcome to Tab 2")
    st.write("This is the content of Tab 2.")

with tab3:
    st.header("🌄 Welcome to Tab 3")
    st.markdown(
        """
        <div style='
            background-color: #f0f4fa;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(79,139,249,0.08);
            margin-bottom: 16px;
        '>
            <span style='font-size:22px; font-weight:bold; color:#4F8BF9;'>
                Discover a beautiful view below!
            </span>
            <p style='font-size:16px; color:#333; margin-top:8px;'>
                Enjoy this curated image from Unsplash.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        caption="A beautiful view",
        use_column_width=True
    )