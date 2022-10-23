# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:17:07 2021

@author: Andi5
"""
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


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["app"]
mycol = mydb["twitter_raw"]
today = datetime.datetime.now().strftime('%Y-%m-%d')
today_but_last_week = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

def get_content_dt(field, word, startdate=today_but_last_week, enddate=today):
    content = []
    startdate = datetime.datetime.strptime(startdate, '%Y-%m-%d')
    enddate = datetime.datetime.strptime(enddate, '%Y-%m-%d')
    numdays = (enddate - startdate).days
    for x in mycol.find({field: {'$regex': '.*'+word+'.*', '$options': 'i'}}):
        if startdate <= x['date'] <= enddate:
            content.append(x)
    freq_val = []
    for day in range(numdays):
        day = startdate + datetime.timedelta(days=day)
        freq_val.append(len([x for x in content if x['date'].date() == day.date()]))
    freq = dict(zip([startdate + datetime.timedelta(days=x) for x in range(numdays)], freq_val))
    df = pd.DataFrame(freq.items(), columns=['date', 'freq'])
    return df

def get_cve_topk(startdate=today_but_last_week, enddate=today, topk=3):
    cve = {}
    startdate = datetime.datetime.strptime(startdate, '%Y-%m-%d')
    enddate = datetime.datetime.strptime(enddate, '%Y-%m-%d')
    numdays = (enddate - startdate).days
    for x in mycol.find({"content": {"$regex": ".*cve.*"}}):
        if startdate <= x['date'] <= enddate:
            words = x['content'].split()
            for word in words:
                if word.startswith('cve'):
                    word = word.lower().replace(':', '').replace(',', '').replace('.', '').replace(';', '').replace(')', '').replace('(', '')
                    cve[word] = cve.get(word, 0) + 1
    sorted_cve = sorted(cve.items(), key=lambda x: x[1], reverse=True)
    topk = sorted_cve[:topk]
    topk_cve = [x[0] for x in topk]
    return cve, topk_cve



st.set_page_config(page_title='TI',  layout='wide', page_icon=':crab:')
st.markdown(f'<h1 style="text-align: center; color: ;">ĐÂY LÀ TITLE NHƯNG CHƯA BIẾT ĐẶT GÌ</h1>', unsafe_allow_html=True)




## Data

with st.spinner('Updating Report...'):
    
    #Metrics setting and rendering

    # hosp_df = pd.read_excel('DataforMock.xlsx',sheet_name = 'Hospitals')
    # hosp = st.selectbox('Choose Hospital', hosp_df, help = 'Filter report to show only one hospital')
    
    # m1, m2, m3, m4, m5 = st.columns((1,1,1,1,1))
    
    # todf = pd.read_excel('DataforMock.xlsx',sheet_name = 'metrics')
    # to = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Total Outstanding')]   
    # ch = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Current Handover Average Mins')]   
    # hl = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Hours Lost to Handovers Over 15 Mins')]
    
    # m1.write('')
    # m2.metric(label ='Total Outstanding Handovers',value = int(to['Value']), delta = str(int(to['Previous']))+' Compared to 1 hour ago', delta_color = 'inverse')
    # m3.metric(label ='Current Handover Average',value = str(int(ch['Value']))+" Mins", delta = str(int(ch['Previous']))+' Compared to 1 hour ago', delta_color = 'inverse')
    # m4.metric(label = 'Time Lost today (Above 15 mins)',value = str(int(hl['Value']))+" Hours", delta = str(int(hl['Previous']))+' Compared to yesterday')
    # m1.write('')
     
    # Number of Completed Handovers by Hour
    
    st.markdown("<h2 style='text-align: center; color: grey;'>Trends</h2>", unsafe_allow_html=True)

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
    fig = px.bar(fct, x = 'date', y='freq',color = "freq", template = 'seaborn')
    fig.update_traces(marker_color='#264653')
    # fig.add_scatter(x=fct['date'], y=fct['freq'], mode='lines', line=dict(color="blue"), name='freq')
    fig.update_layout(title_text=top3_cve[2].upper(),title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None, legend=dict(orientation="h",yanchor="bottom",y=0.9,xanchor="right",x=0.99))
    g3.plotly_chart(fig, use_container_width=True) 

    fct = get_content_dt('content', top3_cve[3])
    fig = px.bar(fcst, x = 'date', y='freq', template = 'seaborn')
    fig.update_traces(marker_color='#7A9E9F')
    fig.update_layout(title_text=top3_cve[3].upper(),title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None, legend=dict(orientation="h",yanchor="bottom",y=0.9,xanchor="right",x=0.99))
    g4.plotly_chart(fig, use_container_width=True) 
      
       
with st.spinner('Report updated!'):
    time.sleep(1)   

with st.spinner('Updating graph and wordcloud...'):
    graph, wc = st.columns((2.7, 1.3))

    # Graph
    graph.markdown("<h2 style='text-align: center; color: grey;'>Graph</h2>", unsafe_allow_html=True)
    graph.write("")
    graph.graphviz_chart('''
            digraph Twelve_colors {
            # resize the graph
            size="4,4";
            label = "Twelve colors. Neato layout"
            labelloc = "b"
            layout = neato
            fontname = Arial
            node [
                shape = circle
                width = 1.5
                color="#00000088"
                style = filled
                fontname="Helvetica,Arial,sans-serif"
            ]
            edge [len = 2 penwidth = 1.5 arrowhead=open]
            start = regular
            normalize = 0
            green -> {white yellow cyan yellowgreen springgreen} [color = green]
            green [fillcolor = green fontcolor = white]
            white [fillcolor = white]
            blue [fillcolor = blue fontcolor = white]
            red [fillcolor = red fontcolor = white]
            red -> {white yellow magenta orange deeppink } [color = red]
            yellow [fillcolor = yellow]
            yellow -> {orange yellowgreen} [color = yellow]
            blue -> {white cyan magenta deepskyblue purple} [color = blue]
            cyan [fillcolor = cyan]
            magenta [fillcolor = magenta fontcolor = white]
            deepskyblue [fillcolor = deepskyblue]
            cyan -> {springgreen deepskyblue} [color  = cyan]
            orange [fillcolor = orange]
            yellowgreen [fillcolor = yellowgreen]
            deeppink [fillcolor = deeppink fontcolor = white]
            magenta -> {deeppink purple} [color = magenta]
            purple [fillcolor = purple fontcolor = white]
            springgreen [fillcolor = springgreen]
            // © 2022 Costa Shulyupin, licensed under EPL
        }
        ''', use_container_width=True)

    # Wordcloud
    wc.markdown("<h2 style='text-align: center; color: grey;'>WordCloud</h2>", unsafe_allow_html=True)
    wc.write("")
    wc.image('images/twitter_wordcloud.png', use_column_width=True)

with st.spinner('Updating table...'):
    time.sleep(1)

    # Table
    st.markdown("<h2 style='text-align: center; color: grey;'>Blog</h2>", unsafe_allow_html=True)
    st.write("")

    blog1, blog2, blog3 = st.columns((1,1,1))

    df = pd.read_csv('blog_summary.csv')
    title = df['title'].tolist()
    summary = df['summary'].tolist()

    blog1.markdown(f'<h3 style="text-align: center; color: grey;">{title[0]}</h3>', unsafe_allow_html=True)
    blog1.markdown(f'<p style="background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
                        {summary[0]} </p>', unsafe_allow_html=True)
    
    blog2.markdown(f'<h3 style="text-align: center; color: grey;">{title[1]}</h3>', unsafe_allow_html=True)
    blog2.markdown(f'<p style="background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
                        {summary[1]} </p>', unsafe_allow_html=True)

    blog3.markdown(f'<h3 style="text-align: center; color: grey;">{title[2]}</h3>', unsafe_allow_html=True)
    blog3.markdown(f'<p style="background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
                        {summary[2]} </p>', unsafe_allow_html=True)
    
    blog1.markdown(f'<h3 style="text-align: center; color: grey;">{title[3]}</h3>', unsafe_allow_html=True)
    blog1.markdown(f'<p style="background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
                        {summary[3]} </p>', unsafe_allow_html=True)
    
    blog2.markdown(f'<h3 style="text-align: center; color: grey;">{title[4]}</h3>', unsafe_allow_html=True)
    blog2.markdown(f'<p style="background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
                        {summary[4]} </p>', unsafe_allow_html=True)

    blog3.markdown(f'<h3 style="text-align: center; color: grey;">{title[5]}</h3>', unsafe_allow_html=True)
    blog3.markdown(f'<p style="background-color:#f0f2f6;color:black;font-size:16px;border-radius:2%;margin:15px;padding:15px"> \
                        {summary[5]} </p>', unsafe_allow_html=True)
