import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Read data from csv files
date_data = pd.read_csv('date.csv', sep=';', dtype='str', header=0)
product_data = pd.read_csv('product.csv', sep=';', dtype='str', header=0)
fact_data = pd.read_csv('facttab.csv', sep=';', dtype='str', header=0)