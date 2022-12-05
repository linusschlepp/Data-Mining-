from main import PolynomialFeatures, train_test_split, y, x_all, LinearRegression, plt

x = x_all[['horsepower']]

dict_test = {}
dict_train = {}
figure = plt.figure(num='Polymorphic Regression', figsize=(12, 10))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
image = figure.add_subplot()

#image.scatter(x_train, y_train, color='blue')
#image.scatter(x_test, y_test, color='green')
x_train = x_train.replace(['?'], 0)
x_test = x_test.replace(['?'], 0)
y_train = y_train.replace(['?'], 0)
y_test = y_test.replace(['?'], 0)

for pol_degree in range(2, 10):
    poly = PolynomialFeatures(degree=pol_degree)
    x_train_model = poly.fit_transform(x_train)
    x_test_model = poly.fit_transform(x_test)
    model = LinearRegression()
    model.fit(x_train_model,y_train)

    print('R² of the train-data: {:.2f}'.format(model.score(x_train_model, y_train)))
    print('R² of the test-data: {:.2f}'.format(model.score(x_test_model, y_test)))
    dict_train[pol_degree] = model.score(x_train_model, y_train)
    dict_test[pol_degree] = model.score(x_test_model, y_test)

    image.plot(x_train_model, model.predict(x_train_model), color='red')

plt.show()

image = plt.figure(num='R² for train and test data', figsize=(12, 10))

plot1 = image.add_subplot(221)
plot1.bar(range(len(dict_train)), list(dict_train.values()), align='center')
plot1.set_title('Train data')
plot1.set_xlabel('Polymorial degree')
plot1.set_ylabel('R²')
# plot1.xticks(range(len(dict_train)), list(dict_train.keys()))


plot2 = image.add_subplot(222)

plot2.bar(range(len(dict_test)), list(dict_test.values()), align='center')
plot2.set_title('Test data')
plot2.set_xlabel('Polymorial degree')
plot2.set_ylabel('R²')
# plot2.xticks(range(len(dict_test)), list(dict_test.keys()))

image.tight_layout()
plt.show()

figure = plt.figure(figsize=(10, 10), num='Polymorial Regression')
image = figure.add_subplot()

#image.scatter(x_train, y_train, color='blue')
