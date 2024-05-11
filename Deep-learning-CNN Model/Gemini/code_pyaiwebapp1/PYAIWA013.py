import streamlit as st

name = st.text_input("กรุณาป้อน ชื่อ : ")
#name = st.text_input("กรุณาป้อนชื่อ : ","พิมพ์ตรงนี้นะครับ")
surname = st.text_input("กรุณาป้อน นามสกุล : ")

st.text("สวัสดีครับ คุณ " + name + ' ' + surname)


    



