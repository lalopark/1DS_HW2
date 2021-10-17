# app3.py

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
