import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Read data from csv files
# date_data = pd.read_csv('date.csv', sep=';', dtype='str', header=0, usecols=['DSID', 'year', 'monthinyear'])
# product_data = pd.read_csv('product.csv', sep=';', dtype='str', header=0, usecols=['PSID', 'artid', 'name', 'prodgroup'])
# fact_data = pd.read_csv('facttab.csv', sep=';', dtype='str', header=0)
# customer_data = pd.read_csv('customer.csv', sep=';', dtype='str', header=0)

fact_data = pd.read_csv('facttab.csv', sep=';')
product_data = pd.read_csv('product.csv', sep=';', usecols=['PSID', 'artid', 'name', 'prodgroup'])
date_data = pd.read_csv('date.csv', sep=';', usecols=['DSID', 'year', 'monthinyear', 'month'])
customer_data = pd.read_csv('customer.csv', sep=';')


# Join on common rows
join_1 = pd.merge(left=fact_data, right=customer_data, on='CSID')
join_2 = pd.merge(left=join_1, right=product_data, on='PSID')
join_3 = pd.merge(left=join_2, right=customer_data, on='CSID')
