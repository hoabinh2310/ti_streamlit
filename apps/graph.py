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

t1, wc, t2 = st.columns((0.75,2,0.75))
title = 'Under Development'
wc.markdown(f"<h2 style='text-align: center;'>{title}</h2>", unsafe_allow_html=True)
wc.image('images/dvl.png', use_column_width=True)