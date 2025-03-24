import streamlit as st
import plotly.express as px

fig = px.line(x=[1,2,3,4], y=[4,5,6,7])
st.plotly_chart(fig)
