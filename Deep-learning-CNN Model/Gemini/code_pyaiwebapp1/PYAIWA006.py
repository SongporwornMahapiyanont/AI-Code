import streamlit as st

text1 = "ข้อความที่ 1 ตัวปกติ"
st.markdown(f'<p>{text1}</p>', unsafe_allow_html=True) #Fix code html

text2 = "ข้อความที่ 2 ตัวหนา"
st.markdown(f'<b>{text2}</b>', unsafe_allow_html=True)

text3 = "ข้อความที่ 3 ตัวเอียง"
st.markdown(f'<i>{text3}</i>', unsafe_allow_html=True)

text4 = "ข้อความที่ 4 ขีดเส้นใต้"
st.markdown(f'<u>{text4}</u>', unsafe_allow_html=True)

text5 = "ข้อความที่ 5 ตัวหนาและขีดเส้นใต้"
st.markdown(f'<u><b>{text5}</b></u>', unsafe_allow_html=True)

text6 = "ข้อความที่ 6 ตัวเอียงตัวหนาและขีดเส้นใต้"
st.markdown(f'<u><b><i>{text6}</i></b></u>', unsafe_allow_html=True)
