import streamlit as st
import requests
from bs4 import BeautifulSoup
#web scrapper in streamlit
st.title("web scrapper in streamlit")
#st.image('https://images.unsplash.com/photo-1529485726363-95c8d62f656f')

with st.form("search"):
    keyword= st.text_input("Search")
    button= st.form_submit_button("Submit")
    if button:
        page=requests.get(f"https://unsplash.com/search/photos/{keyword}")
        soup=BeautifulSoup(page.content, 'html.parser')
        rows=soup.find_all('img', class_='n3VNCb')
        print(len(rows))



