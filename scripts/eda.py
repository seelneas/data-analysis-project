import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
files = ['data/benin-malanville.csv', 'data/sierraleone-bumbuna.csv', 'data/togo-dapaong_qc.csv']
df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

# Check Data
print(df.head())
print(df.columns)

# Handle Missing Values
df['RH'] = pd.to_numeric(df['RH'], errors='coerce')
df['RH'].fillna(df['RH'].mean(), inplace=True)

# Analyze RH Data
print(df['RH'].describe())

# Plot RH Data
plt.figure(figsize=(10, 6))
sns.histplot(df['RH'])
plt.title('Relative Humidity Distribution')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Frequency')
plt.show()

# Correlation Analysis
correlation_matrix = df[['RH', 'GHI', 'DNI', 'DHI', 'Tamb']].corr()
print("Correlation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Heatmap')
plt.show()
