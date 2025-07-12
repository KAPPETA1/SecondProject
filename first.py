import streamlit as st
import spacy 
from textblob import TextBlob
st.title("First streamli app")

nlp=spacy.load("en_core_web_sm")
text="hi how are you"
doc=nlp(text)
for token in doc:
    print(token.text,token.pos_,token.dep_)
st.title("📝 Text Box Example")

# Single-line input
name = st.text_input("Enter your name")

# Multi-line text area
user_notes = st.text_area("Write your notes here", height=200)

# Display input
if name:
    st.write(f"Hello, **{name}**!")

if user_notes:
    st.write("🗒️ Your notes:")
    st.code(user_notes)
