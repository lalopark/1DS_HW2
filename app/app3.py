# app3.py

import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objs as go
import pickle as pkle
import os.path
import streamlit as st 
import base64
import seaborn as sns
import plotly.express as px
import re




def app():
    st.title('Analysis1')
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
    df = df.replace({'education_level': 'Graduate'}, 'Undergraduate')
    df2 = train[train['last_new_job'].notna()]
    df2['last_new_job'] = df2['last_new_job'].astype(int)

    fig1 = px.histogram(train, x= 'city_development_index', nbins = 50, title='City Development Index Distribution of Candidates')
    st.plotly_chart(fig1) 
    
 
    
    fig5 = px.pie(df, names='education_level', title='Education Levels of Candiates') 
    st.plotly_chart(fig5)
       
    df_melt = train.melt(id_vars='education_level', value_vars='experience')
    box2 = px.box(df_melt, x="education_level", y="value", title='Experience Distribution by Education Level')
    st.plotly_chart(box2)
    
    df_melt_3 = train.melt(id_vars='major_discipline', value_vars='experience')
    box3 = px.box(df_melt_3, x="major_discipline", y="value", title='Experience Distribution by Major')
    st.plotly_chart(box3)

    fig2 = px.histogram(train, x= 'training_hours', nbins = 50, title='Training Hour Distribution of Candidates')
    st.plotly_chart(fig2) 
    
    group = train.groupby(['training_hours','relevent_experience']).size()
    group = group.reset_index()
    group.columns.values[2] = "count" 
    fig6 = px.line(group, x="training_hours", y="count", color="relevent_experience", title='Density Curve of Traiing Hours For Candidates With Relevant Experience vs Those Without')
    st.plotly_chart(fig6)

    fig3 = px.histogram(df, x='experience', nbins=50, title='Experience Distribution of Candidates')
    st.plotly_chart(fig3)

    fig4 = px.histogram(df2, x='last_new_job', nbins=5, title='Last New Job Distribution of Candidates')
    st.plotly_chart(fig4)
    
    
    
