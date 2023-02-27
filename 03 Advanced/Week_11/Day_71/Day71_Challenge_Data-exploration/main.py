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
