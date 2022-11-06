from main import data, plt, min_year, max_year

# Set filter for 2nd day of week
day_of_week_filter = data.day_of_week == 2


# Get filtered data
filtered_data = data[day_of_week_filter].copy()

plt.plot(filtered_data.index, filtered_data.births, 'k-')
print(filtered_data)
plt.title('Amount of births on Tuesday per week from {} to {}'.format(min_year, max_year))
plt.axis((0, len(filtered_data.index), 0, 20000))
plt.xlabel('weeks')
plt.ylabel('births')
plt.show()

# Within the plot, we could see that certain anomalies occurred (births dropped under 8000 in this week)
# On which weeks did this happen?
weekly_anomalies = filtered_data[filtered_data.births < 8000].copy()
# Shows when anomalies happened, in days starting at 1.1.2000
print(weekly_anomalies)
