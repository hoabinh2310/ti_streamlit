import streamlit as st

import streamlit_book as stb
from pathlib import Path
#geemap.ee_initialize()


st.session_state["warned_about_save_answers"] = True


st.set_page_config(layout="wide", page_title="SatSchool", page_icon="🛰️")

st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Set multipage
current_path = Path(__file__).parent.absolute()

# Streamit book properties
stb.set_book_config(menu_title="Main Menu",
                    menu_icon="",
                    options=[
                            "Trends",
                            "Wordcloud",
                            "Graph",
                            "Blog",
                            ],
                    paths=[
                        current_path / "apps/trends.py",
                        current_path / "apps/wordcloud.py",
                        current_path / "apps/graph.py",
                        current_path / "apps/blog.py",
                          ],
                    icons=[
                        # name for icon: https://fontawesome.com/v4.7.0/icons/
                          "bar-chart",
                          "cloud",
                          "asterisk",
                          "book",
                          ],
                    save_answers=True,
                    )
    
with st.sidebar:

    st.sidebar.title("About")
    st.sidebar.info(
        """
        🌐 https://test.org
        
        ©️ 2022 TI Streamlit
    """
    )