import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px


def get_data(database_data):
    return pd.read_csv(database_data)



def main():
    show = False
    
    df = get_data("data1.csv")
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

    #show if we got a hashtag
    if title:
        title = "@" + title.replace(" ","")
        st.write("You entered: ", title)
        show = True
        #agree = st.checkbox('Press me')
    
    container = st.empty()
    happy_previous = 0
    neutral_previous = 0
    bad_previous = 0

    #while agree:
    with container.container():

        # getting data
        emotions = df["clasification"].value_counts()
        n_happy_actual = int(emotions['happy'])
        n_neutral_actual = int(emotions['neutral'])
        n_bad_actual = int(emotions['bad'])

        #show if we got a hashtag
        if show:

            # create three columns
            happy, neutral, bad = st.columns(3)

            happy.metric(
                label="Happy 😀",
                value=n_happy_actual,
                delta=n_happy_actual - happy_previous
            )

            neutral.metric(
                label = "Neutral 😐",
                value = n_neutral_actual,
                delta = int(n_neutral_actual - neutral_previous)
            )

            bad.metric(
                label = "Bad 😡",
                value = n_bad_actual,
                delta = n_bad_actual - bad_previous
            )
            happy_previous = n_happy_actual
            neutral_previous = n_neutral_actual
            bad_previous = n_bad_actual

time.sleep(2)   
#if agree == False:
#        st.write("We finished")


main()

