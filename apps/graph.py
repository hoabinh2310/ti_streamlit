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

# graph, wc = st.columns((2.7, 1.3))

# # Graph
# graph.markdown("<h2 style='text-align: center; color: grey;'>Graph</h2>", unsafe_allow_html=True)
# graph.write("")

st.title("Graph")
st.graphviz_chart('''
            digraph Twelve_colors {
            # resize the graph
            size="5,5";
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
            // © 2022 TI Streamlit
        }
        ''', use_container_width=True)