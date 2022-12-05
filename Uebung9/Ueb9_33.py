from main import fish_data, PolynomialFeatures, train_test_split, LinearRegression

X = fish_data.iloc[:,2:]                                     # All width and heights
y = fish_data.iloc[:,1]                                      # Weight

x_train, x_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.3,
                                                    random_state = 13)     # 70% of the data for training

model = LinearRegression()                             # instanciate
model.fit(x_train, y_train)                            # train

print('Results for linear regression')
print('R² for train-data: {:.2f}'.format(model.score(x_train, y_train)))
print('R² for test-data: {:.2f}'.format(model.score(x_test, y_test)))

poly = PolynomialFeatures(degree = 3)
X_train2 = poly.fit_transform(x_train)
X_test2 = poly.fit_transform(x_test)

model2 = LinearRegression()
model2.fit(X_train2, y_train)

print('Results for polymorial regression')
print('R² for train-data: {:.2f}'.format(model2.score(X_train2, y_train)))
print('R² for test-data: {:.2f}'.format(model2.score(X_test2, y_test)))