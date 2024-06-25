import streamlit as st
import pandas as pd

import time  # This is the module that contains the sleep function
from datetime import datetime
tabela = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)
st.markdown("""
<style>.st-emotion-cache-6q9sum.ef3psqc4
            {
            visibility: hidden;
            
            }
.st-emotion-cache-ch5dnh.ef3psqc5 
            {
            visibility: hidden;
            
            }
            
            
            </style>
""", unsafe_allow_html=True)
#text elements
st.write("Hello, World!")
st.subheader("This is a subheader")
st.header("This is a header")
st.text("This is a text")
st.markdown("# This is")
st.markdown("----")
#link
st.markdown("[This is a link](https://www.google.com)")
st.caption("This is a caption")
st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k ''')
json = '''{
    "name": "John",
    "age": 30,
    "city": "New York"
}'''
st.json(json)
code='''import streamlit as st'''
st.code(code, language='python')

#swiss army knife of stramlit is write function
st.write("## H2")
#metric function
st.metric(label= "wind speed", value="120ms⁻¹", delta="-10ms⁻¹")
#table and dataframes function
st.table(tabela)
st.dataframe(tabela)
#media widgets of stramlit
st.image("img.png",caption="this is confsuion matrix",width=400)
#audio
st.audio("Zaroori Tha.mp3")
#video
st.video("video.mp4")

#removing stramlit hamburger $ footer
st.markdown("----")

#v8 of streamlit
st.header("basic interacive widgets of streamlit---")

def CHANGE():
    print(st.session_state.checker)
state= st.checkbox("checkbox", value=True, on_change=CHANGE, key="checker")
# if state:
#     st.write("welcome")
# else:
#    st.write("Bye")

#radio button
radio_btn = st.radio("college", ["NSTI DDN", "NSTI Kanpur", "NSTI Patna"])
print(radio_btn)

#button
def on_click(): 
    print("clicked")
btn  =st.button("click me", on_click=on_click)
print(btn)

#select box
select_box = st.selectbox("select", ["one", "two", "three"])
print(select_box)

#multiselect
multi_select = st.multiselect("multiselect", ["one", "two", "three"])
print(multi_select)


st.markdown("----")
#File Uploader Widget of Streamlit | Complete Streamlit Python Course | Streamlit Tutorial 9

st.title("upload files")
image= st.file_uploader("upload", type=["csv", "txt", "pdf", "png", "jpg", "jpeg", "gif"], accept_multiple_files=True)
if image is not None:
    st.image(image)


#Some More Interactive Widgets | Complete Streamlit Python Course | Streamlit Tutorial 10

st.markdown("----")
#slider
slider = st.slider("slider", min_value=0, max_value=10)
print(slider)

#select slider
select_slider = st.select_slider("select_slider", ["one", "two", "three"])
print(select_slider)

#text input
text_input = st.text_input("text_input",  key="text_input",max_chars=20)
print(text_input)

#text area
val = st.text_area("course description")
print(val)

#number input
num = st.number_input("number_input")
print(num)

#date input
date = st.date_input("enter your best date")
print(date)

#time input
time = st.time_input("time_input")
print(time)

#Timer App With Progress Bar | Complete Streamlit Python Course | Streamlit Tutorial 11

st.markdown("----")

bar = st.progress(0)
for i in range(10):
 
    bar.progress((i+1)*10)
    time.sleep(0.1)












