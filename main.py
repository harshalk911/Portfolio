import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Harshal Korade")
    content = """Hi! I'm a passionate Python developer with a strong focus on building clean, 
    scalable, and efficient web applications. I specialize in backend development, integrating 
    databases, and crafting dynamic user experiences with modern tools and frameworks.
    """
    st.info(content)
