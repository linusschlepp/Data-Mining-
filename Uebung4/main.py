import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fact_data = pd.read_csv('facttab.csv', sep=';', header= 0, usecols=['ordid','PSID','CSID','DSID'])
product_data = pd.read_csv('product.csv', sep=';', header=0, usecols=['PSID', 'artid', 'name'])
date_data = pd.read_csv('date.csv', sep=';', header=0, usecols=['DSID', 'year', 'monthinyear', 'month'])
customer_data = pd.read_csv('customer.csv', header=0,  sep=';', usecols=["CSID","custid","name"])

# Rename columns with same name
product_data.rename(columns={'name': 'product_name'}, inplace=True)
customer_data.rename(columns={'name': 'customer_name'}, inplace=True)




