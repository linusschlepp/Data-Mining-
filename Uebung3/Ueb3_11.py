from main import date_data, pd, plt, np, fact_data, product_data

# Filter for year and prodgroup, reduce to needed columns
join_1 = pd.merge(left=fact_data, right=product_data, on='PSID')
join_2 = pd.merge(left=join_1, right=date_data, on='DSID')
man_bike = join_2.query("year==2019 and prodgroup=='Man bicycle'")
solution = man_bike[['monthinyear', 'quantity', 'name']]

# Group
grouped = solution.groupby(['monthinyear', 'name']).sum().reset_index()

"""
My Addition to given example from lecture
"""
# Filter for individual names
filtered_man_city = grouped[grouped.name == 'Man City Bike'].copy()
filtered_man_trekking = grouped[grouped.name == 'Man Trekking Bike'].copy()
print(filtered_man_city)
print(filtered_man_trekking)

# Create bar chart
x_axis = np.arange(len(filtered_man_trekking))
plt.bar(x_axis - 0.2, filtered_man_city.quantity, 0.4, label=filtered_man_city.name.values[0])
plt.bar(x_axis + 0.2, filtered_man_trekking.quantity, 0.4, label=filtered_man_trekking.name.values[0])
print(filtered_man_trekking.name.values[0])
plt.xticks(x_axis, filtered_man_trekking.monthinyear)

plt.xlabel('Months')
plt.ylabel('Quantity')
plt.legend()
plt.show()
