import streamlit as st
import pandas as pd

# Custom HTML for look and feel
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 40px 10px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            max-width: 600px;
            margin: 40px auto;
        }
        .title {
            color: #2c3e50;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 20px;
        }
    </style>
    <div class="main">
        <div class="title">Excel Data Downloader</div>
    </div>
""", unsafe_allow_html=True)

# File uploader in the center
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Preview of uploaded data:")
    st.dataframe(df)

    # Download button for the data
    st.download_button(
        label="Download Excel",
        data=uploaded_file,
        file_name="downloaded_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )