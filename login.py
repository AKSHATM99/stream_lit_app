import streamlit as st
from db import verify

def login():
    st.header("Log In")
    user_name = st.text_input('User Name', key="LoginPageKeyUserName")
    password = st.text_input('Password',type="password")
    login =  st.button("LogIn")
    if login:
        verify(user_name, password)
