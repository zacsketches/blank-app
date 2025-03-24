import plotly.graph_objects as go
import numpy as np
import streamlit as st

# Sample data
t = np.linspace(0, 10, 100)
y1 = np.sin(t)
y2 = np.cos(t)
y3 = np.sin(t) * np.cos(t)

# Create figure
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=t, y=y1, mode='lines', name='sin(t)'))
fig.add_trace(go.Scatter(x=t, y=y2, mode='lines', name='cos(t)'))
fig.add_trace(go.Scatter(x=t, y=y3, mode='lines', name='sin(t) * cos(t)'))

# Customize layout
fig.update_layout(
    title='Multiple Line Series Plot',
    xaxis_title='Time',
    yaxis_title='Value',
    template='plotly_dark',
    dragmode='pan',  # Enables panning
    xaxis=dict(rangeslider=dict(visible=True)),  # Enables zooming with range slider
)

# Streamlit app
st.title("Plotly Line Chart in Streamlit")
st.plotly_chart(fig, use_container_width=True)