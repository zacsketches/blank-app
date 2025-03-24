import streamlit as st
import plotly.express as px

fig = px.line(x=[1,2,3,4,6], y=[4,5,6,7,9])
st.plotly_chart(fig)
