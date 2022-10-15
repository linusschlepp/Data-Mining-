import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Read data from csv file
data = pd.read_csv('US_births_2000-2014.csv', sep=',', dtype='int', header=0)
