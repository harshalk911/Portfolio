import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.markdown(
        """
        <style>
        .fancy-header {
            color: #e91e63;
            font-size: 64px;
            font-weight: bold;
            text-shadow: 1px 1px 2px #000000;
        }
        </style>
        <div class='fancy-header'>Harshal Korade</div>
        """,
        unsafe_allow_html=True
    )

    content = """Hi! I'm a passionate Python developer with a strong focus on building clean, 
    scalable, and efficient web applications. I specialize in backend development, integrating 
    databases, and crafting dynamic user experiences with modern tools and frameworks.
    """
    st.info(content)

st.markdown(
    f"<h1 style= 'color: #1f77b4';>Below you can find some apps I have built in Python."
    f" Feel free to contact me.</h1>",
    unsafe_allow_html=True
)

col3 , empty_col, col4 = st.columns([1.5,0.5,1.5])

data = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        st.write(f"[Go to App]({row['app']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        st.write(f"[Go to App]({row['app']})")
