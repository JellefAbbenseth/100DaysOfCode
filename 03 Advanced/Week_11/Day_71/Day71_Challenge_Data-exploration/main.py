import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')

print(df.head())
print(df.shape)
print(df.columns)
print(df.isna())
print(df.tail())
clean_df = df.dropna()
print(clean_df.tail())
print(clean_df['Starting Median Salary'].idxmax())
print(clean_df['Undergraduate Major'][43])
print(clean_df.loc[43])

# 1. major with highest mid-career salary
print("\n1. Major with highest mid-career salary:\n")
# print(clean_df['Mid-Career Median Salary'].max())
highest_mid_car_salary_id = clean_df['Mid-Career Median Salary'].idxmax()
# print(highest_mid_car_salary_id)
# print(clean_df['Mid-Career Median Salary'].loc[highest_mid_car_salary_id])
print(clean_df.loc[highest_mid_car_salary_id])

# 2. major with lowest starting salary
print("\n2. Major with lowest starting salary:\n")
lowest_starting_salary_id = clean_df['Starting Median Salary'].idxmin()
print(clean_df.loc[lowest_starting_salary_id])

# 3. major with lowest mid-career salary
print("\n2. Major with lowest mid-career salary:\n")
lowest_mid_car_salary_id = clean_df['Mid-Career Median Salary'].idxmin()
print(clean_df.loc[lowest_mid_car_salary_id])

# differences
print("\nIncluded Spread:\n")
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
print(clean_df.head())

print("\nLow risk:\n")
low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())

# 4. Highest potential and greatest spread
print("\nHighest values:")
high_value = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(high_value[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head(), end="\n\nHigh risk:\n")
high_risk = clean_df.sort_values('Spread', ascending=False)
print(high_risk[['Undergraduate Major', 'Spread']].head())

# groupyby
pd.options.display.float_format = '{:,.2f}'.format
print("\nAverage Salary by group:")
print(clean_df.groupby('Group').count())
print("\nAverage salary by group:\n")
print(clean_df.groupby('Group').mean())
