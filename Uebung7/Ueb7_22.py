from main import  KNeighborsClassifier, accuracy_score, x_train, y_test, x_test, y_train

model_nb = KNeighborsClassifier(n_neighbors=8)
model_nb.fit(x_train, y_train)
prediction = model_nb.predict(x_test)
print("The accuracy is {0:.2f}%".format(100 * accuracy_score(y_test, prediction)))





