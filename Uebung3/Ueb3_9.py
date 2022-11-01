from main import fact_data, pd, product_data, date_data, customer_data, np

join = pd.merge(left=fact_data, right=product_data, on='PSID')

# Get all orders with artid 100013
orders = join[join['artid'] == 100013].ordid
solution = pd.merge(left=join, right=orders, on='ordid')

solution = solution[['artid', 'name', 'quantity']]
grouped = solution.groupby(['artid', 'name']).sum().reset_index()
grouped_sort = grouped.nlargest(10, ['quantity'])
grouped_sort.set_index('artid', inplace=True)

# print(grouped_sort[1:])
