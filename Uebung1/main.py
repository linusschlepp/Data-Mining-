import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Read data from csv file
data = pd.read_csv('US_births_2000-2014.csv', sep=',', dtype='int', header=0)

min_year = str(data.year.min())
max_year = str(data.year.max())
