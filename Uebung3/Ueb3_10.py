from main import *

facttab = pd.read_csv('facttab.csv', sep=';')
product = pd.read_csv('product.csv', sep=';', usecols=['PSID', 'artid', 'name', 'prodgroup'])
date = pd.read_csv('date.csv', sep=';', usecols=['DSID', 'year', 'monthinyear'])


