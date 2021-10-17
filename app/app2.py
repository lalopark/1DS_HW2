# app2.py

import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objs as go
import pickle as pkle
import os.path
import streamlit as st

def app():
    st.title('Analysis2')
    train = pd.read_csv('app/aug_train.csv')

    train = train.replace({'company_size': '10/49'}, '10-49')
    train = train.replace({'company_size': '<10'}, '1-9')
    train = train.replace({'company_size': '100-500'}, '100-499')
    train = train.replace({'education_level': 'Graduate'}, 'Undergraduate')
    train = train.replace({'major': 'Other'}, 'other_major')
    train = train.fillna(value={'gender':'Female'})
    train = train.fillna('Other')

    train.rename(columns={'gender': 'Gender', 'Education_level': 'Education_level'})
    
    
    
    #10/16
    train = pd.read_csv('app/aug_train.csv')
    exp_clean = list()
    nj_clean = list()
    for i in train['experience'].astype(str):
        exp_clean.append(''.join(e for e in i if e.isalnum()))
    for i in train['last_new_job'].astype(str): 
        nj_clean.append(''.join(e for e in i if e.isalnum()))

    train['experience'] = exp_clean
    train['last_new_job'] = nj_clean

    train['experience'] = pd.to_numeric(train['experience'], errors='coerce')
    train['last_new_job'] = pd.to_numeric(train['last_new_job'], errors='coerce')

    df = train[train['experience'].notna()]
    df['experience'] = df['experience'].astype(int)
    df2 = train[train['last_new_job'].notna()]
    df2['last_new_job'] = df2['last_new_job'].astype(int)
    df2 = df2.replace({'gender': 'Other'}, 'Female')
    df2 = df2.fillna(value={'gender':'Female'})

    imbalance = df2.groupby('gender').count().reset_index()
    imbalance = imbalance.rename(columns={'enrollee_id': 'Count','gender':'Gender'})
 
    c = alt.Chart(imbalance, title = 'Gender Imbalanced Data').mark_bar().encode(
        x="Gender",
        y="Count"
    ).properties(width=600, height=400).configure_axisX(labelAngle=45).interactive()
    
    st.altair_chart(c)
    
    final = df2.groupby(['gender','last_new_job','experience']).count().reset_index()
    fig = px.scatter(x=list(final['experience']), y=list(final['last_new_job']),
                color=final["gender"],size = final['major_discipline'])

    st.plotly_chart(fig)
    
    
    
    
    
    
    Gender = ['Female','Male']
    selected_gender = st.multiselect('Gender', Gender, Gender)

    Education = ['Phd','Master','Undergraduate','High School']
    selected_education = st.multiselect('Education_level', Education, Education)

    df_selected = train[(train.gender.isin(selected_gender) & train.education_level.isin(selected_education))]

    # Education_level bar graph
    st.header('Take a closer look at the dataset based on gender and education levels. Try clicking the filters above!')
    st.write('Data Dimension: ' + str(df_selected.shape[0]) + ' rows and ' + str(df_selected.shape[1]) + ' columns.')
    university_df = df_selected.groupby(['enrolled_university']).count().reset_index()[['enrolled_university','enrollee_id']].rename(columns={'enrollee_id':'Count'})
    #st.dataframe(university_df)
    #s = df_selected['enrolled_university'].value_counts()
    #st.bar_chart(s)

    c = alt.Chart(university_df, title = 'Enrolled University Type').mark_bar().encode(
        x="enrolled_university",
        y="Count"
    ).properties(width=600, height=400).configure_axisX(labelAngle=45).interactive()
    st.altair_chart(c)


    # major_discipline bar graph
    major_df = df_selected.groupby(['major_discipline']).count().reset_index()[['major_discipline','enrollee_id']].rename(columns={'enrollee_id':'Count'})
    #st.dataframe(major_df)

    c = alt.Chart(major_df, title = 'Major' ).mark_bar().encode(
        x="major_discipline",
        y="Count"
    ).properties(width=600, height=400).configure_axisX(labelAngle=45).interactive()
    st.altair_chart(c)


    company_size_type = df_selected.groupby(['company_size','company_type']).count().reset_index()[['company_size','company_type','enrollee_id']].rename(columns={'enrollee_id':'Count'})
    #st.dataframe(company_size_type)
    categoryNames = ['1-9','10-49','50-99','100-499','500-999','1000-4999','5000-9999','10000+' ]
    c = alt.Chart(company_size_type, title = 'Company Size').mark_bar().encode(
        alt.X("company_size",sort=categoryNames),
        y="Count",
        color = 'company_type'
    ).properties(width=600, height=400).configure_axisX(labelAngle=45).interactive()
    st.altair_chart(c)
    
    



  

