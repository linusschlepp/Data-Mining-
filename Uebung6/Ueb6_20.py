from main import *


ran_stream = 12

df['iris'] = target
x_train, x_test, y_train, y_test = train_test_split(df, df['iris'], random_state=ran_stream)

model_nb = GaussianNB()
model_nb.fit(x_train, y_train)
prediction = model_nb.predict(x_test)
print(prediction)
print('The accuracy is {:.1f}%'.format(100*np.mean(prediction == y_test)))

