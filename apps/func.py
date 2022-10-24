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
# import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import json

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
    for day in range(numdays+1):
        day = startdate + datetime.timedelta(days=day)
        freq_val.append(len([x for x in content if x['date'].date() == day.date()]))
    freq = dict(zip([startdate + datetime.timedelta(days=x) for x in range(numdays)], freq_val))
    df = pd.DataFrame(freq.items(), columns=['date', 'freq'])
    df = df.sort_values(by='date', ascending=False)
    return df

def get_cve_wc(df=df, startdate=startday, enddate=endday,k=8):
    cve = {}
    startdate = datetime.datetime.strptime(startdate, '%Y-%m-%d')
    enddate = datetime.datetime.strptime(enddate, '%Y-%m-%d')
    numdays = (enddate - startdate).days
    df['date'] = df['date'].apply(pd.to_datetime)
    df = df[(df.date >= startdate) & (df.date <= enddate)]
    wc = []
    for i in range(len(df)):
        if startdate <= df.iloc[i]['date'] <= enddate:
            words = df.iloc[i]['content'].split()
            cve_words = set()
            for word in words:
                if word.startswith('cve') and len(word) > 8:
                    word = word.lower().replace(':', '').replace(',', '').replace('.', '').replace(';', '').replace(')', '').replace('(', '').replace('-','')
                    cve_words.add(word)
                    wc.append(word)
            for word in cve_words:
                cve[word] = cve.get(word, 0) + 1
    sorted_cve = sorted(cve.items(), key=lambda x: x[1], reverse=True)
    topk = sorted_cve[:k]
    topk_cve = [x[0] for x in topk]

    image = 'images/twitterlogo.png'
    mask = np.array(Image.open(image))
    iwc = WordCloud(background_color="white", max_words=2000, mask=mask, collocations=False, contour_color='#1c96e8', contour_width=1.5)
    iwc.generate(' '.join(wc))
    iwc.to_file('images/twitter_wordcloud2.png')
    # print('Wordcloud saved to images/twitter_wordcloud2.png')
    return iwc



def get_ner():
    df_raw = pd.read_csv('data/blog_raw.csv')
    id2url = {}
    for idx, _url in zip(df_raw["id"], df_raw['url']):
        id2url[idx] = _url

    df = pd.read_csv('data/blog_summary.csv')
    ner_data = json.load(open('data/ner.json', 'r'))

    dict_id_ner = {}
    dict_text_tag = {}
    set_long_text = set()
    set_idx = set()

    for i in ner_data:
        dict_id_ner[i] = ner_data[i]
        set_idx.add(i)
        for nr in ner_data[i]:
            dict_text_tag[nr['text']] = nr['tag']
            set_long_text.add(nr['text'].replace(' ', '_'))

    color = {
        "application": "#faa",
        "hardware": "#00ff00",
        "os": "#0000ff",
        "relevant_term": "#afa",
        "update": "#8ef",
        "vendor": "#fea",
        "version": "#ff8000",
    }

    title = []
    ner = []
    url = []
    for i in range(len(df)):
        if df.iloc[i]['id'] in set_idx:
            title.append(df.title[i])
            text = df.summary[i]
            for long_text in set_long_text:
                text = text.replace(long_text, long_text.replace('_', ' '))
            url.append(id2url[df.iloc[i]['id']])
            text = text.split(' ')
            ner.append([(x, dict_text_tag.get(x, 'O')+" ", color[dict_text_tag.get(x, 'O')]) if (dict_text_tag.get(x, 'O')!='O') else (x + " ") for x in text ])
    
    return ner, title, url