import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("./temperatures.db")
cursor = connection.cursor()
dates = list(cursor.execute("SELECT date FROM temperatures"))
x_asis = [date[0] for date in dates]

temperatures = list(cursor.execute("SELECT temperature FROM temperatures"))
y_asis = [temperature[0] for temperature in temperatures]

st.header("Web scraping temperatures plot!")

plot = px.line(x=x_asis, y=y_asis, labels={"x":"dates", "y": "temperatures"})
st.plotly_chart(plot)
