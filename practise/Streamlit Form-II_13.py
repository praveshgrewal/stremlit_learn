import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center;'> User Form </h1>", unsafe_allow_html=True)
# form= st.form(key="register_form")
# form.text_input("username")
# form.form_submit_button("submit")

#with keyword
with st.form("my_form",clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name=col1.text_input("naam jo 10th mai hai wo ghr aala na likhna")
    l_name=col2.text_input("goot")
    st.text_input("Email")
    st.text_input(f"Password (koii dhang ka kade setting ka naam likh de)")
    st.text_input("ek baar or likh de ")
    
    day, month, year = st.columns(3)
    day.text_input("day")
    month.text_input("month")
    year.text_input("year")
    s_state=st.form_submit_button("dekhi jagi kar de submit")
    if s_state:
        if f_name=="" or l_name=="":
            st.error("please fill all the details")
        else:
            st.success("submitted")