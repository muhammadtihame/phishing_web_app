import streamlit as st
import pickle

# Load your trained model
model = pickle.load(open('phishing.pkl', 'rb'))

st.set_page_config(page_title="Phishing Detection", layout="centered")

st.title("Phishing Website Detection App")

# ----------- INPUT FIELDS ------------

# Input 1: URL Length
url_length = st.number_input("Enter URL Length:")

# Input 2: Does it have HTTPS?
https_option = st.selectbox("Does it have HTTPS?", ("Yes", "No"))
https_value = 1 if https_option == "Yes" else 0

# ------------ PREDICT BUTTON ------------
if st.button("Predict"):
    # Pass inputs to model
    prediction = model.predict([[url_length, https_value]])

    # Output result
    if prediction == 1:
        st.error("Warning! This is a Phishing Website.")
    else:
        st.success("This is a Legitimate Website.")
