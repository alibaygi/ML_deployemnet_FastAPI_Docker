import streamlit as st
import requests
import json

# Set FastAPI endpoint
endpoint = 'http://localhost:8000/predict'
# Specify this path for Dockerization to work
#endpoint = 'http://host.docker.internal:8000/predict'

st.header("The social network prediction tool")
st.write("""
The social network prediction tool is a software designed to predict customer purchase likelihood.
 By analyzing historical data and utilizing  statistical techniques the tool is able to accurately predict 
 the probability of a customer making a purchase in the future. 
 The tool takes into account various input values, such as age and salary, to determine the customer's purchase likelihood.
""")

# input_section
st.markdown("---")
st.subheader("Input values: Age and Salary")
with st.container():
    age = st.number_input("How old are you?")
    salary = st.number_input("Please write in your yearly income($)")
    sub_button = st.button("Submit")

    if sub_button:
        ml_model_input = {
            'age': age,
            'salary': salary}
        # st.json(ml_model_input)

        # post request use jupyter notebook
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        #response = requests.post('http://127.0.0.1:8000/predict', headers=headers, json=ml_model_input)
        response = requests.post(
            endpoint, headers=headers, json=ml_model_input)
        response_dict = eval(response.text)
        st.subheader("Evaluation result")
        # t.json(response_dict)
        if response_dict["class_index"] == 1:
            st.write("A potential customer")
        else:
            st.write("Not a potential customer")


# streamlit run stream_app.py
# Command to run Docker image: docker run -d -p 8501:8501 <streamlit-app-name>:latest
