import streamlit as st

text1 = "ข้อความที่ 1 ชิดซ้าย (แสดงด้วย st.text)"
st.text(text1)

text2 = "ข้อความที่ 2 ชิดซ้าย (แสดงด้วย st.markdown)"
st.markdown(f'<p style="text-align:left">{text2}</p>', unsafe_allow_html=True)

text3 = "ข้อความที่ 3 ชิดขวา (แสดงด้วย st.markdown)"
st.markdown(f'<p style="text-align:right">{text3}</p>', unsafe_allow_html=True)

text4 = "ข้อความที่ 4 กึ่งกลาง (แสดงด้วย st.markdown)"
st.markdown(f'<p style="text-align:center">{text4}</p>', unsafe_allow_html=True)
