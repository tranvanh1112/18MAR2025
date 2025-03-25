import streamlit as st
import pandas as pd

# Dashboard title
st.title("Anya's First Dashboard")

# Sidebar navigation
st.sidebar.title("Want to know more:")
section = st.sidebar.radio("Go to: ", ["Home", "Data Table", "Bar Chart"])

# Load data
data = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [23, 17, 35, 29]
})

# Define pages based on navigation
if section == "Home":
    st.write("Welcome to the dashboard! Please select a section from the sidebar.")
    st.write("The next line...")

elif section == "Data Table":
    st.subheader("Data Table")
    st.write(data)

elif section == "Bar Chart":
    st.subheader("Bar Chart")
    st.bar_chart(data.set_index("Category"))
