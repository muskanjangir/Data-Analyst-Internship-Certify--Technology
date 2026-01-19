#--------------------------------------------------------------------------------------------------------
#Task 4 -Interactive Dashboard
#• Use Python libraries like Plotly or Streamlit to create an interactive dashboard.
#• Display key insights from a dataset with visualizations (bar charts, pie charts, line graphs, etc.).
#• Ensure the dashboard allows user interaction (e.g., filtering data, selecting parameters).

#-----------------------------------------------------------------------------------------------------------
# pip install streamlit

#loading Libraries

import pandas as pd 
import streamlit as st
import plotly.express as px


#load cleaned data set 

df = pd.read_csv('Tasks/titanic_clean.csv')

#Dashboard title 
st.title("Titanic Interactive Dashboard")
st.write(df.head())

#Sidebar filters 

pclass = st.sidebar.selectbox("Select Pclass" ,sorted(df['pclass'].unique()))

gender = st.sidebar.selectbox("Select Gender" , df['sex'].unique())

#Filter dataset
filtered_df = df[(df['pclass'] == pclass) & (df['sex'] == gender)]
st.write(filtered_df)

#Graphs
fig1 = px.bar(df,x='sex' ,color='survived',title='Gender Vs Survival!')
st.plotly_chart(fig1)

fig2 = px.bar(df,x='pclass' ,color='survived',title='Pclass Vs Survival!')
st.plotly_chart(fig2)

fig3 = px.histogram(df,x='age' ,nbins = 20,title='Age Distribution')
st.plotly_chart(fig3)

fig4 = px.scatter(df,x='age' ,y = 'fare',color='survived',title='Age Vs Fare Scatterplot!')
st.plotly_chart(fig4)


#in terminal ---- streamlit run  Tasks/dashboard.py