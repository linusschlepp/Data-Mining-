from main import plt, fish_data, pd, LinearRegression, x_train, y_train, x_test, y_test, y_fish

scmx = pd.plotting.scatter_matrix(fish_data.iloc[:, 1:],
                                  c=fish_data.iloc[:, 1].values,
                                  figsize=(15, 15),
                                  marker='o',
                                  s=30,
                                  alpha=0.8)
plt.show()

model = LinearRegression()  # Create model
model.fit(x_train, y_train)  # Train

print('R² of train-data: {:.2f}'.format(model.score(x_train, y_train)))
print('R² of test-data: {:.2f}'.format(model.score(x_test, y_test)))

# Visualisieren des Ergebnisses
fig = plt.figure(figsize=(10, 10), num='Linear Regression')
bild = fig.add_subplot()
bild.scatter(x_train, y_train, color="blue")  # Blue Points
bild.scatter(x_test, y_test, color="green")  # Green Points
bild.plot(x_train, model.predict(x_train), color="red")
bild.set_xlabel(x_train.columns[0])
bild.set_ylabel(y_fish.name)
bild.set_title("Linear Regression between length and weight")
plt.show()
