# ! python-exercises\mood-notes-analyzer\venv\Scripts\python.exe
import streamlit as st
import plotly.express as px
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from pathlib import Path

nltk.download('vader_lexicon')

filepaths = glob.glob("./diary/*.txt")
scores = []
analyzer = SentimentIntensityAnalyzer()

# getting neg and pos scores from diary
for filepath in filepaths:
    with open(filepath, 'r', encoding='UTF-8') as file:
        diary = file.read()
    scores.append(analyzer.polarity_scores(diary))

# cleaning data to get each value into each single list
dates = [Path(filepath).stem for filepath in filepaths]
pos_scores = [dict['pos'] for dict in scores]
neg_scores = [dict['neg'] for dict in scores]

# setting streamlit webpage
st.title("Diary Tone")
st.subheader("Happiness")

# creating positive plot figure
pos_figure = px.line(x=dates, y=pos_scores, 
                     labels={"x": "Days", "y": "Happiness"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
# creating negative plot figure
neg_figure = px.line(x=dates, y=neg_scores, 
                     labels={"x": "Days", "y": "Negativity"})
st.plotly_chart(neg_figure)
