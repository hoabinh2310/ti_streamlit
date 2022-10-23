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

import streamlit as st
from annotated_text import annotated_text

import json
from apps.func import get_ner

"""
# Annotated text example

Below is an example of how to use the annotated_text function:
"""


# def get_ner():

#     df = pd.read_csv('data/blog_summary.csv')
#     ner_data = json.load(open('data/ner.json', 'r'))

#     dict_id_ner = {}
#     dict_text_tag = {}
#     set_long_text = set()
#     set_idx = set()

#     title = []
#     summary = []
#     ner = []
#     for i in ner_data:
#         dict_id_ner[i] = ner_data[i]
#         set_idx.add(i)
#         for nr in ner_data[i]:
#             dict_text_tag[nr['text']] = nr['tag']
#             set_long_text.add(nr['text'].replace(' ', '_'))

#     # print(df)
#     for i in range(len(df)):
#         if df.iloc[i]['id'] in set_idx:
#             title.append(df.title[i])
#             text = df.summary[i]
#             for long_text in set_long_text:
#                 text = text.replace(long_text, long_text.replace('_', ' '))
#             # summ
#             text = text.split(' ')
#             ner.append([(x, dict_text_tag.get(x, 'O')+" ") if (dict_text_tag.get(x, 'O')!='O') else (x + " ") for x in text ])
    
#     return ner, title



# st.write("")
# st.write("")
# st.write("")
# st.write("")

# ner, title = get_ner()
# annotated_text(*ner[0])