import pandas as pd
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters

pd.options.display.float_format = '{:,.2f}'.format

register_matplotlib_converters()

data = pd.read_csv('cost_revenue_dirty.csv')


# Explore and Clean the Data

print("Describe")
print(data.describe)
print("\nShape\n")
print(data.shape)
print("\n")
print(data.head())
print(data.tail())
print('\nInfo\n')
print(data.info())
print('\nSample\n')
print(data.sample())

print('Any Null:')
print(data.isna().values.any())
print('\nAny duplicates:')
print(data.duplicated().values.any())
duplicated_rows = data[data.duplicated()]
print(len(duplicated_rows))

# Data Type Conversions

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget',
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        data[col] = data[col].astype(str).str.replace(char, "")
    data[col] = pd.to_numeric(data[col])

print(data.head())

data.Release_Date = pd.to_datetime(data.Release_Date)
print(data.head())
print('\nInfo:')
print(data.info())

# Descriptive Statistics

print(data.describe())
print('\nLowest budget film:')
print(data[data.USD_Production_Budget == 1100.00])
print(f'\nHighest budget film: \n{data[data.USD_Production_Budget == 425000000.00]}')

# Investigating the Zero Revenue Films

zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
print(zero_domestic.sort_values('USD_Production_Budget', ascending=False))

zero_worldwide = data[data.USD_Worldwide_Gross == 0]
print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
print(zero_worldwide.sort_values('USD_Production_Budget', ascending=False))

# Filtering on Multiple Conditions

international_releases = data.loc[(data.USD_Domestic_Gross == 0) &
                                  (data.USD_Worldwide_Gross != 0)]
print(f'Number of international releasees: {len(international_releases)}\n\nInternational releases:')
print(international_releases.head())

international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}\n\nInternational releases:')
print(international_releases.head())

# Unreleased Films

scrape_date = pd.Timestamp('2018-5-1')
future_releases = data[data.Release_Date >= scrape_date]
print(f'Number of unreleased movies: {len(future_releases)}')
print(future_releases)

data_clean = data.drop(future_releases.index)

# Films that Lost Money

money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
print(f'{(len(money_losing)/len(data_clean) * 100)} %')
