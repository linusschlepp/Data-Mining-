from main import pd, fact_data, date_data, product_data

filtered_date = date_data[date_data['year'] == 2019].copy()
print(filtered_date)

print('Only consider january? Enter y for yes, press enter for no')
only_january = str(input()) == 'y'

join_1 = pd.merge(fact_data, filtered_date, on='DSID', how='outer')

join_1 = join_1[join_1['year'] == 2019].copy()
if only_january:
    join_1 = join_1[join_1['monthinyear'] == 1].copy()



print(join_1)

new_fact = join_1.groupby(['ordid', 'PSID']).size().unstack(fill_value=0).astype('int')
sum_dict = new_fact.sum().to_dict()
print(sum_dict)

# List, storing unique psids
psid_lst = fact_data['PSID'].unique()
# store psids and product names in one dictionary
name_dict = dict(zip(product_data['PSID'], product_data['product_name']))
print(name_dict)
# Solution-dataframe will later be recreated from this list
lst_df = []
for prod_1 in psid_lst:
    x_a = new_fact[new_fact[prod_1] == 1]
    for prod_2 in psid_lst:
        if prod_2 == prod_1:
            continue
        support = x_a[prod_2].sum()
        lst_df.append({
            'article_1' : name_dict.get(prod_1),
            'article_2' : name_dict.get(prod_2),
            'confidence' : support/sum_dict.get(prod_1),
            'support' : support
        })


sol_df = pd.DataFrame(lst_df).sort_values('confidence', ascending=False).head()
sol_df.to_csv('test_1.csv')
print(sol_df)