import streamlit as st
import io
from PIL import Image

import google.generativeai as genai
genai.configure(api_key="AIzaSyCJA1hPNHpbNmU89AAiyAqTqPhZ7Pa_1Dk")
model = genai.GenerativeModel("gemini-pro-vision")

st.title("สัตว์ สิ่งของ ผลไม้ ดอกไม้")
ch = st.selectbox("เลือกหมวด",
                 ("สัตว์","สิ่งของ","ผลไม้","ดอกไม้"))
                  
prompt = ch + " ในภาพนี้คืออะไร"

img_file = st.file_uploader("เปิดไฟล์ภาพ")

if img_file is not None:
    imagefile = io.BytesIO(img_file.read())
    img = Image.open(imagefile)
    st.image(img_file,channels="BGR")

if st.button("ประมวลผล"):
    try:
        response = model.generate_content([img,prompt])
        st.text(response.text)
    except:
        st.text("no response")




    



