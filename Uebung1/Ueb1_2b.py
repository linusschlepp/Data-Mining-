from main import data, plt


day_of_week_filter = data.day_of_week == 2
year_data = data[day_of_week_filter].copy()


plt.plot(year_data.index, year_data.births, 'k-')
plt.axis((0, len(year_data.index), 0, 20000))
plt.xlabel('weeks')
plt.ylabel('births')
plt.show()
