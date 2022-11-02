import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fact_data = pd.read_csv('facttab.csv', sep=';')
product_data = pd.read_csv('product.csv', sep=';', usecols=['PSID', 'artid', 'name', 'prodgroup'])
date_data = pd.read_csv('date.csv', sep=';', usecols=['DSID', 'year', 'monthinyear', 'month'])
customer_data = pd.read_csv('customer.csv', sep=';')


join_1 = pd.merge(left=fact_data, right=customer_data, on='CSID')
join_1.to_csv('test.csv')


