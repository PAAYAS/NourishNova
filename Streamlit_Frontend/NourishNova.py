import streamlit as st
from PIL import Image
import base64

st.set_page_config(
    page_title="NourishNova",
    page_icon="🥗",
    layout="wide",
)

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("Streamlit_Frontend/image.jpg")
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.write("# Welcome to NourishNova 🥗")
st.write("## Empowering you to make nutritious choices")
st.sidebar.success("Select a recommendation from above")

st.markdown(
    """
    An Application for nutrition advice that uses Scikit-Learn, FastAPI, and Streamlit and a content-based approach.
    """
)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
