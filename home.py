import streamlit as st
import requests

st.title('Taxi Fare prediction app')


distance = st.number_input('Enter the distance')

passenger_count = st.number_input('Enter the number of passengers')

button = st.button('Predict')

if button:
    url = "https://taxifare-lecture-api-684763614222.us-central1.run.app/predict"

    response = requests.post(url +f"?distance={distance}&passernger_count={passenger_count}")
    st.write(url +f"?distance={distance}&passernger_count={passenger_count}")
    st.write(response.json())
