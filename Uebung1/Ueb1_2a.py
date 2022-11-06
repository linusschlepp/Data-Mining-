from main import data, plt, min_year, max_year

# On which day (Monday - Sunday) happened the most births?

# Group by day_of_week
group_week_day = data.groupby(by='day_of_week').sum()
# Get all days of week (1-7)
#days_of_week = range(0, 7)

# Get births from dataset
births = group_week_day['births']
print(births)
plt.bar(births.index, births)
plt.title('Total births per day of week from {} to {}'.format(min_year, max_year))
plt.xlabel('Day of week')
plt.ylabel('Births')
plt.show()