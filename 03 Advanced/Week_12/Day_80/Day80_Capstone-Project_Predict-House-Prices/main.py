import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

pd.options.display.float_format = '{:,.2f}'.format

data = pd.read_csv('boston.csv', index_col=0)

# Preliminary Data Exploration

print(f'There are {data.shape[0]} rows and {data.shape[1]} columns!')
print(data.head())

# Data Cleaning - Check for Missing Values and Duplicates

print(f'\nAre there any NaN values: {data.isna().values.any()}\n')
print(f'Are there any duplicates: {data[data.duplicated()]}')

# Descriptive Statistics

print(f'Student-teacher ratio on average: {data.PTRATIO.mean()}')
print(f'Average price of a home: ${round(data.PRICE.mean() * 1000, 2)}')
print(f'Minimum number of rooms per dwelling: {data.RM.min()}')
print(f'Maximum number of rooms per dwelling: {data.RM.max()}')

# Visualise the Features

# House Prices:
plt.figure(figsize=(8,4), dpi=200)
sns.displot(data=data,
            x='PRICE',
            aspect=2,)
plt.show()

# Distance to Employment - Length of Commute

plt.figure(figsize=(8,4), dpi=200)
sns.displot(data=data,
            x='DIS',
            aspect=2,)
plt.show()

# Number of Rooms

plt.figure(figsize=(8,4), dpi=200)
sns.displot(data=data,
            x='RM',
            aspect=2,)
plt.show()

# Access to Highways

plt.figure(figsize=(8,4), dpi=200)
sns.displot(data=data,
            x='RAD',
            aspect=2,)
plt.show()


