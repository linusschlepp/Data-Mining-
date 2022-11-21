from main import plt, train_test_split, KNeighborsClassifier, accuracy_score, data, target

image = plt.figure(num="Nearest Neighbors", figsize=(8, 5))
content = image.add_subplot()
content.set_title("Nearest Neighbors with different parameters")
content.set_xlabel("Amount Neighbors");content.set_ylabel("Confidence")
color = ['#FF0000', '#FFFF00', '#00FF00', '#00FFFF', '#0000FF', '#FF00FF']

parameter = range(1, 21)
for stream in range(12, 17):
    x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=stream)

    accuracy = []

    for neighbor in parameter:
        model = KNeighborsClassifier(n_neighbors=neighbor)
        model.fit(x_train, y_train)
        prediction = model.predict(x_test)
        accuracy.append(100 * accuracy_score(y_test, prediction))
    content.plot(parameter, accuracy, color=color[stream - 12], label=str(stream))

content.legend()
plt.show()