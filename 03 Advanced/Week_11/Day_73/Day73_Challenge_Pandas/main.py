import pandas as pd
import matplotlib.pyplot as plt

# original in colaboratory

colors = pd.read_csv('data/colors.csv', names=['name', 'rgb', 'is_trans'], header=0)
print(colors.head())

print(colors['name'].nunique())

print(colors.groupby('is_trans').count())

print(colors.is_trans.value_counts())

sets = pd.read_csv('data/sets.csv', names=['set_num', 'name', 'year', 'theme_id', 'num_parts'], header=0)
print(sets.head())
print(sets.tail())

print(sets.sort_values('year').head())

print(sets[sets['year'] == sets['year'].min()])

print(sets.sort_values('num_parts', ascending=False).head())

sets_by_year = sets.groupby('year').count()
print(sets_by_year['set_num'].head())
# print(sets_by_year['set_num'].max())

print(sets_by_year['set_num'].tail())

plt.figure(figsize=(10,6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of sets sold', fontsize=14)
plt.ylim(0, 900)
plt.plot(sets_by_year.index, sets_by_year.set_num)
plt.show()

plt.figure(figsize=(10,6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of sets sold', fontsize=14)
plt.ylim(0, 900)
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
plt.show()


