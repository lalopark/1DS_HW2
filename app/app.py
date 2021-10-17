#app.py
import app1
import app2
import app3
import app4
import app5

import streamlit as st



PAGES = {
    "About the Dataset": app1,
    "Analysis1": app2,
    "Analysis2": app3,
    "Writeup": app4,
    'Developer Contact': app5
    
}
st.sidebar.title('Page Navigation')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

st.sidebar.title('Developer Contact')

