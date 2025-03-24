python

import streamlit as st
import plotly.express as px

fig = px.line(x=[1,2,3], y=[4,5,6])
st.plotly_chart(fig)
