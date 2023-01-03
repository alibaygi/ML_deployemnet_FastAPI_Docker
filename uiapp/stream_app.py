import streamlit as st
import requests, json

st.header("This a social network ads prediction")
#input_section
st.markdown("---")
st.subheader("Number input")
with st.container():
    age = st.number_input("How old are you?")
    salary = st.number_input("Please write in your yearly income")
    sub_button = st.button("Submit")

    if sub_button:
        ml_model_input = {
                'age': age,
                'salary': salary}
        st.json(ml_model_input)

        ##post request use jupyter notebook
        headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        }

        response = requests.post('http://127.0.0.1:8000/predict', headers=headers, json=ml_model_input)
        st.write(response.text)
#response = requests.post('http://127.0.0.1:8080/query', 
     #data=ml_model_input)

#streamlit run stream_app.py