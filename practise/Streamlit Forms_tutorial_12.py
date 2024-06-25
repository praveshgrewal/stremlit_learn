import streamlit as st
import pandas as pd

st.markdown("<h1>User Form</h1>", unsafe_allow_html=True)
# form= st.form(key="register_form")
# form.text_input("username")
# form.form_submit_button("submit")

#with keyword
with st.form("my_form"):
    col1, col2 = st.columns(2)
    col1.text_input("name")
    col2.text_input("aakhri name")
    st.text_input("email")
    st.text_input("password")
    st.text_input("confirm-password")
    st.form_submit_button("dekhi jagi kar de submit")