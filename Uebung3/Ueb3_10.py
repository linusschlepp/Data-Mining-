from main import join_1, pd, date_data, product_data

# Filter for state bavaria (Bayern)
filter_1 = join_1[join_1['state'] == 'Bayern']
join_2 = pd.merge(left=filter_1, right=date_data, on='DSID')
filter_2 = join_2[join_2['month'] == 201902]
join_3 = pd.merge(left=filter_2, right=product_data, how='right', on='PSID')
filter_3 = join_3[join_3['prodgroup'] == 'Lady bicycle']

solution = filter_3[['artid', 'name_y', 'quantity']]
grouped = solution.groupby(['artid', 'name_y']).sum().reset_index()

grouped.set_index('artid', inplace=True)
grouped.quantity = grouped.quantity.astype(float)

# All ladies-bikes, bought in 2019 by bavarian customers
print(grouped)