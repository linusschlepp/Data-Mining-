from main import plt, train_test_split, GaussianNB, accuracy_score, data, target, recall_score

image = plt.figure(num="Gaussian Naive Bayes", figsize=(8, 5))
content = image.add_subplot()
content.set_title("Gaussian Naive Bayes with random numbers")
content.set_xlabel("Amount Neighbors")
content.set_ylabel("Confidence")

accuracy = []
for stream in range(12, 17):
    x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=stream)
    model = GaussianNB()
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    accuracy.append(100 * accuracy_score(y_test, prediction))

content.bar(range(12, 17), accuracy)

content.legend()
plt.show()

print('Accuracy: {0:.2f}'.format(100 * accuracy_score(y_test, prediction)))
print('Recall: {0:.2F}'.format(100 * recall_score(y_test, prediction, pos_label='g')))
print('Precision: {0:.2F}'.format(100 * recall_score(y_test, prediction, pos_label='g')))

print('Amount of elements of class: {}'.format(model.class_count_))
