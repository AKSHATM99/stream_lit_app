import streamlit as st
from image_model import show_image_model_page
from linear_reg import show_linear_model_page

st.write(':flag-in:')
page = st.sidebar.selectbox("Select Model :blush:", ("Deep Learning Model", "Linear Regression Model"))

if page == "Linear Regression Model":
    show_linear_model_page()
else:
    show_image_model_page()