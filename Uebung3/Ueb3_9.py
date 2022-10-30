from main import *

facttab = pd.read_csv('facttab.csv', sep=';')
product = pd.read_csv('product.csv', sep=';', usecols=['PSID', 'artid', 'name', 'prodgroup'])
date = pd.read_csv('date.csv', sep=';', usecols=['DSID', 'year', 'monthinyear'])
customer = pd.read_csv('customer.csv', sep=';')

# Join all four tables
join1 = pd.merge(left=facttab, right=product, on='PSID')
join2 = pd.merge(left=join1, right=date, on='DSID')
join3 = pd.merge(left=join2, right=customer, on='CSID')

join3.to_csv('test.csv')
herrenrad = join3.query("artid==100013")
lst = herrenrad['custid'].unique()
print(lst)
test = join3[join3['custid'].isin(lst)]
print(test['name_x'].unique())

pivot = pd.pivot_table(test, index='name_x',  values='quantity',
                       aggfunc=np.sum, margins=True).sort_values('quantity')

# Get rid of last (All) row
new_pivot = pivot.iloc[:-1]

# Get best three customers  (last 3 because sorted ascending)
print(pivot.tail(10))