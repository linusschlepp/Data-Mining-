from main import data, plt

day_of_week_filter = data.year == 2005
year_data = data[day_of_week_filter].copy()

months = range(0, 12)
data_month = year_data.groupby(by='month').sum()
print(data_month)
plt.bar(months, data_month.births)
plt.show()
