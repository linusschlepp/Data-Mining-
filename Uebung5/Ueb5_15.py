# Vorlesung Data Mining
# Kapitel 3: Beispiel zu Iris-Bewertung mit oneR
# Edwin Schicker
import numpy as np
import pandas as pd
import random
from utils import train
import sklearn as scn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Datensatz zu Iris laden
data_set = load_iris()
data = data_set['data']
target = data_set['target']
n_data, n_features = data.shape


middle = data.mean(axis=0)
Xdiskr = np.array(data >= middle, dtype='int')
features = np.array(['sepallength','sepalwidth','petallength','petalwidth'])

# Store all data in dataframe
df = pd.DataFrame(Xdiskr, columns=features)
df['iris'] = target
print(df)

lst_df = []
for x in range(1000):

    ran_stream = random.randint(1, 10000)

    df_train, df_test = train_test_split(df, random_state=ran_stream)

    all_predictions = pd.DataFrame(columns=features)
    error = pd.Series(dtype=int)
    for feature in features:
        prediction, err = train(df_train, feature, df_train)
        all_predictions[feature] = prediction
        error[feature] = err

    min_error = error.min()
    best_feature = error.idxmin()
    solution = all_predictions[best_feature]

    df_test['prognose'] = df_test.apply(lambda x: solution[x[best_feature]], axis=1)

    lst_df.append({
        'number': ran_stream,
        'accuracy': 100*np.mean(df_test.prognose == df_test.iris)
    })


sol_df = pd.DataFrame(lst_df).sort_values('accuracy', ascending=False).head(10)
print(sol_df)
