import streamlit as st
import pickle
import numpy as np

# Load the model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Phishing Website Detection App")

# Take user input
url_length = st.number_input("Enter URL Length:")
has_https = st.selectbox("Does it have HTTPS?", [0, 1])

# Button to predict
if st.button('Predict'):
    features = np.array([[url_length, has_https]])  # Example features
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("Phishing Website Detected!")
    else:
        st.success("Safe Website!")
