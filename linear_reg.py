import streamlit as st
import os
import numpy as np
import pickle

#Loading Linear Regression Model
reg = pickle.load(open('linear_reg_model.pkl', 'rb'))

def show_linear_model_page():
    st.header("Linear Regression Model")
    age = st.slider('Age of your car?(Years)', 0, 20, 5)
    st.write("My Car is ", age, 'years old')
    km = st.slider('KiloMeters Driven?', 0, 200000, 10000)
    st.write("My Car covered ", km, 'in total')
    ok = st.button("Calculate Price :moneybag:")
    if ok:
        int_features = [int(x) for x in (km, age)]
        final_int = [np.array(int_features)]
        prediction = reg.predict(final_int)
        if int(prediction)>0:
            st.header(str(int(prediction))+ " ₹")
        else:
            st.header("Not A Good Deal")
       
