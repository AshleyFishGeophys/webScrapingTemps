import streamlit as st
import plotly.express as px
from functions import get_from_db

st.title("time vs avg temp")

dates, temps = get_from_db()


figure = px.line(x=dates, y=temps, labels={"x":"date", "y":"temperature"})

st.plotly_chart(figure)
