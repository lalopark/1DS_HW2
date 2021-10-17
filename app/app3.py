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
    st.title('Analysis2')
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

    fig1 = px.histogram(train, x= 'city_development_index', nbins = 50, title='City Development Index Distribution of Candidates')
    st.plotly_chart(fig1) 

    fig2 = px.histogram(train, x= 'training_hours', nbins = 50, title='Training Hour Distribution of Candidates')
    st.plotly_chart(fig2) 

    fig3 = px.histogram(df, x='experience', nbins=50, title='Experience Distribution of Candidates')
    st.plotly_chart(fig3)

    fig4 = px.histogram(df2, x='last_new_job', nbins=5, title='Last New Job Distribution of Candidates')
    st.plotly_chart(fig4)

    fig5 = px.pie(df, names='education_level', title='Education Levels of Candiates') 
    st.plotly_chart(fig5)

    group = train.groupby(['training_hours','relevent_experience']).size()
    group = group.reset_index()
    group.columns.values[2] = "count" 

    fig6 = px.line(group, x="training_hours", y="count", color="relevent_experience", title='Density Curve of ')
    st.plotly_chart(fig6)
