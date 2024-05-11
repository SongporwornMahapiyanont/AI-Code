import streamlit as st

st.title("คำนวณพื้นที่สามเหลี่ยม")
h = st.text_input("ป้อนความสูง : ") 
b = st.text_input("ป้อนความกว้างของฐาน : ") 

if st.button("คำนวณ"): # True ทำงาน เมื่อกดปุ่ม
    try:
        a = 0.5 * float(h) * float(b)
        st.header("พื้นที่ = " + str(a))
    except:
        st.header("ไม่สามารถคำนวณได้")

    



