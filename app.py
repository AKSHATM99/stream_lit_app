import streamlit as st
from image_model import show_image_model_page
from linear_reg import show_linear_model_page
from login import login
from signup import signup
from streamlit_autorefresh import st_autorefresh


if "logged_in" in st.session_state:
    st_autorefresh(interval=1500, limit=20, key="key1")
    st.write(':flag-in:')
    page = st.sidebar.selectbox("Select Model :blush:", ("Deep Learning Model", "Linear Regression Model"))
    if page == "Linear Regression Model":
        show_linear_model_page()
    else:
        show_image_model_page()
    col1, col2, col3 = st.columns(3)
    if col3.button('LogOut'):
        del st.session_state["logged_in"]
        st_autorefresh(interval=1500, limit=20, key="key2")

elif 'logged_in' not in st.session_state:
    st_autorefresh(interval=1500, limit=20, key="key3")
    st.write(':flag-in:')
    page1 = st.sidebar.selectbox("Login :blush:", ("Login", "New User ? Sign Up...."))
    if page1 == "Login":
        login()
    else:
        signup()








