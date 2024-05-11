import streamlit as st

label = st.empty()
label.text("คุณยังไม่ได้กดปุ่มใดๆ")

if st.button("ปุ่ม A"):
    label.text("คุณกดปุ่ม A")

if st.button("ปุ่ม B"):
    label.text("คุณกดปุ่ม B")

    



