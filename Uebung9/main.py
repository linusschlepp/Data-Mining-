import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv('automobile85.csv')
x_columns = ['horsepower', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-size', 'compression-ratio',
             'city-mpg', 'highway-mpg']

y_column = ['price']
x_all = data.loc[:, x_columns]
y = data[y_column]

fish_data = pd.read_csv('Fish.csv')
fish_target = fish_data.iloc[:, 0]
fish_data_data = fish_data.iloc[:,-4:]

X_all = fish_data.iloc[:, 2:]  # All length and width
y_fish = fish_data.iloc[:, 1]  # Weight

X = X_all[["Length3"]]  # Length3 is chosen
x_train, x_test, y_train, y_test = train_test_split(X, y_fish, test_size=0.3)  # Use 70% of the data for training
