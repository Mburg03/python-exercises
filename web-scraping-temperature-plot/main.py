import streamlit as st
import plotly.express as px
import pandas as pd

st.header("Web scraping temperatures plot!")
df = pd.read_csv("./temperatures.csv")

x_asis = df["date"].tolist()
y_asis = df["temperature"].tolist()

plot = px.line(x=x_asis, y=y_asis, labels={"x":"dates", "y": "temperatures"})
st.plotly_chart(plot)
