import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Harshal Korade")
    content = """Hi! I'm a passionate Python developer with a strong focus on building clean, 
    scalable, and efficient web applications. I specialize in backend development, integrating 
    databases, and crafting dynamic user experiences with modern tools and frameworks.
    """
    st.info(content)

st.subheader("Below you can find some apps I have built in Python. Feel free to contact me.")

col3 , empty_col, col4 = st.columns([1.5,0.5,1.5])

data = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
