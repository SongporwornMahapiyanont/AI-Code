import streamlit as st

import google.generativeai as genai
genai.configure(api_key="xxx")
model = genai.GenerativeModel("gemini-pro")

st.title("gemini-pro")
prompt = st.text_input("ป้อน prompt: ")

try:
    response = model.generate_content(prompt)
    st.text(response.text)
except:
    st.text("no response")




    



