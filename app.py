import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Hackathon Data Analyzer", page_icon="📈", layout="wide")

st.title("📈 Real-World Tech Salary Analyzer")
st.write("This dashboard loads real data using Pandas and showcases clean filters for judges.")

# 2. Load the Dataset using Pandas
# Pandas converts the CSV into a "DataFrame" (a highly optimized table)
df = pd.read_csv("tech_jobs.csv")

# 3. Sidebar Filter: Interactive Job Filter
st.sidebar.header("Filter Settings")
unique_jobs = df["Job_Title"].unique() # Extracts unique job roles from our data
selected_job = st.sidebar.selectbox("Select a Job Role to Analyze:", unique_jobs)

# 4. Filter the data table based on user selection
filtered_df = df[df["Job_Title"] == selected_job]

# 5. Core Insights (Math Calculations via Pandas)
st.subheader(f"📊 Insights for: {selected_job}s")

# Create simple columns for quick-glance metrics
col1, col2, col3 = st.columns(3)

with col1:
    avg_salary = filtered_df["Salary_USD"].mean() # Calculates mathematical average
    st.metric(label="Average Salary", value=f"${avg_salary:,.0f} USD")

with col2:
    highest_salary = filtered_df["Salary_USD"].max() # Finds the highest value
    st.metric(label="Highest Salary Tracked", value=f"${highest_salary:,.0f} USD")

with col3:
    total_listings = len(filtered_df) # Counts rows matching the filter
    st.metric(label="Total Job Postings", value=total_listings)

# 6. Display the filtered data table visually
st.write("### 📋 Matching Jobs")
st.dataframe(filtered_df, use_container_width=True)

# 7. Visualization: Salary Comparison Bar Chart across companies
st.write("### 📊 Salary Comparison Across Companies")
st.bar_chart(data=filtered_df, x="Company", y="Salary_USD")
