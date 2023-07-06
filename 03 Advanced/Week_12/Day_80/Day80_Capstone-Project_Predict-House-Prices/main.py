import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Import and Options

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
plt.figure(figsize=(8, 4), dpi=200)
sns.displot(data=data,
            x='PRICE',
            aspect=2, )
plt.show()

# Distance to Employment - Length of Commute

plt.figure(figsize=(8, 4), dpi=200)
sns.displot(data=data,
            x='DIS',
            aspect=2, )
plt.show()

# Number of Rooms

plt.figure(figsize=(8, 4), dpi=200)
sns.displot(data=data,
            x='RM',
            aspect=2, )
plt.show()

# Access to Highways

plt.figure(figsize=(8, 4), dpi=200)
sns.displot(data=data,
            x='RAD',
            aspect=2, )
plt.show()

# Next to the River?

grouped_properties = data['CHAS'].value_counts()
print(grouped_properties)

plt.figure(figsize=(14, 8))
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

# Split Training & Test Dataset

target = data['PRICE']
features = data.drop('PRICE', axis=1)

X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size=0.2,
                                                    random_state=10)

# Information about Test Data

train_pct = 100 * len(X_train) / len(features)
print(f'Training data is {train_pct:.3}% of the total data.')

test_pct = 100 * X_test.shape[0] / features.shape[0]
print(f'Test data makes up the remaining {test_pct:0.3}%.')

# Multivariable Regression

regression = LinearRegression()
regression.fit(X_train, y_train)
rsquared = regression.score(X_train, y_train)
rcoef = regression.coef_
print(f"Theta zero: {regression.intercept_}")
print(f"Theta one: {rcoef}")
print(f"R-squared: {rsquared}")

# Evaluate the Coefficients of the Model

regression_data = pd.DataFrame(data=rcoef, index=X_train.columns, columns=['Coefficient'])
print(regression_data)

premium = regression_data.loc['RM'].values[0] * 1000
print(f'The price premium for having an extra room is ${premium:.5}')

# Analyse the Estimated Values & Regression Residuals

predicted_vals = regression.predict(X_train)
residuals = (y_train - predicted_vals)

plt.figure(dpi=100)
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Actual vs Predicted Prices: $y _i$ vs $\hat y_i$', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\hat y _i$', fontsize=14)
plt.show()
print()

plt.figure(dpi=100)
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Residuals vs Predicted Values', fontsize=17)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Residuals skew and mean

resid_mean = round(residuals.mean(), 2)
resid_skew = round(residuals.skew(), 2)

sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Residuals Skew ({resid_skew}) Mean({resid_mean})')

# Data Transformations for a Better Fit

tgt_skew = data['PRICE'].skew()
sns.displot(data['PRICE'], kde='kde', color='green')
plt.title(f'Normal Prices. Skew is {tgt_skew:.3}')
plt.show()

y_log = np.log(data['PRICE'])
sns.displot(y_log, kde=True)
plt.title(f'Log Prices. Skew is {y_log.skew():.3}')
plt.show()

# How does the log transformation work?

plt.figure(dpi=150)
plt.scatter(data.PRICE, np.log(data.PRICE))

plt.title('Mapping the Original Price to a Log Price')
plt.ylabel('Log Price')
plt.xlabel('Actual $ Price in 000s')
plt.show()

# Regression using Log Prices

new_target = np.log(data['PRICE'])
features = data.drop('PRICE', axis=1)

X_train, X_test, log_y_train, log_y_test = train_test_split(features,
                                                            new_target,
                                                            test_size=0.2,
                                                            random_state=10)

log_regr = LinearRegression()
log_regr.fit(X_train, log_y_train)
log_rsquared = log_regr.score(X_train, log_y_train)

log_predictions = log_regr.predict(X_train)
log_residuals = (log_y_train - log_predictions)

print(f'Training data r-squared: {log_rsquared:.2}')

# Evaluating Coefficients with Log Prices

df_coef = pd.DataFrame(data=log_regr.coef_, index=X_train.columns, columns=['coef'])
print(df_coef)

# Regression with Log Prices & Residual Plots

# Graph of Actual vs. Predicted Log Prices
plt.scatter(x=log_y_train, y=log_predictions, c='navy', alpha=0.6)
plt.plot(log_y_train, log_y_train, color='cyan')
plt.title(f'Actual vs Predicted Log Prices: $y _i$ vs $\hat y_i$ (R-Squared {log_rsquared:.2})', fontsize=17)
plt.xlabel('Actual Log Prices $y _i$', fontsize=14)
plt.ylabel('Prediced Log Prices $\hat y _i$', fontsize=14)
plt.show()

# Original Regression of Actual vs. Predicted Prices
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Original Actual vs Predicted Prices: $y _i$ vs $\hat y_i$ (R-Squared {rsquared:.3})', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\hat y _i$', fontsize=14)
plt.show()

# Residuals vs Predicted values (Log prices)
plt.scatter(x=log_predictions, y=log_residuals, c='navy', alpha=0.6)
plt.title('Residuals vs Fitted Values for Log Prices', fontsize=17)
plt.xlabel('Predicted Log Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Original Residuals vs Fitted Values', fontsize=17)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Calculate mean and the skew

# Distribution of Residuals (log prices) - checking for normality
log_resid_mean = round(log_residuals.mean(), 2)
log_resid_skew = round(log_residuals.skew(), 2)

sns.displot(log_residuals, kde=True, color='navy')
plt.title(f'Log price model: Residuals Skew ({log_resid_skew}) Mean ({log_resid_mean})')
plt.show()

sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Original model: Residuals Skew ({resid_skew}) Mean ({resid_mean})')
plt.show()

# Compare Out of Sample Performance

print(f'Original Model Test Data r-squared: {regression.score(X_test, y_test):.2}')
print(f'Log Model Test Data r-squared: {log_regr.score(X_test, log_y_test):.2}')

# Predict a Property's Value using the Regression Coefficients

# Starting Point: Average Values in the Dataset
features = data.drop(['PRICE'], axis=1)
average_vals = features.mean().values
property_stats = pd.DataFrame(data=average_vals.reshape(1, len(features.columns)),
                              columns=features.columns)
print(property_stats)

# Make prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Convert Log Prices to Acutal Dollar Values
dollar_est = np.e**log_estimate * 1000
# or use
dollar_est = np.exp(log_estimate) * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')

# Define Property Characteristics
next_to_river = True
nr_rooms = 8
students_per_classroom = 20
distance_to_town = 5
pollution = data.NOX.quantile(q=0.75) # high
amount_of_poverty =  data.LSTAT.quantile(q=0.25) # low

# Solution:
# Set Property Characteristics
property_stats['RM'] = nr_rooms
property_stats['PTRATIO'] = students_per_classroom
property_stats['DIS'] = distance_to_town

if next_to_river:
    property_stats['CHAS'] = 1
else:
    property_stats['CHAS'] = 0

property_stats['NOX'] = pollution
property_stats['LSTAT'] = amount_of_poverty

# Make prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Convert Log Prices to Acutal Dollar Values
dollar_est = np.e**log_estimate * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')
