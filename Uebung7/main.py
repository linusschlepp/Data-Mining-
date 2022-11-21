import pandas as pd
import numpy as np
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score
import warnings
from sklearn.naive_bayes import GaussianNB
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data = pd.read_csv('ionosphere.csv', sep=',', header=None)

# Remove all rows, where first coloumn is 0
data = data[data[0] != 0]

# Remove first two columns
data = data.iloc[:,2:]

# Get last row
target = data.iloc[:, -1:]

# Remove last row from dataframe
data.drop(columns=data.columns[-1], axis=1, inplace=True)

ran_stream = 12

x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=ran_stream)
