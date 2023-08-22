import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return st.header(response.json()[0][0]["label"])

def text_gen():
    st.header(":blue[Sentiment Analysis Model]")
    prompt = st.text_input("Enter your Sentence")
    gen = st.button(":blue[Generate]")
    if gen:
        if len(prompt)<=0:
            st.write("Please enter your Sentence")
        else:
            query({
                "inputs": prompt,
            })
