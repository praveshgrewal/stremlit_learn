import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

x= np.linspace(0,10,100)
st.markdown("<h1 style='text-align: center;'> Streamlit slidbar </h1>", unsafe_allow_html=True)
st.sidebar.write("hello world")



st.markdown("<h1 style='text-align: center;'> Streamlit charbar </h1>", unsafe_allow_html=True)
opt=st.sidebar.radio("select graph",options=['line', 'bar','h-bar'])
if opt=='line':

    fig=plt.figure()
    plt.style.use('ggplot')

    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x),'--')

    st.pyplot(fig)

elif opt=='bar':
    fig=plt.figure()
    plt.style.use('ggplot')
    plt.bar(x,np.sin(x))
    st.pyplot(fig)

elif opt=='h-bar':
    fig=plt.figure()
    plt.style.use('ggplot')
    plt.barh(x,np.sin(x))
    st.pyplot(fig)