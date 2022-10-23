import streamlit.components.v1 as components
import datetime
import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
from apps.func import get_content_dt, get_cve_topk


# Path: streamlit\ti_streamlit\apps\blog.py

if 'well_done' not in st.session_state:
    st.session_state.well_done = False
    
st.title("Blog")

blog1, blog2, blog3 = st.columns((1,1,1))

df = pd.read_csv('data/blog_summary.csv')
title = df['title'].tolist()
summary = df['summary'].tolist()

with blog1:
    for i in range(5):
        st.markdown(f'<h4 style="text-align: center;">{title[i].title()}</h3>', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align:left;background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
                        {summary[i]} </p>', unsafe_allow_html=True)

with blog2:
    for i in range(5,10):
        st.markdown(f'<h4 style="text-align: center;">{title[i].title()}</h3>', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align:left;background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
                        {summary[i]} </p>', unsafe_allow_html=True)

with blog3:
    for i in range(10,15):
        st.markdown(f'<h4 style="text-align: center;">{title[i].title()}</h3>', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align:left;background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
                        {summary[i]} </p>', unsafe_allow_html=True)

