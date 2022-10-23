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
            # create a set of words are cve
            cve_words = set()
            for word in words:
                if word.startswith('cve') and len(word) > 8:
                    word = word.lower().replace(':', '').replace(',', '').replace('.', '').replace(';', '').replace(')', '').replace('(', '')
                    cve_words.add(word)
            for word in cve_words:
                cve[word] = cve.get(word, 0) + 1
    sorted_cve = sorted(cve.items(), key=lambda x: x[1], reverse=True)
    topk = sorted_cve[:topk]
    topk_cve = [x[0] for x in topk]
    return cve, topk_cve