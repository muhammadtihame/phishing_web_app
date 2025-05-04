import streamlit as st
import pickle
from urllib.parse import urlparse

# Load the trained model
model = pickle.load(open('phishing.pkl', 'rb'))

st.set_page_config(page_title="Phishing Detection", layout="centered")

st.title("Phishing Website Detection App")

# ----------- INPUT FIELD ------------
url_input = st.text_input("Enter the URL (e.g., https://example.com):")

# ------------ PREDICT BUTTON ------------
if st.button("Predict"):
    if url_input:
        try:
            # Extract features from the URL
            parsed_url = urlparse(url_input)
            
            # Feature 1: URL Length
            url_length = len(url_input)
            
            # Feature 2: Check for HTTPS
            https_value = 1 if parsed_url.scheme == "https" else 0
            
            # Pass features to model
            prediction = model.predict([[url_length, https_value]])
            
            # Output result
            if prediction == 1:
                st.error("Warning! This is a Phishing Website.")
            else:
                st.success("This is a Legitimate Website.")
                
        except Exception as e:
            st.error(f"Error processing URL: {str(e)}")
    else:
        st.warning("Please enter a URL to predict.")

# ----------- CREDIT TEXT ------------
st.markdown("<p style='text-align: center; font-size: 14px;'>CREATED BY MOHAMMAD TIHAME</p>", unsafe_allow_html=True)
