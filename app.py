from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import random
import time

import streamlit as st
from langchain.llms import OpenAI

print(random.randint(0,1000))

st.title("🦜🔗 Rating Summary")
st.write('This is a demo of the Rating Summary app. The app is currently under development.')

def get_feedback():
    print('processing')
    res = f"Rating 1: {rating1}, Rating 2: {rating2}, Rating 3: {rating3}, Rating 4: {rating4}, Rating 5: {rating5}, Rating 6: {rating6}, Rating 7: {rating7}, Rating 8: {rating8}, Rating 9: {rating9}, Rating 10: {rating10}, Other observations: {other_obv}"
    return res

def clear_text():
    st.session_state["rating1"] = 0
    st.session_state["rating2"] = 0
    st.session_state["rating3"] = 0
    st.session_state["rating4"] = 0
    st.session_state["rating5"] = 0
    st.session_state["rating6"] = 0
    st.session_state["rating7"] = 0
    st.session_state["rating8"] = 0
    st.session_state["rating9"] = 0
    st.session_state["rating10"] = 0
    st.session_state["other_obv"] = ''


with st.form(key='my_form'):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        rating1 = st.number_input('Insert rating 1', min_value=0, max_value=10, value=0, step=1, key='rating1')
    with col2:
        rating2 = st.number_input('Insert rating 2', min_value=0, max_value=10, value=0, step=1, key='rating2')
    with col3:
        rating3 = st.number_input('Insert rating 3', min_value=0, max_value=10, value=0, step=1, key='rating3')
    with col4:
        rating4 = st.number_input('Insert rating 4', min_value=0, max_value=10, value=0, step=1, key='rating4')
    with col5:
        rating5 = st.number_input('Insert rating 5', min_value=0, max_value=10, value=0, step=1, key='rating5')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        rating6 = st.number_input('Insert rating 6', min_value=0, max_value=10, value=0, step=1, key='rating6')
    with col2:
        rating7 = st.number_input('Insert rating 7', min_value=0, max_value=10, value=0, step=1, key='rating7')
    with col3:
        rating8 = st.number_input('Insert rating 8', min_value=0, max_value=10, value=0, step=1, key='rating8')
    with col4:
        rating9 = st.number_input('Insert rating 9', min_value=0, max_value=10, value=0, step=1, key='rating9')
    with col5:
        rating10 = st.number_input('Insert rating 10', min_value=0, max_value=10, value=0, step=1, key='rating10')
 

    other_obv = st.text_area('Other observations:', key='other_obv')

    # st.form_submit_button(label='Submit', on_click=get_feedback)
    submit_button = st.form_submit_button(label='Submit')
    # st.form_submit_button("Reset", on_click=clear_text)

st.button("Reset", on_click=clear_text)

if submit_button:
    res_block = st.empty()
    res_block.write('processing...')
    res = get_feedback()
    res_block.write(res)


# st.button("clear text input", on_click=clear_text)