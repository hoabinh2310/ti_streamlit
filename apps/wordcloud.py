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

st.title("Word Cloud")

wc, data = st.columns((2, 1))

# wc.markdown("<h2 style='text-align: center; color: grey;'>WordCloud</h2>", unsafe_allow_html=True)
# wc.write("")
wc.image('images/twitter_wordcloud.png', use_column_width=True)