import streamlit as st
import plotly.express as px
from functions import read

st.title("time vs avg temp")

dates, temps = read()

figure = px.line(x=dates, y=temps, labels={"x":"date", "y":"temperature"})

st.plotly_chart(figure)
