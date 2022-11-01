from main import join_2, pd, np

# Convert datatypes of specific columns, into required datatypes (float, int)
join_2['price'] = join_2['price'].astype(float)
join_2['quantity'] = join_2['quantity'].astype(int)
# Create total price column, by multiplying the individual price with the quantity
join_2['total_price'] = join_2['price'] * join_2['quantity']

pivot = pd.pivot_table(join_2, index='custid', values='total_price',
                       aggfunc=np.sum, margins=True)

# Sort values ascending from pivot
new_pivot = pivot.sort_values('total_price')

# Get rid of last (All) row
new_pivot = new_pivot.iloc[:-1]

# Get best three customers  (last 3 because sorted ascending)
print(new_pivot.tail(3))


