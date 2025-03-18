import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dashboard title
st.title('Anya\'s First Dashboard')

# Sidebar navigation
st.sidebar.title('Want to know more:')
section = st.sidebar.radio('Go to: ', ['Home', 'Data Table', 'Bar Chart'])

# Load data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 17, 35, 29]
    })

# Define pages based on navigation
if section == 'Home':
    st.write('Welcome to the dashboard! Please select a section from the sidebar.')
    st.write('The next line...')
    
elif section == 'Data Table':
    st.subheader('Data Table')
    st.write(data)
    
elif section == 'Bar Chart':
    st.subheader('Bar Chart')
    fig, ax = plt.subplots()
    ax.bar(data['Category'], data['Values'])
    ax.set_xlabel('Category')
    ax.set_ylabel('Values')
    st.pyplot(fig)
    
