import streamlit as st
from db import verify
from streamlit_autorefresh import st_autorefresh

def login():
    st.header("Log In")
    user_name = st.text_input('User Name', key="LoginPageKeyUserName")
    password = st.text_input('Password',type="password")
    login =  st.button("LogIn")
    if login:
        verify(user_name, password)
    st_autorefresh(interval=500, limit=200, key="login_refresh")
