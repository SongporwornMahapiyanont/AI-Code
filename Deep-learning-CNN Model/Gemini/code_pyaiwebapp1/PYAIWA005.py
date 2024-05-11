import streamlit as st

a = 40 # --> '40'
st.text("อุณหภูมิ " + str(a) + " องศาเซลเซียส")

b = 10.83
st.text("ระยะทาง " + str(b) + " เซนติเมตร")

c = 3.45
st.text("น้ำหนัก " + format(c,'.3f') + " กิโลกรัม")

d = "มะละกอ"
st.text("คุณชอบทาน" + d)

