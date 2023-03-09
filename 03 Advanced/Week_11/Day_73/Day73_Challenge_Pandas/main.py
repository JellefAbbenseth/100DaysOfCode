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

# Aggregate Data with the Python .agg() Function

themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
print(themes_by_year.head(), end='\n')
print(themes_by_year.tail(), end='\n\n')

plt.figure(figsize=(10,6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of themes', fontsize=14)
plt.ylim(0, 100)
plt.plot(themes_by_year.index[:-2], themes_by_year.theme_id[:-2])
plt.show()

plt.figure(figsize=(10,6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.theme_id[:-2], color='b')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Sets', fontsize=14, color='green')
ax2.set_ylabel('Number of Themes', fontsize=14, color='blue')

plt.show()

parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
print(parts_per_set.head(), end='\n')
print(parts_per_set.tail(), end='\n\n')

plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
plt.show()

set_theme_count = sets['theme_id'].value_counts()
print(set_theme_count[:5], end="\n")

themes = pd.read_csv('data/themes.csv', names=['id', 'name', 'parent_id'], header=0)
print(themes.head(), end="\n")
print(themes[themes.name == 'Star Wars'], end="\n")
print(sets[sets.theme_id == 18], end="\n")
print(sets[sets.theme_id == 209], end="\n\n")

set_theme_count = sets["theme_id"].value_counts()
print(set_theme_count[:5], end="\n")

set_theme_count = pd.DataFrame({'id':set_theme_count.index, 'set_count':set_theme_count.values})
print(set_theme_count.head(), end="\n")

merged_df = pd.merge(set_theme_count, themes, on='id')
print(merged_df[:3], end="\n\n")

plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()


