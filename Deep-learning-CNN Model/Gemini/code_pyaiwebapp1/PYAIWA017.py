import streamlit as st
import cv2

img = cv2.imread("bird.jpg")
(h,w,c) = img.shape

st.image(img, caption="นก",channels="BGR")
st.text("ภาพนี้ กว้าง " + str(w) + " สูง " + str(h))
