import streamlit as st
import cv2

img1 = cv2.imread("zebra.jpg")
img2 = cv2.imread("duck.jpg")
img3 = cv2.imread("bird.jpg")

col1, col2, col3 = st.columns(3)

col1.image(img1, caption='ม้าลาย',channels="BGR")
col2.image(img2, caption='เป็ด',channels="BGR")   
col3.image(img3, caption='นก',channels="BGR")
