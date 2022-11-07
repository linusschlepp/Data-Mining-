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

# in DataFrame alle Daten ablegen
df = pd.DataFrame(Xdiskr, columns=features)
df['iris'] = target
print(df)
sum_dict = df.sum().to_dict()

lst_df = []
simple_lst = ['sepallength', 'sepalwidth', 'petallength', 'iris']


for x in range(1000):

    ran_stream = random.randint(1, 10000)

    df_train, df_test = train_test_split(df, random_state=ran_stream)

    all_predictions = pd.DataFrame(columns=features)
    confidence = pd.Series(dtype=int)
    for feature_1 in features:
        x_a = df[df[feature_1] == 1]
        prediction, err = train(df_train, feature_1, df_train)
        all_predictions[feature_1] = prediction
        for feature_2 in features:
            if feature_2 == feature_1:
                continue
            support = x_a[feature_2].sum()
            confidence[feature_1] = support / sum_dict.get(feature_2)

    sol_df = pd.DataFrame(lst_df)

    max_confidence = confidence.max()
    best_feature = confidence.idxmax()
    solution = all_predictions[best_feature]

    df_test['prognose'] = df_test.apply(lambda x: solution[x[best_feature]], axis=1)

    lst_df.append({
        'number': ran_stream,
        'accuracy': 100*np.mean(df_test.prognose == df_test.iris)
    })

sol_df = pd.DataFrame(lst_df).sort_values('accuracy', ascending=False).head(5)
print(sol_df)
