from main import np, df_quarter, train_test_split, pd, features
from utils import calculate_error


# Has scored 81% in Ueb5_15
ran_stream = 2520

df_train, df_test = train_test_split(df_quarter, random_state=ran_stream)

all_predictions = pd.DataFrame(columns=features)

error = calculate_error(features, df_train, all_predictions)
best_feature = error.idxmin()
solution = all_predictions[best_feature]

df_test['prognose'] = df_test.apply(lambda x: solution[x[best_feature]], axis=1)

print('The accuracy, scored with {} is: {:.2f}%'.format(ran_stream, 100*np.mean(df_test.prognose == df_test.iris)))
