from main import pd, fact_data, date_data
from utils import create_confidence_df

filtered_date = date_data[date_data['year'] == 2019].copy()
print(filtered_date)

join_1 = pd.merge(fact_data, filtered_date, on='DSID', how='outer')

join_1 = join_1[join_1['year'] == 2019].copy()
if str(input('Only consider january? Enter y for yes, press enter for no')) == 'y':
    join_1 = join_1[join_1['monthinyear'] == 1].copy()
print(join_1)
new_fact = join_1.groupby(['ordid', 'PSID']).size().unstack(fill_value=0).astype('int')

# Solution-dataframe will later be recreated from this list
sol_df = create_confidence_df(new_fact)
sol_df.to_csv('test_14.csv')
print(sol_df)
