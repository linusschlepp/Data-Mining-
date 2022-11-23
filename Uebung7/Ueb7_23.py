from main import x_train, y_train, x_test, accuracy_score, y_test, KNeighborsClassifier, pd, plt

dict = {}
for neighbor in range(1, 20):
    model_nb = KNeighborsClassifier(n_neighbors=neighbor)
    model_nb.fit(x_train, y_train)
    prediction = model_nb.predict(x_test)
    accuracy = 100 * accuracy_score(y_test, prediction)
    dict[neighbor] = accuracy
    print('The accuracy for {} is {}'.format(neighbor, accuracy))


df = pd.DataFrame([dict])
print(df)
plt.plot(range(1, 20), df.iloc[0], 'k-')
plt.show()