import streamlit as st

text1 = "ข้อความที่ 1 Hello"
st.markdown(f'<p style="color:#355f22;font-size:15px;">{text1}</p>', unsafe_allow_html=True)

text2 = "ข้อความที่ 2 สุขสันต์วันเกิด"
st.markdown(f'<p style="color:#00ff00;font-size:100%;">{text2}</p>', unsafe_allow_html=True)

text3 = "ข้อความที่ 3 สวัสดีครับ"
st.markdown(f'<p style="color:#ccff00;font-size:150%;">{text3}</p>', unsafe_allow_html=True)

text4 = "ข้อความที่ 4 ยินดีที่ได้รู้จักครับผม"
st.markdown(f'<p style="background-color:#2244cc;color:#55ff55;font-size:24px;">{text4}</p>', unsafe_allow_html=True)

text5 = "ข้อความที่ 5 การเขียนโปรแกรมภาษา Python"
st.markdown(f'<p style="background-color:#005555;color:#ffffff;font-size:150%;text-align:center">{text5}</p>', unsafe_allow_html=True)
