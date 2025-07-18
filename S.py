import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyDNZ95groz6jTtyX6u6aUSmxGhsja_p63w")
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat()

# Load Excel data
excel_file = "C:\\Users\\Hp\\Downloads\\SampleData.xlsx"
df = pd.read_excel(excel_file)

# Analysis
summary = df.describe().to_string()
sales_by_month = df.groupby('OrderDate')['Total'].sum()

# AI Summary
prompt = f"Summarize the following Excel data and its analysis:\n\nData sample:\n{df.head().to_string()}\n\nAnalysis:\n{df}"
initial_response = model.generate_content(prompt)

# Streamlit UI
st.set_page_config(page_title="Excel Data Analysis with Gemini AI", layout="wide")
st.title("📊 Excel Data Analysis with Gemini AI")

col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("Data Sample")
    st.dataframe(df.head(20), use_container_width=True)
    st.download_button(
        label="⬇️ Download Full Data as CSV",
        data=df.head(20).to_csv(index=False).encode('utf-8'),
        file_name="SampleData.csv",
        mime="text/csv"
    )

    

with col2:
    st.subheader("Monthly Sales Trend")
    fig, ax = plt.subplots()
    sales_by_month.plot(ax=ax, title='Monthly Sales Trend', color="#4F8BF9")
    ax.set_ylabel("Total Sales")
    ax.set_xlabel("Order Date")
    st.pyplot(fig)

    st.subheader("AI Summary of Excel Data")
    st.info(initial_response.text)
    # Expand Streamlit app to use full screen below code
    st.markdown(
        """
        <style>
            .main .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                max-width: 100vw;
            }
            .css-18e3th9 {
                padding-top: 0rem;
                padding-bottom: 0rem;
                max-width: 100vw;
            }
            .stApp {
                height: 100vh;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
st.markdown("---")
st.subheader("💬 Chat with Gemini AI")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_message = st.text_input("Type your question about the data:", key="user_input")
if st.button("Send") and user_message:
    response = chat.send_message(user_message)
    st.session_state.chat_history.append(("You", user_message))
    st.session_state.chat_history.append(("Bot", response.text))

for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
