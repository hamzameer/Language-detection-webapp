import requests
import streamlit as st

input_text = st.text_input("Enter some text and it will be classified into a langauge")

if st.button("Submit"):

    # Inputs to ML model
    inputs = {
        "text": input_text
        }
       
    # Posting inputs to ML API
    response = requests.post(f"http://https://backend-aoeymj3qqa-wl.a.run.app/predict", json=inputs, verify=False)
    json_response = response.json()

    prediction = json_response["language"]  

    st.write(f"The language is **{prediction}!**")