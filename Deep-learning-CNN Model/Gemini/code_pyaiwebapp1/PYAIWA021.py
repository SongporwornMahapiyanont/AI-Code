import streamlit as st
import cv2
import numpy as np

img_file = st.file_uploader("เปิดไฟล์ภาพ")

if img_file is not None:
    print(img_file)
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    (h,w,c) = img.shape
    st.image(img ,channels="BGR")
    st.text("ชื่อไฟล์ : " + img_file.name)
    st.text("ขนาดภาพ : " + str(w) + "," + str(h) + "," + str(c) )
    
