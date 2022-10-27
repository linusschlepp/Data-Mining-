import matplotlib.pyplot as plt

from main import *

facttab = pd.read_csv('facttab.csv', sep=';')
product = pd.read_csv('product.csv', sep=';', usecols=['PSID', 'artid', 'name', 'prodgroup'])
date = pd.read_csv('date.csv', sep=';', usecols=['DSID', 'year', 'monthinyear'])

# Join der drei Tabellen:
join1 = pd.merge(left=facttab, right=product, on='PSID')
join2 = pd.merge(left=join1, right=date, on='DSID')

# Filtern nach Jahr und Prodgroup mit query, auf benötigte Spalten reduzieren
herrenrad = join2.query("year==2019 and prodgroup=='Man bicycle'")
ergebnis = herrenrad[['monthinyear', 'quantity', 'name']]

# Gruppieren
gruppiert = ergebnis.groupby(['monthinyear', 'name']).sum().reset_index()

# Filter for individual names
filtered_man_city = gruppiert[gruppiert.name == 'Man City Bike'].copy()
filtered_man_trekking = gruppiert[gruppiert.name == 'Man Trekking Bike'].copy()
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
