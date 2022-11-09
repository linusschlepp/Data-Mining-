from utils import calculate_error
from main import np, ran, train_test_split, pd, features, df_middle

lst_df = []
for x in range(1000):
    ran_stream = ran.randint(1, 10000)

    df_train, df_test = train_test_split(df_middle, random_state=ran_stream)

    all_predictions, error = calculate_error(features, df_train)
    min_error = error.min()
    best_feature = error.idxmin()
    solution = all_predictions[best_feature]

    df_test['prognose'] = df_test.apply(lambda x: solution[x[best_feature]], axis=1)

    lst_df.append({
        'number': ran_stream,
        'accuracy': 100 * np.mean(df_test.prognose == df_test.iris)
    })

sol_df = pd.DataFrame(lst_df).sort_values('accuracy', ascending=False).head(10)
print(sol_df)
