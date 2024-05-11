import streamlit as st
import cv2

img = cv2.imread("zebra.jpg")

st.image(img, caption='ม้าลาย',channels="BGR") #OpenCV BGR ลองเปลี่ยนเป็น RGB
