import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px


def get_data(database_data):
    return pd.read_csv(database_data)



def main():
    df = get_data("data.csv")

    # Dashboard creation

    st.set_page_config(
        page_title="Real-time Tweets Sentiment Analysis",
        page_icon = "https://cdn.freebiesupply.com/logos/large/2x/twitter-3-logo-png-transparent.png",
        layout="wide", 
        menu_items = {"About":"Source code: https://github.com/Hernandez2206/real_time_page"}
    )

    #importing css 
    with open('styles.css') as styles:
        st.markdown(f'<style>{styles.read()}</style>', unsafe_allow_html=True)

    #hastag to extract
    st.title("Real-Time Dashboard")

    title = st.text_input("",placeholder="Enter a hashtag")

    if title:
        title = "@" + title.replace(" ","")
        st.write("You entered: ", title)

main()

