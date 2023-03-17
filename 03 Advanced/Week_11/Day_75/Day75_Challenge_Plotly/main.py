import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# original in colaboratory

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

df_apps = pd.read_csv('apps.csv')

print(df_apps.shape)

print(df_apps.sample(5))

# Drop Unused Columns
df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)
print(df_apps.head())

# Find and Remove NaN values in Ratings
nan_rows = df_apps[df_apps.Rating.isna()]
print(nan_rows.shape)
print(nan_rows.head())

df_apps_clean = df_apps.dropna()
print(df_apps_clean.shape)

# Find an Remove Duplicates
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
print(duplicated_rows.head())

print(df_apps_clean[df_apps_clean.App == 'Instagram'])

df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
print(df_apps_clean[df_apps_clean.App == 'Instagram'])

print(df_apps_clean.shape)

# Find different apps
print(df_apps_clean.sort_values('Rating', ascending=False).head())

print(df_apps_clean.sort_values('Size_MBs', ascending=False).head())

print(df_apps_clean.sort_values('Reviews', ascending=False).head(50))

# Plotly Pie and Donut Charts - Visualise Categorical Data: Content Ratings

ratings = df_apps_clean.Content_Rating.value_counts()
print(ratings)

fig = px.pie(labels=ratings.index, values=ratings.values)
fig.show()

fig = px.pie(labels=ratings.index,
             values=ratings.values,
             title="Content Rating",
             names=ratings.index,
             )
fig.update_traces(textposition='outside', textinfo='percent+label')

fig.show()

fig = px.pie(labels=ratings.index,
             values=ratings.values,
             title="Content Rating",
             names=ratings.index,
             hole=0.6,
             )
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')

fig.show()

# Numeric Type Conversion: Examine the Number of Installs

print(df_apps_clean.Installs.describe())

print(df_apps_clean.info())

print(df_apps_clean[['App', 'Installs']].groupby('Installs').count())

df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
print(df_apps_clean[['App', 'Installs']].groupby('Installs').count())

# Find the Most Expensive Apps, Filter out the Junk, and Calculate a (ballpark) Sales

print(df_apps_clean.Price.describe())

df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)

print(df_apps_clean.sort_values('Price', ascending=False).head(20))

df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
print(df_apps_clean.sort_values('Price', ascending=False).head(5))

df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
print(df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10])
