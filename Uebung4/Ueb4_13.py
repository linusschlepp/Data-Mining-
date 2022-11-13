from main import pd
from utils import create_confidence_df

new_fact = pd.read_csv('facttab.csv', sep=';', header= 0, usecols=['ordid','PSID'])
new_fact = new_fact.groupby(['ordid', 'PSID']).size().unstack(fill_value=0).astype('int')

sol_df = create_confidence_df(new_fact)
sol_df.to_csv('test_13.csv')
print(sol_df)







