from main import PolynomialFeatures, x_train, x_test, LinearRegression, y_train, pd, np, y_test, plt, y_fish

poly = PolynomialFeatures(degree=3)
x_train_model = poly.fit_transform(x_train)
x_test_model = poly.fit_transform(x_test)

model = LinearRegression()
model.fit(x_train_model, y_train)
model1 = LinearRegression()
model1.fit(x_train, y_train)

x_fit = np.arange(x_train.min().values, x_train.max().values)  # only in 1d field
x_fit = pd.DataFrame(x_fit, columns=['Length3'])  # Convert to dataframe
X_fit2 = poly.fit_transform(x_fit)

fig = plt.figure(figsize=(10, 10), num='Linear/polymorphic Regression for comparing reasons')
image = fig.add_subplot()
image.scatter(x_train, y_train, color='blue', label='Train-data')
image.scatter(x_test, y_test, color='green', label='Test-data')
image.plot(x_fit, model1.predict(x_fit), color='red', label='Linear')
image.plot(x_fit, model.predict(X_fit2), color='purple', label='Polynom')
image.set_xlabel(x_train.columns[0])
image.set_ylabel(y_fish.name)
image.legend()
image.set_title('Polymorphic Regression between Length and Weight')
plt.show()
