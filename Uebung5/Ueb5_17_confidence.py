from main import np, df_quarter, train_test_split, pd, features, df_middle
from utils import calculate_confidence

sum_dict = df_quarter.sum().to_dict()

# Has scored 84% in 16
ran_stream = 9946

df_train, df_test = train_test_split(df_quarter, random_state=ran_stream)

all_predictions = pd.DataFrame(columns=features)

confidence = calculate_confidence(features, df_middle, df_train, all_predictions, sum_dict)
best_feature = confidence.idxmax()
solution = all_predictions[best_feature]

df_test['prognose'] = df_test.apply(lambda x: solution[x[best_feature]], axis=1)

print('The accuracy, scored with {} is: {:.2f}%'.format(ran_stream, 100*np.mean(df_test.prognose == df_test.iris)))


