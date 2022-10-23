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

startday = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
endday = (datetime.datetime.now()).strftime('%Y-%m-%d')

dftw = pd.read_csv('data/twitter_raw.csv')
dftw['date'] = pd.to_datetime(dftw['date']).apply(lambda x: x.strftime('%Y-%m-%d'))
dftw = dftw.sort_values(by='date', ascending=False)
cve = [1 if 'cve' in x.lower() else 0 for x in dftw['content']]
dftw['cve'] = cve
df = dftw[dftw.cve == 1]

def get_cve_topk(df=df, startdate=startday, enddate=endday, k=8):
    cve = {}
    startdate = datetime.datetime.strptime(startdate, '%Y-%m-%d')
    enddate = datetime.datetime.strptime(enddate, '%Y-%m-%d')
    numdays = (enddate - startdate).days
    df.date = pd.to_datetime(df.date)
    df = df[(df.date >= startdate) & (df.date <= enddate)]
    for i in range(len(df)):
        # dt = datetime.datetime.strptime(df.iloc[i]['date'], '%Y-%m-%d')
        if startdate <= df.iloc[i]['date'] <= enddate:
            words = df.iloc[i]['content'].split()
            # create a set of words are cve
            cve_words = set()
            for word in words:
                if word.startswith('cve') and len(word) > 8:
                    word = word.lower().replace(':', '').replace(',', '').replace('.', '').replace(';', '').replace(')', '').replace('(', '')
                    cve_words.add(word)
            for word in cve_words:
                cve[word] = cve.get(word, 0) + 1
    sorted_cve = sorted(cve.items(), key=lambda x: x[1], reverse=True)
    topk = sorted_cve[:k]
    topk_cve = [x[0] for x in topk]
    return topk_cve

def get_content_dt(df=df, word="", startdate=startday, enddate=endday):
    content = []
    startdate = datetime.datetime.strptime(startdate, '%Y-%m-%d')
    enddate = datetime.datetime.strptime(enddate, '%Y-%m-%d')
    numdays = (enddate - startdate).days
    df.date = pd.to_datetime(df.date)
    df = df[(df.date >= startdate) & (df.date <= enddate)]
    for i in range(len(df)):
        if word in df.iloc[i]['content']:
            content.append(df.iloc[i])
    freq_val = []
    for day in range(numdays):
        day = startdate + datetime.timedelta(days=day)
        freq_val.append(len([x for x in content if x['date'].date() == day.date()]))
    freq = dict(zip([startdate + datetime.timedelta(days=x) for x in range(numdays)], freq_val))
    df = pd.DataFrame(freq.items(), columns=['date', 'freq'])
    df = df.sort_values(by='date', ascending=False)
    return df