# app1.py
import streamlit as st
import pandas as pd
  
def app():
    st.image('app/data_scientist.png',use_column_width=True)
    st.title('Context')
    st.write('The demand for data scientists has been steadily increasing as the job title is often referenced as "the sexiest job of the 21st century.” \
    As students of data science, we were interested in diving into the HR analytics involving data science practitioners,\
    hence obtained a dataset from Kaggle (https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists)\
    that includes the demographic, education, and experience information of data scientist candidates for a company. ')
    st.title('About Data')
    st.write('This dataset includes 14 features of 19093 data scientists such as demographics, education, and experience level\
    and is divided into test and train, the latter containing an additional column of “whether the candidate is currently looking\
    for a job” which we’ve utilized to create an interactive sidebar feature to collect the user’s input responses to predict their\
    likelihood of looking for a new job at the moment, based on the provided data set. We’d like to inform the users and our site\
    visitors that the provided dataset is quite imbalanced on several demographical facets, hence in cases when the probability,\
    we’ve made sure to output a qualifying statement: “we’ll need more information to guess your next move!”')

    # dictionary with list object in values
    details = {
        'Column' : ['enrollee_id','city','city_development_index','Gender',\
                    'relevent_experience','enrolled_university','education_level',\
                    'major_discipline','experience','company_size','company_type',\
                    'last_new_job','training_hours'],
        'Description' : ['Unique ID for candidate',\
                         'City code',\
                         'Developement index of the city (scaled)'
                         'Gender of candidate',\
                         'Relevant experience of candidate',\
                         'Type of University course enrolled if any',\
                         'Education level of candidate',\
                         'Education major discipline of candidate',\
                         'Candidate total experience in years',\
                         "Number of employees in current employer's company",\
                         'Type of current employer',\
                         'Difference in years between previous job and current job',\
                         'Completed training hours',\
                         'Whether the candidate is currently looking for a job']}
    
      
    # creating a Dataframe object 
    df = pd.DataFrame(details)
    st.write(df)

    st.write("Data Source [link](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists)")
    
             
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
    st.write(group)
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
        st.sidebar.success('Your probability of getting data scientist position is ', round(float(val)*100,3))
        


        

   
