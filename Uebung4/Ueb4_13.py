from main import *

new_fact = pd.read_csv('facttab.csv', sep=';', header= 0, usecols=['ordid','PSID'])
new_fact = new_fact.groupby(['ordid', 'PSID']).size().unstack(fill_value=0).astype('int')
print(new_fact)

lst = fact_data['PSID'].unique()
sol_lst = {}

for col in lst:
    x_a = new_fact[new_fact[col] == 1]
    for col_1 in lst:
        if col_1 == col:
            continue
        correct = x_a[col_1].sum()
        sol_lst[(col_1, col)] = correct

print(sol_lst)
sol_lst = sorted(sol_lst, key=sol_lst.get, reverse=True)[:5]
print(sol_lst)







