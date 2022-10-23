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

g1, g2, g3, g4 = st.columns((1,1,1,1))

cve, top3_cve = get_cve_topk(topk=4)
    
    
fgdf = get_content_dt('content', top3_cve[0])
fig = px.bar(fgdf, x = 'date', y='freq', template = 'seaborn')
fig.update_traces(marker_color='#264653')
fig.update_layout(title_text=top3_cve[0].upper(),title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None)
g1.plotly_chart(fig, use_container_width=True) 
    
        
fcst = get_content_dt('content', top3_cve[1])
fig = px.bar(fcst, x = 'date', y='freq', template = 'seaborn')
fig.update_traces(marker_color='#7A9E9F')
fig.update_layout(title_text=top3_cve[1].upper(),title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None)
g2.plotly_chart(fig, use_container_width=True)  
    

fct = get_content_dt('content', top3_cve[2])
fig = px.bar(fct, x = 'date', y='freq', template = 'seaborn')
fig.update_traces(marker_color='#264653')
# fig.add_scatter(x=fct['date'], y=fct['freq'], mode='lines', line=dict(color="blue"), name='freq')
fig.update_layout(title_text=top3_cve[2].upper(),title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None, legend=dict(orientation="h",yanchor="bottom",y=0.9,xanchor="right",x=0.99))
g3.plotly_chart(fig, use_container_width=True) 

fct = get_content_dt('content', top3_cve[3])
fig = px.bar(fcst, x = 'date', y='freq', template = 'seaborn')
fig.update_traces(marker_color='#7A9E9F')
fig.update_layout(title_text=top3_cve[3].upper(),title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None, legend=dict(orientation="h",yanchor="bottom",y=0.9,xanchor="right",x=0.99))
g4.plotly_chart(fig, use_container_width=True) 