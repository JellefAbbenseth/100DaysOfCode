import pandas as pd
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
