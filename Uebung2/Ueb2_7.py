from main import plt, data, min_year, max_year

plt.hist(data['births'])
plt.ylabel('Occurrence in Timeline')
plt.xlabel('Amount of Births')
plt.title('Amount of births in given timeline: from {} to {}'.format(min_year, max_year))
# Show first histogram, containing data, over whole timeline
plt.show()

print('Enter specific year')
input_year = int(input())

# Filter data for specific year
filtered_data = data[data.year == input_year].copy()
plt.hist(filtered_data['births'])
plt.xlabel('Amount of births')
plt.ylabel('Occurrence in {}'.format(input_year))
plt.title('Amount of births in: {}'.format(input_year))
# Show histogram, only for given year
plt.show()


