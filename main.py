import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px

database_data = "url or file"

def get_data(database_data):
    return pd.read_csv(database_data)



df = get_data("data.csv")
print(df)

# Dashboard creation

st.set_page_config(
    page_title="Real-time Tweets Sentiment Analysis",
    page_icon = "https://cdn.freebiesupply.com/logos/large/2x/twitter-3-logo-png-transparent.png",
    layout="wide"
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

#st.write("You entered: ", title)