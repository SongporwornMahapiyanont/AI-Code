import streamlit as st

col1,col2,col3 = st.columns(3)

col1.button("เปิดไฟ")
col2.button("เปิดพัดลม",help="ร้อนจังเลย")
col3.button("เปิดแอร์",help="ขอเย็นๆ")
