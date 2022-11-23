from main import *

diabetes_df = pd.read_csv('diabetes_dataset.csv', header=0, sep=',')

model = DecisionTreeClassifier(criterion='entropy', splitter='best')
df = diabetes_df.iloc[:,:-1]
decision = diabetes_df.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(df, decision, test_size=0.2, random_state=15)
print(x_test)
model = model.fit(x_train, y_train)
prediction = model.predict(x_test)

fig = plt.figure(num='Diabetes', figsize=(30, 10))
plot_tree(model, feature_names=df.columns, filled=True, rounded=True, fontsize=3)
plt.show()

# Accuracy is too low
print("Accuracy: {0:.2f}%".format(100 * accuracy_score(y_test, prediction)))
model = DecisionTreeClassifier(criterion="entropy", min_samples_split=0.25, max_depth=3)
model = model.fit(x_train, y_train)
prediction = model.predict(x_test)

# This accuracy is better
print("Accuracy: {0:.2f}%".format(100 * accuracy_score(y_test, prediction)))