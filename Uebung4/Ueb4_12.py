from main import fact_data, product_data, pd, customer_data


new_df = pd.merge(left=fact_data, right=product_data, on='PSID')
new_df = pd.merge(left=new_df, right=customer_data, on='CSID')

new_df=new_df[['custid', 'customer_name', 'artid', 'product_name']]
# Create new column inside new_df
new_df['amount'] = 0

# Group and sort (ascending: custid, descending: amount):
new_df = new_df.groupby(['custid', 'customer_name', 'artid', 'product_name']).count().reset_index()
new_df = new_df.sort_values(['custid', 'amount'], ascending=[True, False])

# New empty dataframe is created, containing all columns of X
solution = pd.DataFrame(columns=new_df.columns)
for cust_id in customer_data['custid'].values:
    #  get first 3 rows of individual custid (are the top 3 products because is sorted descending)
    temp = new_df[new_df.cust_id == cust_id].iloc[:3]
    solution = pd.concat([solution, temp])

print(solution)