import numpy as np
import pandas as pd
import matplotlib
import random as ran
import sklearn as scn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Load dataset for iris
data_set = load_iris()
data = data_set['data']
target = data_set['target']
n_data, n_features = data.shape

min_value = data.min(axis=0)
max_value = data.max(axis=0)
middle = data.mean(axis=0)
quarter = (middle + min_value) / 2
three_quarter = (max_value + middle) / 2
x_temp_1 = np.array(data >= quarter, dtype='int')
x_temp_2 = np.array(data >= middle, dtype='int')
x_temp_3 = np.array(data >= three_quarter, dtype='int')
df_disc_quarter = x_temp_1 + x_temp_2 + x_temp_3
features = np.array(['sepallength', 'sepalwidth', 'petallength', 'petalwidth'])

# Store all data in dataframe, values inside dataframe, range from 0 to 4
df_quarter = pd.DataFrame(df_disc_quarter, columns=features)
df_quarter['iris'] = target


df_disc_middle = np.array(data >= middle, dtype='int')

# Store all data in dataframe, values inside dataframe, range from 0 to 1
df_middle = pd.DataFrame(df_disc_middle, columns=features)
df_middle['iris'] = target

