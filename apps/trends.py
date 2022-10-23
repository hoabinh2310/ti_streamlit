import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import numpy as np
import datetime
import pymongo

import streamlit.components.v1 as components
import datetime
import streamlit as st
import altair as alt
from apps.func import get_content_dt, get_cve_topk


st.title("Twitter Trends")

with st.container():
    g1, g2, g3 = st.columns((1,1,1))

    # cve, top3_cve = get_cve_topk(topk=3)

    top3_cve = ['cve-2022-42889', 'cve-2022-40684', 'cve-2022-37969']

    # fgdf = get_content_dt('content', top3_cve[0])
    # fgdf.to_csv('data/fgdf.csv', index=False)
    fgdf = pd.read_csv('data/fgdf.csv')
    fig = px.bar(fgdf, x = 'date', y='freq', template = 'seaborn')
    fig.update_traces(marker_color='#264653')
    fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None)
    g1.markdown(f"<h4 style='text-align: center; color: grey;'>{top3_cve[0].upper()}</h2>", unsafe_allow_html=True)
    g1.plotly_chart(fig, use_container_width=True) 
        
            
    # fcst = get_content_dt('content', top3_cve[1])
    # fcst.to_csv('data/fcst.csv', index=False)
    fcst = pd.read_csv('data/fcst.csv')
    fig = px.bar(fcst, x = 'date', y='freq', template = 'seaborn')
    fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None)
    g2.markdown(f"<h4 style='text-align: center; color: grey;'>{top3_cve[1].upper()}</h2>", unsafe_allow_html=True)
    g2.plotly_chart(fig, use_container_width=True) 
        

    # fct = get_content_dt('content', top3_cve[2])
    # fct.to_csv('data/fct.csv', index=False)
    fct = pd.read_csv('data/fct.csv')
    fig = px.bar(fct, x = 'date', y='freq', template = 'seaborn')
    fig.update_traces(marker_color='#264653')
    fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None)
    g3.markdown(f"<h4 style='text-align: center; color: grey;'>{top3_cve[2].upper()}</h2>", unsafe_allow_html=True)
    g3.plotly_chart(fig, use_container_width=True) 



with st.container():
    g1, g2, g3 = st.columns((1,1.5,1))

    # cve, top3_cve = get_cve_topk(topk=3)

    top3_cve = ['cve-2022-42889', 'cve-2022-40684', 'cve-2022-37969']

    # fgdf = get_content_dt('content', top3_cve[0])
    # fgdf.to_csv('data/fgdf.csv', index=False)
    fgdf = pd.read_csv('data/fgdf.csv')
    fig = px.bar(fgdf, x = 'date', y='freq', template = 'seaborn')
    fig.update_traces(marker_color='#264653')
    fig.update_layout(title_x=0,margin= dict(l=10,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None)
    g1.markdown(f"<h4 style='text-align: center; color: grey;'>{top3_cve[0].upper()}</h2>", unsafe_allow_html=True)
    g1.plotly_chart(fig, use_container_width=True) 
        
    # t1, wc, t2 = g2.columns((1,2,1))    
    # g2.markdown("<h2 style='text-align: center; color: grey;'>WordCloud</h2>", unsafe_allow_html=True)    
    g2.write(" ")
    g2.write(" ")
    g2.write(" ")
    g2.write(" ")
    g2.image('images/twitter_wordcloud.png', use_column_width=True)


    # fct = get_content_dt('content', top3_cve[2])
    # fct.to_csv('data/fct.csv', index=False)
    fct = pd.read_csv('data/fct.csv')
    fig = px.bar(fct, x = 'date', y='freq', template = 'seaborn')
    fig.update_traces(marker_color='#264653')
    fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None)
    g3.markdown(f"<h4 style='text-align: center; color: grey;'>{top3_cve[2].upper()}</h2>", unsafe_allow_html=True)
    g3.plotly_chart(fig, use_container_width=True) 

with st.container():
    g1, g2, g3 = st.columns((1,1,1))

    # cve, top3_cve = get_cve_topk(topk=3)

    top3_cve = ['cve-2022-42889', 'cve-2022-40684', 'cve-2022-37969']

    # fgdf = get_content_dt('content', top3_cve[0])
    # fgdf.to_csv('data/fgdf.csv', index=False)
    fgdf = pd.read_csv('data/fgdf.csv')
    fig = px.bar(fgdf, x = 'date', y='freq', template = 'seaborn')
    fig.update_traces(marker_color='#264653')
    fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None)
    g1.markdown(f"<h4 style='text-align: center; color: grey;'>{top3_cve[0].upper()}</h2>", unsafe_allow_html=True)
    g1.plotly_chart(fig, use_container_width=True) 
        
            
    # fcst = get_content_dt('content', top3_cve[1])
    # fcst.to_csv('data/fcst.csv', index=False)
    fcst = pd.read_csv('data/fcst.csv')
    fig = px.bar(fcst, x = 'date', y='freq', template = 'seaborn')
    fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None)
    g2.markdown(f"<h4 style='text-align: center; color: grey;'>{top3_cve[1].upper()}</h2>", unsafe_allow_html=True)
    g2.plotly_chart(fig, use_container_width=True) 
        

    # fct = get_content_dt('content', top3_cve[2])
    # fct.to_csv('data/fct.csv', index=False)
    fct = pd.read_csv('data/fct.csv')
    fig = px.bar(fct, x = 'date', y='freq', template = 'seaborn')
    fig.update_traces(marker_color='#264653')
    fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None)
    g3.markdown(f"<h4 style='text-align: center; color: grey;'>{top3_cve[2].upper()}</h2>", unsafe_allow_html=True)
    g3.plotly_chart(fig, use_container_width=True) 

