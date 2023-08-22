import streamlit as st
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from PIL import ImageFile,Image, ImageOps
ImageFile.LOAD_TRUNCATED_IMAGES = True

#Loading & Compiling Model 

model = keras.models.load_model('BikeVsCar_Model(91.5).h5')

def show_image_model_page():
    st.header(":blue[Deep Learning Model (Bike Vs Car)]")
    #File Uploader
    file = st.file_uploader("Upload the image to be classified \U0001F447", type=["jpg", "png"])
    # Uploading and Transforming Image to array for feeding to model
    if file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        size = (100,100)    
        image = ImageOps.fit(image, size)
        x = np.asarray(image)
        x = np.expand_dims(x,axis=0)
        images = np.vstack([x])
        val = model.predict(images)
        if val<0.5:
            st.header("The image is classified as 'Bike' :bike:")
        else:
            st.header("The image is classified as 'Car' :car:")
    

