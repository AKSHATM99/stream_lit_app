import streamlit as st
from db import insert

def signup():
    st.header("Sign Up")
    user_name = st.text_input('User Name', key="SignUpPageKeyUserName")
    password = st.text_input('Password',type='password', key="SignUpPageKeyPass")
    country = st.text_input('Country')
    signup =  st.button("SignUp")
    if signup:
        insert(user_name, password, country)


