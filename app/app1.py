# app1.py
import streamlit as st
import pandas as pd
  
def app():
    st.image('app/data_scientist.png',use_column_width=True)
    st.title('Context')
    st.write('The demand for data scientists has been steadily increasing as the job title is often referenced as "the sexiest job of the 21st century.” \
    As students of data science, we were interested in diving into the HR analytics involving data science practitioners,\
    hence obtained a dataset from [Kaggle](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists)"\
    that includes the demographic, education, and experience information of data scientist candidates for a company. ')
    st.title('About the Dataset')
    st.write('This dataset includes 14 features of 19093 data scientists such as demographics, education, and experience level\
    and is divided into test and train, the latter containing an additional column of “whether the candidate is currently looking\
    for a job” which we’ve utilized to create an interactive sidebar feature to collect the user’s input responses to predict their\
    likelihood of looking for a new job at the moment, based on the provided data set. We’d like to inform the users and our site\
    visitors that the provided dataset is quite imbalanced on several demographical facets, hence in cases when the probability,\
    we’ve made sure to output a qualifying statement: “we’ll need more information to guess your next move!”')

    # dictionary with list object in values
    st.title('What the Dataset Looks Like')
    details = {
        'Column' : ['enrollee_id','city','city_development_index','Gender',\
                    'relevent_experience','enrolled_university','education_level',\
                    'major_discipline','experience','company_size','company_type',\
                    'last_new_job','training_hours','target'],
        'Description' : ['Unique ID for candidate',\
                         'City code',\
                         'Developement index of the city (scaled)',\
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
    
      
    train = pd.read_csv('app/aug_train.csv')
    st.write(train)
        

   
