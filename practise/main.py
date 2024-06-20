import streamlit as st
import pandas as pd
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
