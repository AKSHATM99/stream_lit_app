import streamlit as st
from image_model import show_image_model_page
from linear_reg import show_linear_model_page
from login import login
from signup import signup
from streamlit_autorefresh import st_autorefresh
from text_gen import text_gen

if "logged_in" in st.session_state:
    st.title(':blue[Ai Verse :computer:]')
    st.write(':flag-in:')
    st.write("Welcome :blush:" , st.session_state['user_name'])
    page = st.sidebar.selectbox("Select Model :blush:", ("Deep Learning Model", "Linear Regression Model", "Sentiment Analysis Model"))
    if page == "Linear Regression Model":
        show_linear_model_page()
    elif page == "Sentiment Analysis Model":
        text_gen()
    else:
        show_image_model_page()
    col1, col2, col3 = st.columns(3)
    if col3.button(':blue[LogOut]'):
        st.warning("Logged out Successfully....")
        del st.session_state["logged_in"]
        st_autorefresh(interval=500, limit=200, key="logout_refresh")

elif 'signed_in' in st.session_state or 'logged_in' not in st.session_state:
    st.title(':blue[Ai Verse :computer:]')
    st.write(':flag-in:')
    page1 = st.sidebar.selectbox("Login :blush:", ("Login", "New User ? Sign Up...."))
    if page1 == "Login":
        login()
    else:
        signup()








