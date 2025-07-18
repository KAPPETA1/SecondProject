import pandas as pd
import matplotlib.pyplot as plt

import google.generativeai as genai

# Load Excel data
excel_file ="C:\\Users\\Hp\\Downloads\\SampleData.xlsx"  # Update with your Excel file path
df = pd.read_excel(excel_file)

# Perform basic analysis
summary = df.describe().to_string()

# Prepare prompt with data sample and analysis
prompt = f"Summarize the following Excel data and its analysis:\n\nData sample:\n{df.head().to_string()}\n\nAnalysis:\n{df}"

# Your API key
genai.configure(api_key="AIzaSyDNZ95groz6jTtyX6u6aUSmxGhsja_p63w")

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat()

initial_response = model.generate_content(prompt)
print("\n📊 AI Summary of Excel Data:\n", initial_response.text)
sales_by_month = df.groupby(df['OrderDate']).sum()
sales_by_month.plot(title='Monthly STotal Trend')
plt.ylabel("TOtal Sales")
plt.show()
# Start chat loop
print("\n💬 Chatbot is ready! Type 'exit' to quit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = chat.send_message(user_input+ "\n\n" + initial_response.text)
    print("Bot:", response.text)
