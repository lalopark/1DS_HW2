# app2.py

import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
import plotly.express as px
import plotly.graph_objs as go
import pickle as pkle
import os.path
import streamlit as st

def app():
    st.title('Analysis1')
    train = pd.read_csv('aug_train.csv')

    st.write("Here's our first attempt at using data to create a table:")
    train = train.replace({'company_size': '10/49'}, '10-49')
    train = train.replace({'company_size': '<10'}, '1-9')
    train = train.replace({'company_size': '100-500'}, '100-499')
    train = train.replace({'education_level': 'Graduate'}, 'Undergraduate')
    train = train.fillna(value={'gender':'Female'})
    train = train.fillna('other')
    
    st.write(train)

    train.rename(columns={'gender': 'Gender', 'Education_level': 'Education_level'})
    
    Gender = ['Female','Male']
    selected_gender = st.multiselect('Gender', Gender, Gender)

    Education = ['Phd','Master','Undergraduate','High School']
    selected_education = st.multiselect('Education_level', Education, Education)

    df_selected = train[(train.gender.isin(selected_gender) & train.education_level.isin(selected_education))]

    # Education_level bar graph
    st.header('Display Entire Dataset of Selected Gender(s) & Education Level(s)')
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

    


    '''
    scatter = alt.Chart(df_selected).mark_circle().encode(
        alt.X('major_discipline', scale=alt.Scale(zero=False),
                axis=alt.Axis(grid=False)),
        alt.Y('training_hours', scale=alt.Scale(zero=False),
                axis=alt.Axis(grid=False)),
        color='gender').properties(width=600, height=400)
    st.altair_chart(scatter)
    '''

