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
    # res_block.write(res)


# st.button("clear text input", on_click=clear_text)
sample = {
        "Critical Thinking": {
            "Information and Discovery": 2,
            "Interpretation and Analysis": 3,
            "Reasoning": 2,
            "Problem-solving/ Solution finding": 2,
            "Self-reflection": 2
        },
        "Creativity": {
            "Idea Generation and Expression": 2,
            "Openness and Courage to explore": 4,
            "Creative Production and Innovation": 1,
            "Self-Reflection/Agency": 2
        },
        "Collaboration": {
            "Responsibility and Initiative": 2,
            "Cooperation, Flexibility and Responsiveness": 3,
            "Common goal or shared purpose": 3,
            "Self-Reflection/ Agency": 3
        },
        "Communication": {
            "Being Clear, Complete, Concise &Confident": 2,
            "Listening & Feedback": 3,
            "Trust building": 2,
            "Self reflection": 2
        }
    }


prompt = """You are a leadership instructor and you have just finished an assessment. You want to give feedback to the students' parents.
            The students have been rated based of fixed set of rubrics with each criterion rated between 1 and 4.
            1 means 'Novice', 2 means 'Emerging', 3 means 'Proficient', 4 means 'Exemplary'

            You should provide two outputs: Assessment of Leadership (What the student is good at) and Assessment for Leadership (what are the things student can improve). 
            You can only use the information provided as part of the input, nothing else.

            Here is an example where student is a male named `Sharayu`. You can refer this but don't use the same feeback for all students.
            The score are delimited by four hash symbols.
            ####{sample}####
            And here is feedback provided by the instructor, delimited by four hash symbols.
            #### Assessment of Leadership: Sharayu displays utmost commitment to his team and always envisions the end-result of collaborative work. He consistently fulfills roles and responsibilities with little prompting, monitors progress of group's efforts and communicates well with his team.
            Assessment for Leadership: Sharayu can enhance his critical thinking skills by actively engaging in the analysis and planning part of solving a problem. Exercises like brainstorming, creating story boards for academic as well as extra-curricular projects in a group setting would enhance his problem solving skills. Assuming positions of leadership would add to his leadership experience and further enhance his confidence in sharing his ideas openly. ####
            Here is the scores of the student for which you have to generate feedback, delimited by tripple backticks.
            ```{data}```
            About the student: Name: {name}, Gender: {gender}
            """.format(name= 'Karan', gender='Male', data=data, sample=sample)
st.write(repr(prompt))
# st.write(data)


MAX_OUTPUT_LENGHT = 100