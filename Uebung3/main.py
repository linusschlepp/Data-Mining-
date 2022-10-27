import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Read data from csv files
date_data = pd.read_csv('date.csv', sep=';', dtype='str', header=0)
product_data = pd.read_csv('product.csv', sep=';', dtype='str', header=0)
fact_data = pd.read_csv('facttab.csv', sep=';', dtype='str', header=0)
customer_data = pd.read_csv('customer.csv', sep=';', dtype='str', header=0)


# Join on common rows
join1 = pd.merge(left=fact_data, right=customer_data, on='CSID')
join2 = pd.merge(left=join1, right=product_data, on='PSID')