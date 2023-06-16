from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import random
import time

import streamlit as st
from langchain.llms import OpenAI

print(random.randint(0,1000))

st.title("🦜🔗 Rating Summary")
st.write('This is a demo of the Rating Summary app. The app is currently under development.')

num_ratings = 15
num_cols = 5

def get_feedback():
    print('processing')
    res = data
    return res


def clear_text():
    for key in data.keys():
        if key == 'other_obv':
            continue
        st.session_state[key] = 0
    st.session_state["other_obv"] = ''

data = {}

with st.form(key='my_form'):
    cols = st.columns(num_cols)

    for i in range(1, num_ratings+1):
        col = cols[(i % num_cols) -1]
        with col:
            data[f'rating{i}'] = st.number_input(f'Insert rating {i}', min_value=0, max_value=10, value=0, step=1, key=f'rating{i}')

        if i % num_cols==0:
            cols = st.columns(num_cols)

    data['other_obv'] = st.text_area('Other observations:', key='other_obv')

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