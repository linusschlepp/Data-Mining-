from main import plt, pivot, data

# Get year with most births inside pivot
year_most_births = pivot['All'].iloc[:-1].idxmax()
# Filter data for corresponding year
filtered_data = data[data['year'] == year_most_births].copy()

# Change index, 0 - 364
filtered_data.reset_index(drop=True, inplace=True)

# Group previously filtered data
group_filtered_data = filtered_data.groupby(by='month').sum()
print(filtered_data)

# Plot filtered data
plt.plot(group_filtered_data.index, group_filtered_data['births'], 'k-')
plt.xlabel('Months')
plt.ylabel('births')

# Get average amount of births
birth_avg = filtered_data.births.mean()

# Filter births above average
more_births_avg = filtered_data[filtered_data.births > birth_avg].copy()

# Filter births below average
less_births_avg = filtered_data[filtered_data.births < birth_avg].copy()
print('Birth average: {}'.format(birth_avg))
print(more_births_avg)
print(less_births_avg)

plt.show()