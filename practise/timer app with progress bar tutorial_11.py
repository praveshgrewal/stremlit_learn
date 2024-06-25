import streamlit as st
import pandas as pd
import time as ts
from datetime import time

def converter(value):
   m,s,mm = value.split(":")
   t_s= int(m)*60 + int(s)+ int(mm)/1000
   return t_s

val = st.time_input("set timer",value=time(0,0,0))
if str(val) == "00:00:00":
    st.write("please set timer")
else:
   sec = converter(str(val))
   bar = st.progress(0)
   per=sec/100
   progress = st.empty()
   for i in range(100):
     bar.progress(i+1)
     progress.write(str(i+1) + "%")
     ts.sleep(per)
