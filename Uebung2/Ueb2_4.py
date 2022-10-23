from main import *

# Get max_births in whole timeline
max_births = data['births'].max()

# Filter for max_births
filtered_data = data[data['births'] == max_births].copy()
max_year = filtered_data.values.item(0)
max_month = filtered_data.values.item(1)
max_date_month = filtered_data.values.item(2)
max_births = filtered_data.values.item(4)


print('Most births occurred on {}.{}.{} : {} '.format(max_year, max_month, max_date_month, max_births))

# Filter for given month
filtered_data = data[data.month == max_month].copy()

# Re-filter for given year
filtered_data = filtered_data[filtered_data.year == max_year].copy()
plt.bar(range(0, 30), filtered_data['births'])
plt.ylabel('Births')
plt.xlabel('Day in month')
plt.title('Amount of births in {}.{}'.format(max_month, max_year))
plt.show()