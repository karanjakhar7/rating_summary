from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import random
import time

import streamlit as st
from langchain.llms import OpenAI

print(random.randint(0,1000))

# RUBRICS = {
#     'Critical Thinking': ['Information and Discovery', 'Interpretation and Analysis', 'Reasoning', 'Problem-solving/ Solution finding', 'Self-reflection'],
#     'Creativity': ['Idea Generation and Expression', 'Openness and Courage to explore', 'Creative Production and Innovation', 'Self-Reflection/Agency'],
#     'Collaboration': ['Responsibility and Initiative', 'Cooperation, Flexibility and Responsiveness', 'Common goal or shared purpose', 'Self-Reflection/ Agency'],
#     'Communication': ['Being Clear, Complete, Concise &Confident', 'Listening & Feedback', 'Trust building', 'Self reflection'],
# }

RUBRICS = {
    "Critical Thinking": {
        "Information and Discovery": "<score>",
        "Interpretation and Analysis": "<score>",
        "Reasoning": "<score>",
        "Problem-solving/ Solution finding": "<score>",
        "Self-reflection": "<score>",
    },
    "Creativity": {
        "Idea Generation and Expression": "<score>",
        "Openness and Courage to explore": "<score>",
        "Creative Production and Innovation": "<score>",
        "Self-Reflection/Agency": "<score>",
    },
    "Collaboration": {
        "Responsibility and Initiative": "<score>",
        "Cooperation, Flexibility and Responsiveness": "<score>",
        "Common goal or shared purpose": "<score>",
        "Self-Reflection/ Agency": "<score>",
    },
    "Communication": {
        "Being Clear, Complete, Concise &Confident": "<score>",
        "Listening & Feedback": "<score>",
        "Trust building": "<score>",
        "Self reflection": "<score>",
    },
}
MAX_RATING = 4

st.title("Rating Summary")
st.write('This is a demo of the Rating Summary app. The app is currently under development.')


def get_feedback():
    print('processing')
    res = data
    return res


def clear_text():
    
    for state in st.session_state:
        if type(st.session_state[state])== int: # in isinstance(st.session_state[state], int) bool values also gets picked up
            st.session_state[state] = 1
        elif isinstance(st.session_state[state], str):
            st.session_state[state] = ''

data = {}
additional = {}
with st.form(key='my_form'):
    additional['Name'] = st.text_input('Name:', key='Name')
    additional['Gender'] = st.text_input('Gender:', key='Gender')

    cols = st.columns(len(RUBRICS))
    i = 0
    for rubric, criteria in RUBRICS.items():
        col = cols[i]
        with col:
            st.subheader(rubric)
            data_dict = {}
            for criterion, _ in criteria.items():
                data_dict[criterion] = st.number_input(f'{criterion}', min_value=1, max_value=MAX_RATING, value=1, step=1, key=f'{criterion}')
            data[rubric] = data_dict
        i += 1

    additional['Other observations'] = st.text_area('Other observations:', key='Other observation')

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

prompt = """You are a leadership instructor and you have just finished an assessment. You want to give feedback to your students. The feedback is based on the rubrics below. \n
            You can rate each criterion from 1 to 4. \n
            1 means the student is not good at this criterion, 4 means the student is very good at this criterion. \n
            You should provide two outputs: Assessment of Leadership (What the student is good at) and Assessment for Leadership (what are the things student can improve). 
            You only have the abovementioned information about the student. Nothing else. \n
            About the student: \n
            Name: {name} \n
            Gender: {gender} \n
            RUBRICS and SCORES:{data} \n
            Here is an example of feedback:
            Assessment of Leadership: Sharayu displays utmost commitment to his team and always envisions the end-result of collaborative work. He consistently fulfills roles and responsibilities with little prompting, monitors progress of group's efforts and communicates well with his team.
            Assessment for Leadership: Sharayu can enhance his critical thinking skills by actively engaging in the analysis and planning part of solving a problem. Exercises like brainstorming, creating story boards for academic as well as extra-curricular projects in a group setting would enhance his problem solving skills. Assuming positions of leadership would add to his leadership experience and further enhance his confidence in sharing his ideas openly.
            """.format(name= 'Karan', gender='Male', data=data)
st.write(repr(prompt))


MAX_OUTPUT_LENGHT = 100