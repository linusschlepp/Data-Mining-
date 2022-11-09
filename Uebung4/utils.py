from main import pd, fact_data, product_data


def create_confidence_df(new_fact):
    sum_dict = new_fact.sum().to_dict()
    print(sum_dict)
    # List, storing unique psids
    psid_lst = fact_data['PSID'].unique()
    # store psids and product names in one dictionary
    name_dict = dict(zip(product_data['PSID'], product_data['product_name']))
    print(name_dict)
    lst_df = []
    for prod_1 in psid_lst:
        x_a = new_fact[new_fact[prod_1] == 1]
        for prod_2 in psid_lst:
            if prod_2 == prod_1:
                continue
            support = x_a[prod_2].sum()
            lst_df.append({
                'article_1': name_dict.get(prod_1),
                'article_2': name_dict.get(prod_2),
                'confidence': support / sum_dict.get(prod_1),
                'support': support
            })
    # Sort confidence from big to small, get biggest 5 rows
    sol_df = pd.DataFrame(lst_df).sort_values('confidence', ascending=False).head()

    return sol_df
