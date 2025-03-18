import streamlit as st
import pandas as pd

# Dashboard title
st.title('Anya\'s First Dashboard')

# Load data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 17, 35, 29]
    })

# Tabs for navigation
tab1, tab2, tab3 = st.tabs(['Home', 'Data Table', 'Bar Chart'])

with tab1: 
    st.write('Welcome to the dashboard! Please select a tab above.')
    
with tab2: 
    st.subheader('Data Table')
    st.write(data)
    
with tab3: 
    st.subheader('Bar Chart')
    st.bar_chart(data.set_index('Category'))