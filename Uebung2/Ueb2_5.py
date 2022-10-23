from main import *

# Drop all column
del pivot['All']

# Create max column
pivot['max'] = pivot.max(axis=1)

# Create max_month column
pivot['max_month'] = pivot.idxmax(axis=1)
print(pivot)

# Safe pivot as .csv-file
pivot.to_csv('pivot.csv', sep=';')
