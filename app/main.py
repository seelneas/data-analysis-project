import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
files = ['data/benin-malanville.csv', 'data/sierraleone-bumbuna.csv', 'data/togo-dapaong_qc.csv']
df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

st.title('Solar Analysis Dashboard')

# Sidebar for User Inputs
st.sidebar.header('User Inputs')
selected_var = st.sidebar.selectbox('Select Variable', ['GHI', 'DNI', 'DHI', 'Tamb'])

# Display Data
st.write(df.head())

# Plotting
st.subheader(f'{selected_var} Over Time')
st.line_chart(df[selected_var])

# Correlation Heatmap
st.subheader('Correlation Heatmap')
corr = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)
