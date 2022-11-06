from main import data, plt, min_year, max_year, np, pd


# Create pivot-table
pivot = pd.pivot_table(data, index="year", columns="month", values="births",
                       aggfunc=np.sum, margins=True)

# Delete column 'All' inside pivot
del pivot['All']

# Create Column 'max' and column 'min' inside pivot
pivot['max'] = pivot.max(axis=1)
pivot['min'] = pivot.min(axis=1)

print(pivot)

pivot.to_csv('pivot.csv', sep=';')

# Get 'max'-col within pivot-table
max_col = pivot['max']
print(max_col)

# Get all but the last rows in series to avoid the last row (All)
plt.bar(max_col.iloc[:-1].index, max_col.iloc[:-1])
plt.title('Total amount of births per year from {} to {}'.format(min_year, max_year))
plt.xlabel('Years')
plt.ylabel('Births')
plt.show()

