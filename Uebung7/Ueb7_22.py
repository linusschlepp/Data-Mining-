from main import pd, KNeighborsClassifier, train_test_split, np, precision_score, accuracy_score

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

model_nb = KNeighborsClassifier(n_neighbors=8)
model_nb.fit(x_train, y_train)
prediction = model_nb.predict(x_test)
print("The accuracy is {0:.2f}%".format(100 * accuracy_score(y_test, prediction)))





