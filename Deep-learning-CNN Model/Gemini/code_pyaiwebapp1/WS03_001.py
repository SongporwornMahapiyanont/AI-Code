import streamlit as st

import cv2
from stability_ai import text2image

api_key   = "xxx"
engine_id = "stable-diffusion-v1-6"
filename_save = "image_out.jpg"

st.title("สร้างภาพจากข้อความ")
prompt = st.text_input("ป้อน prompt ภาษาอังกฤษ: ")

if st.button("สร้างภาพ"):      
    try:
        text2image(api_key,engine_id,prompt,filename_save)
        img = cv2.imread(filename_save)
        st.image(img,channels="BGR")
    except:
        st.text("ลองใหม่อีกครั้ง")





    



