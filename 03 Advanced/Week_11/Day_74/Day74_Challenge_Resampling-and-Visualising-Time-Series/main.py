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
