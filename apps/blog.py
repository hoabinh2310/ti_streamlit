import streamlit.components.v1 as components
import datetime
import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
from apps.func import *
from annotated_text import annotated_text


# Path: streamlit\ti_streamlit\apps\blog.py

if 'well_done' not in st.session_state:
    st.session_state.well_done = False
    
st.title("Blog")

blog1, blog2, blog3 = st.columns((1,1,1))

# df = pd.read_csv('data/blog_summary.csv')
# title = df['title'].tolist()
# summary = df['summary'].tolist()
# date = df['date'].tolist()
# print(len(df))

ner, title = get_ner()

for i in range(5):
    ct = st.container()
    with ct:
        blog = ct.columns((1,1,1))
        for j in range(3):
            with blog[j]:
                st.write("")
                st.write("")
                st.markdown(f'<h4 style="text-align: center;background-color:#dbe6f4;border-radius:2%;padding:15px">{title[i*3+j].title()}</h3>', unsafe_allow_html=True)
                st.write("")
                annotated_text(*ner[i*3+j])
                # blog[j].markdown(f'<p style="text-align: center;">{date[i*3+j]}</p>', unsafe_allow_html=True)
                # st.markdown(f'<p style="text-align:left;background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
                                #  {annotated_text(*ner[i*3+j])} </p>', unsafe_allow_html=True)
            # blog[j].markdown(f"### {title[i*3+j]}")
            # blog[j].markdown(summary[i*3+j])



# with blog1:
#     for i in range(5):
#         st.markdown(f'<h4 style="text-align: center;">{title[i].title()}</h3>', unsafe_allow_html=True)
#         st.markdown(f'<p style="text-align:left;background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
#                         {summary[i]} </p>', unsafe_allow_html=True)

# with blog2:
#     for i in range(5,10):
#         st.markdown(f'<h4 style="text-align: center;">{title[i].title()}</h3>', unsafe_allow_html=True)
#         st.markdown(f'<p style="text-align:left;background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
#                         {summary[i]} </p>', unsafe_allow_html=True)

# with blog3:
#     for i in range(10,15):
#         st.markdown(f'<h4 style="text-align: center;">{title[i].title()}</h3>', unsafe_allow_html=True)
#         st.markdown(f'<p style="text-align:left;background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
#                         {summary[i]} </p>', unsafe_allow_html=True)

