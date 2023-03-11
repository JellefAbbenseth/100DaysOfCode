import pandas as pd
import matplotlib.pyplot as plt

# original in colaboratory

print('Tesla Search Trend vs Price:\n')
df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')
print(df_tesla, end='\n\nBitcoin Search Trend:\n')

df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
print(df_btc_search, end='\n\nDaily Bitcoin Price:\n')
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')
print(df_btc_price, end='\n\nUE Benefits Search vs UE Rate 2004-19:\n')

df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')
print(df_unemployment)


# Data Exploration
# Tesla
print('\n\nTesla:\n')
print(df_tesla.shape)
print(df_tesla.head())
print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')
print(df_tesla.describe(), end="\n\n")

# Unemployment Data
print('Unemployment Data:\n')
print(df_unemployment.shape)
print(df_unemployment.head())
print('Largest value for "Unemployemnt Benefits" '
      f'in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}', end='\n\n')

# Bitcoin
print('Bitcoin: \n')
print(df_btc_price.shape)
print(df_btc_price.head())

print(df_btc_search.shape)
print(df_btc_search.head())

print(f'largest BTC News Search: {df_btc_search.BTC_NEWS_SEARCH.max()}')

