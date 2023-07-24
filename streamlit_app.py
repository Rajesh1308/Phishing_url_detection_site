import streamlit as st
import pandas as pd
import pickle
import Feature_extraction_new as feature
from urllib.parse import urlparse

with open("model_svm_rbf.pkl", "rb") as f:
        model_svm_rbf = pickle.load(f)


st.title("Phishing Website Detection")
st.subheader("Enter the URL to check if it is a phishing website or not")
url = st.text_input("URL")
if st.button("Predict"):
    if urlparse(url).scheme not in ['http', 'https']:
         st.warning("Please enter a valid URL with scheme (http:// or https://)")
    else:
        st.write("Extracting Features...")
        st.write("This takes few seconds...")
        y_for_test = feature.get_data_set(url)
        val = y_for_test.fillna(0)
        pred = model_svm_rbf.predict(val)
        st.subheader("Prediction:")
        if pred[0] == 1:
            res = "Legitimate website"
        elif pred[0] == -1:
            res = "Phished website"
        st.success(res)