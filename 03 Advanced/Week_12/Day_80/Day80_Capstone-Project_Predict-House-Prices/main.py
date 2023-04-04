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

# Next to the River?

grouped_properties = data['CHAS'].value_counts()
print(grouped_properties)

plt.figure(figsize=(14,8))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Next to Charles River?')
plt.xlabel('Property Located Next to the River?')
plt.ylabel('Number of Homes')
plt.bar(['No', 'Yes'], grouped_properties)
plt.show()

# Understand the Relationships in the Data

sns.pairplot(data,
             x_vars='DIS',
             y_vars='NOX',
             hue='DIS',
             aspect=2)

sns.pairplot(data,
             x_vars='RM',
             y_vars='PRICE')

sns.pairplot(data,
             x_vars='LSTAT',
             y_vars='PRICE')

# Distance from Employment vs. Pollution

sns.jointplot(data=data,
              x='DIS',
              y='NOX')

# Proportion of Non-Retail Industry versus Pollution

sns.jointplot(data=data,
              x='INDUS',
              y='NOX')

# % of Lower Income Population vs Average Number of Rooms

sns.jointplot(data=data,
              x='LSTAT',
              y='RM')

# % of Lower Income Population versus Home Price

sns.jointplot(data=data,
              x='LSTAT',
              y='PRICE')

# Number of Rooms versus Home Value

sns.jointplot(data=data,
              x='RM',
              y='PRICE')


