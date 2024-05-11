import streamlit as st

import google.generativeai as genai
genai.configure(api_key="xxx")
model = genai.GenerativeModel("gemini-pro")

st.title("ขอโค้ดโปรแกรม")
ch = st.selectbox("เลือกภาษา",
                 ("Python","C","C++","Java"))

text_in = st.text_input("ป้อนโค้ดที่ต้องการ: ")

prompt = "ขอโค้ดโปรแกรม "+ text_in + " ที่เขียนด้วยภาษา " + ch
st.text(prompt)

if st.button("ขอโค้ด"):
    try:
        response = model.generate_content(prompt)
        st.text(response.text)
    except:
        st.text("no response")




    



