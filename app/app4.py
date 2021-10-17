# app4.py

import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objs as go
import pickle as pkle
import os.path
import streamlit as st

def app():
    st.title('Writeup')
    
    st.write('We created several different visualizations of the data set from both a macro and micro lens by\
    first illustrated the general statistical distributions of the data scientist candidate population in terms\
    of city development index, training hour, experience, latest jobs, and education levels (in Analysis 1 Tab),\
    then drilling down to a gender and education level-specific breakdowns to see if there are any noticeable employment\
    trends among groups of different gender identities and academic achievements. The City Development Indices of the cities\
    that the candidates reside in are extremely left-skewed, with the median at 0.86 with an overwhelming majority of residents\
    residing in cities with well-established Infrastructure, Waste Management, Health, Education, and City Product, as defined by\
    the United Nations. The specific country/regional information wasn’t provided in the dataset, so the developers would refrain\
    from making potentially biased assumptions, but it’s interesting to note that there’s a spike at 0.62 with a moderately large\
    group of candidates residing in less developed cities. Our box plot distributions of CDI by Education Level show that Masters,\
    Graduates, and PhD’s are highly centered around cities with high CDI’s, while high school and primary school grads are scattered\
    towards lower CDI’s with slightly more outliers. We hypothesize that candidates in developing cities may have access to online/open-source\
    material that can supplement or replace formal training in DS, hence the supply in the job market.')

    st.write('60% of the dataset are graduate students, with 60% having Graduate Degrees, 22.8% with Undergraduate, 2.15% with PhDs\
    and 10.5% with high school degrees. The developers found this distribution quite jarringly different from the job market situation\
    in the U.S., where closely 50-60% of the data scientist job applicants hold Master’s degrees or higher, so we deemed it a factor highly\
    dependent on the region/continent, which is unknown. The years of experience by education level is as expected with PhD’s and Master’s\
    students having the upper bound of 20> years, followed by Undergraduate degree holders, then High School and Primary Schoolers. Since Data\
    Scientists used to be primarily PhD’s or academic scholars, it’s not surprising that those groups have more experiences than others.\
    The experience distribution by major was quite contrary to our hypothesis - that STEM degree holders will have more YoE on average - with \
    all disciplines having pretty much equivalent distributions.')

    st.write('We must note that our dataset’s intrinsically imbalanced in terms of the candidates’ experience and gender, with nearly ~40% of the\
    candidates having 20+ years of work experience as a Data Scientist. Another limitation that the dataset had was its ambiguity in certain\
    columns, including training hours, which the developers assumed as the # of hours formally trained as a data scientist apart from general\
    work experience. This information would have been more meaningful if it were the number of hours per week spent on training oneself as a\
    better Data Professional, but since it isn’t, the more relevant work experiences as a Data Scientist, the longer the training hours, hence\
    the apparent correlation between having relevant work experience and higher training hours.')

    st.write('Last New Job distribution was quite interesting, with 60% of the candidates only having worked at their current job for less than a year.\
    Given that DS’s are predominantly hired in tech companies or at tech functions, it’s not surprising that frequent job switches are common\
    and not necessarily frowned upon, compared to more traditional industries.')

    st.write('We include two gender-related distributions before deep-diving into it in Analysis 2, as the dataset has 1.5x more male than female candidates,\
    it was hard to recognize the data points that represent female data scientists in Distribution of Data Scientists by Experience and Last New Job.\
    In almost all cases, the number of male data scientists is much higher than the female data scientists, female data scientists points were covered.\
    This graph showed that the respondents who have worked for their previous company for 4 years tended to have longer working experience.\
    On the other hand, the ones who have shorter working experience have changed their positions or jobs more often.')

    st.write('To classify the data scientists by their gender and education level, we added two drop-down menus, so the users can easily select\
    the data that matches with a certain condition and only use it to create plots. Using these two options, we created three-bar plots\
    which show the distribution of data scientists by their enrolled university types, majors, and company types. The majority of the data\
    scientists in the given data set are not currently enrolled in university. However, most Ph.D.-level data scientists answered that they\
    are currently enrolled in university. Also, the proportion of data scientists who are currently attending university full-time was much\
    higher in the female data scientists group than in the male group.')

    st.write('In the major graph, as was expected, the majority of data scientists studied STEM majors regardless of gender,\
    and those who did not attend university are classified as ‘other’ in the major graph. The number of data scientists who studied Arts\
    during their undergrad was the lowest in this distribution graph.')

    st.write('Lastly, to find which type of companies hire data scientists the most, we drew a graph that shows the company type and size\
    that the respondents are currently working for. According to their answers, the majority works for small private firms regardless of gender.\
    However, when we selected only Ph.D.-level data scientists, the result was different. The proportion of respondents\
    who work for the public sector has increased.')

