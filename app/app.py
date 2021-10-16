#app.py
import app1
import app2
import app3
import app4

import streamlit as st



PAGES = {
    "About the Dataset": app1,
    "Analysis1": app2,
    "Analysis2": app4,
    "Writeup": app3
}
st.sidebar.title('Page Navigation')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

st.sidebar.title('Developer Contact')

