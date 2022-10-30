from main import fact_data, pd, product_data, date_data, customer_data, np

# Join all four tables
join1 = pd.merge(left=fact_data, right=product_data, on='PSID')
join2 = pd.merge(left=join1, right=date_data, on='DSID')
join3 = pd.merge(left=join2, right=customer_data, on='CSID')

# Get all rows were artid equals 1000013
join3_query = join3.query("artid==100013")

# Get distinct list of customer ids from join3, who purchased 100013
customer_ids = join3_query['custid'].unique()
# Get all rows from join3, containing distinct customer ids
customer_filtered = join3[join3['custid'].isin(customer_ids)]

# Create pivot of filtered customer list
pivot = pd.pivot_table(customer_filtered, index='name_x', values='quantity',
                       aggfunc=np.sum, margins=True).sort_values('quantity')

# Get rid of last (All) row
new_pivot = pivot.iloc[:-1]

# Get best three customers  (last 3 because sorted ascending)
print(pivot.tail(10))