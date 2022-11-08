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
from apps.func import *
import warnings     
warnings.filterwarnings('ignore')


st.title("Twitter Trends")

dftw = pd.read_csv('data/twitter_raw.csv')
dftw['date'] = pd.to_datetime(dftw['date']).apply(lambda x: x.strftime('%Y-%m-%d'))
dftw = dftw.sort_values(by='date', ascending=False)
cve = [1 if 'cve' in x.lower() else 0 for x in dftw['content']]
dftw['cve'] = cve
df = dftw[dftw.cve == 1]


# choice = st.selectbox('Make a selection', ['week', 'month', 'year', 'all'], key=1)

# kdays = {'week': 7, 'month': 30, 'year': 365, 'all': 365*4}

# startday = (datetime.datetime.now() - datetime.timedelta(days=kdays[choice])).strftime('%Y-%m-%d')
# endday = (datetime.datetime.now()).strftime('%Y-%m-%d')

day = startday = (datetime.datetime.now() - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
day2 = startday = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
start_date = st.date_input("Start Date", value=pd.to_datetime(day, format="%Y-%m-%d"), max_value=pd.to_datetime("today", format="%Y-%m-%d"))
end_date = st.date_input("End Date", value=pd.to_datetime(day2, format="%Y-%m-%d"), max_value=pd.to_datetime("today", format="%Y-%m-%d"), min_value=start_date)

# convert the dates to string
startday = start_date.strftime("%Y-%m-%d")
endday = end_date.strftime("%Y-%m-%d")

list_cve = get_cve_topk(df=df, startdate = startday, enddate = endday, k=8)
ldf = []
for cve in list_cve:
    df_count = get_content_dt(df, cve, startday, endday)
    ldf.append(df_count)

with st.container():
    g1, g2, g3 = st.columns((1,1,1))
    with g1:
        fig = px.bar(ldf[0], x = 'date', y='freq', template = 'seaborn')
        fig.update_traces(marker_color='#D65050')
        fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None, width=300, height=300)
        g1.markdown(f"<h4 style='text-align: center;'>{list_cve[0].upper()}</h2>", unsafe_allow_html=True)
        g1.plotly_chart(fig, use_container_width=True) 
    
    with g2:
        fig = px.bar(ldf[1], x = 'date', y='freq', template = 'seaborn')
        fig.update_traces(marker_color='#D65050')
        fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None, width=300, height=300)
        g2.markdown(f"<h4 style='text-align: center;'>{list_cve[1].upper()}</h2>", unsafe_allow_html=True)
        g2.plotly_chart(fig, use_container_width=True) 
    
    with g3:
        fig = px.bar(ldf[2], x = 'date', y='freq', template = 'seaborn')
        fig.update_traces(marker_color='#D65050')
        fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None, width=300, height=300)
        g3.markdown(f"<h4 style='text-align: center;'>{list_cve[2].upper()}</h2>", unsafe_allow_html=True)
        g3.plotly_chart(fig, use_container_width=True) 


with st.container():
    g1, g2, g3 = st.columns((1,1,1))
    with g1:
        fig = px.bar(ldf[3], x = 'date', y='freq', template = 'seaborn')
        fig.update_traces(marker_color='#D65050')
        fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None, width=300, height=300)
        g1.markdown(f"<h4 style='text-align: center;'>{list_cve[3].upper()}</h2>", unsafe_allow_html=True)
        g1.plotly_chart(fig, use_container_width=True) 
    
    # t1, wc, t2 = g2.columns((1,2,1))    
    # g2.markdown("<h2 style='text-align: center; color: grey;'>WordCloud</h2>", unsafe_allow_html=True)    
    g2.write(" ")
    g2.write(" ")
    # g2.write(" ")

    get_cve_wc(df=df, startdate = startday, enddate = endday)
    g2.image('images/twitter_wordcloud2.png', use_column_width=True)

    with g3:
        fig = px.bar(ldf[4], x = 'date', y='freq', template = 'seaborn')
        fig.update_traces(marker_color='#D65050')
        fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None, width=300, height=300)
        g3.markdown(f"<h4 style='text-align: center;'>{list_cve[4].upper()}</h2>", unsafe_allow_html=True)
        g3.plotly_chart(fig, use_container_width=True) 


with st.container():
    g1, g2, g3 = st.columns((1,1,1))
    with g1:
        fig = px.bar(ldf[5], x = 'date', y='freq', template = 'seaborn')
        fig.update_traces(marker_color='#D65050')
        fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None, width=300, height=300)
        g1.markdown(f"<h4 style='text-align: center;'>{list_cve[5].upper()}</h2>", unsafe_allow_html=True)
        g1.plotly_chart(fig, use_container_width=True) 
    
    with g2:
        fig = px.bar(ldf[6], x = 'date', y='freq', template = 'seaborn')
        fig.update_traces(marker_color='#D65050')
        fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None, width=300, height=300)
        g2.markdown(f"<h4 style='text-align: center;'>{list_cve[6].upper()}</h2>", unsafe_allow_html=True)
        g2.plotly_chart(fig, use_container_width=True) 
    
    with g3:
        fig = px.bar(ldf[7], x = 'date', y='freq', template = 'seaborn')
        fig.update_traces(marker_color='#D65050')
        fig.update_layout(title_x=0,margin= dict(l=0,r=10,b=10,t=0), yaxis_title=None, xaxis_title=None, width=300, height=300)
        g3.markdown(f"<h4 style='text-align: center;'>{list_cve[7].upper()}</h2>", unsafe_allow_html=True)
        g3.plotly_chart(fig, use_container_width=True) 

