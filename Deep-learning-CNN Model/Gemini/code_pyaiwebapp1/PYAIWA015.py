import streamlit as st

ch = st.selectbox("กรุณาเลือกจังหวัด",
                 ("นครปฐม","สุพรรณบุรี","เลย","ระนอง"))

st.text("คุณเลือกจังหวัด " + ch)

