import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. Page Configuration
st.set_page_config(page_title="My First Hackathon App", page_icon="🚀", layout="wide")

# 2. Header and Introduction
st.title("📊 Real-Time Hackathon Data Dashboard")
st.write("Welcome Vinisha! This app demonstrates how quickly you can build a UI using pure Python.")

# 3. Sidebar Configuration
st.sidebar.header("Control Panel")
data_points = st.sidebar.slider("Number of data points to generate:", min_value=10, max_value=200, value=50)
chart_type = st.sidebar.selectbox("Choose Chart Type:", ["Line Chart", "Area Chart", "Bar Chart"])

# 4. Generate Mock Data using NumPy & Pandas
# We generate a matrix of random numbers and format it into a data frame
chart_data = pd.DataFrame(
    np.random.randn(data_points, 3),
    columns=['Feature A', 'Feature B', 'Feature C']
)

# 5. Display Interactive Elements based on User Selection
st.subheader("⚙️ Live Metrics Visualizer")

if chart_type == "Line Chart":
    st.line_chart(chart_data)
elif chart_type == "Area Chart":
    st.area_chart(chart_data)
else:
    st.bar_chart(chart_data)

# 6. Show the raw underlying dataset
if st.checkbox("Show Raw Data Table"):
    st.subheader("📋 Underlying Dataset")
    st.dataframe(chart_data)
