from main import data, plt

# Purely integer-location indexing selection, print first 31 objects within dataframe
january = data.iloc[:31]  # Get data of january, first 31 days
# Print january
print(january)  # Print data

# Draw multiple plots within one figure
plt.subplot(211)
plt.plot(january.index + 1, january['births'], 'b--')
plt.axis([0, 32, 0, 20000])
plt.xlabel('January 2000')
plt.ylabel('Births')

# Input year
year = int(input())
year_filter = data.year == year
year_data = data[year_filter]
year_data.index = year_data.index - year_data.index[0] + 1

plt.subplot(212)
plt.plot(year_data.index, year_data['births'], 'k-')
plt.axis([0, 367, 0, 20000])  # xmin,xmax,ymin,ymax
plt.xlabel('All days in ' + str(year))
plt.ylabel('Births')
plt.show()
