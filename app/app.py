#app.py
import app1
import app2
import app3
import app4
import app5
import pandas as pd

import streamlit as st


PAGES = {
    "About the Dataset": app1,
    "Analysis1": app3,
    "Analysis2": app2,
    "Writeup": app4,
    'Developer Contact': app5
    }

st.sidebar.title('HW2 for 05839 CMU (Interactive Data Science): Page Navigation')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

 #sidebar section
# data manipulation
train = pd.read_csv('app/aug_train.csv')
train = train.replace({'company_size': '10/49'}, '10-49')
train = train.replace({'company_size': '<10'}, '1-9')
train = train.replace({'company_size': '100-500'}, '100-499')
train = train.replace({'education_level': 'Graduate'}, 'Undergraduate')
train = train.replace({'relevent_experience': 'Has relevent experience'}, 'Yes')
train = train.replace({'relevent_experience': 'No relevent experience'}, 'No')
train = train.fillna(value={'gender':'Female'})
train = train.fillna('other')

# group by 
group = train.groupby(['gender', 'relevent_experience', 'education_level', 'major_discipline', 'experience', 'last_new_job'])['target'].mean()
group = pd.DataFrame(group).reset_index()

with st.form(key ='Form1'):
    with st.sidebar:
        name = st.text_input("What is your name?")
        if name != '':
            st.sidebar.success('Thanks, '+name+'!')

        rel = st.radio('Do you have previous relevant experience as a Data Scientist?',\
                       ('Yes', 'No'))

        experience = st.sidebar.slider('How many years of experience do you have?', 0, 30) 
        if int(experience) <=1: 
            experience = '<1'
        elif int(experience) >= 20: 
            experience = '>20'
        else:
            experience = str(experience)
        last_job = st.sidebar.selectbox("How many years did you stay at your previous job?", \
                                        ['1', '2', '3', '4', '>4', 'other', 'never'])
        edu = st.sidebar.selectbox("What is the your highest degree achieved?",\
                               ['Phd', 'Masters', 'Undergraduate','High School','Primary School'])

        major = st.sidebar.selectbox("Which discipline did you major in?",\
                         ['Arts', 'Business Degree', 'Humanities','STEM','No Major', 'Other'])

        gen = st.sidebar.radio('Last but not least, what is your gender?',\
                               ('Male', 'Female', 'Other/Non-binary'))
        submitted1 = st.form_submit_button(label = 'Predict')

val = group.loc[(group['gender'] == str(gen))\
                & (group['relevent_experience'] ==str(rel))\
                & (group['education_level'] == str(edu))\
                & (group['major_discipline'] == str(major))\
                & (group['experience'] == str(experience))\
                & (group['last_new_job'] == str(last_job))]['target']

if val.empty:
    #st.write('We’ll need more information to guess your next move!')
    st.sidebar.success('We’ll need more information to guess your next move!')
else:
    #st.write('Your probability of getting data scientist position is ',round(float(val)*100,3),'%')
    st.sidebar.success('Your probability of getting data scientist position is '+ str(round(float(val)*100,3)) + '.')



