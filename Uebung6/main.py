import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as scn
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

scn.set()
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris


data_set = load_iris()
data = data_set.data
target = data_set.target
features = np.array(['sepallength', 'sepalwidth', 'petallength', 'petalwidth'])
df = pd.DataFrame(data, columns=features)
