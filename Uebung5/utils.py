from main import pd


def train(df, feature, df_train):
    values = df[feature].unique()  # safe values
    prediction = pd.Series(index=values, dtype=int)  # fields for predictions
    error = 0
    # Calculate all preditcions and errors within loop
    for value in values:
        iris, err = train_feature_value(feature, value, df_train)
        prediction[value] = iris
        error += err

    return prediction, error


# Calculate amount of 'hits' for all three iris-types (0 to 2), dependent of feature and value
def train_feature_value(feature, value, df_train):
    df_help = df_train[df_train[feature] == value]  # only rows, of the which Feature holds the value
    iris_counter = df_help.iris.value_counts()  # counts iris appearances
    imax = iris_counter.idxmax()  # most common iris
    error = iris_counter.sum() - iris_counter.max()  # Amount of error: all - max
    return imax, error


# Calculates error and returns it as a dataframe
def calculate_error(features, df_train):
    all_predictions = pd.DataFrame(columns=features)
    error = pd.Series(dtype=int)
    for feature in features:
        prediction, err = train(df_train, feature, df_train)
        all_predictions[feature] = prediction
        error[feature] = err

    return all_predictions, error


# Calculates confidence and returns it as a dataframe
def calculate_confidence(features, df_middle, df_train, sum_dict):
    all_predictions = pd.DataFrame(columns=features)
    confidence = pd.Series(dtype=int)
    for feature_1 in features:
        x_a = df_middle[df_middle[feature_1] == 1]
        prediction, err = train(df_train, feature_1, df_train)
        all_predictions[feature_1] = prediction
        for feature_2 in features:
            if feature_2 == feature_1:
                continue
            support = x_a[feature_2].sum()
            confidence[feature_1] = support / sum_dict.get(feature_2)

    return all_predictions, confidence
