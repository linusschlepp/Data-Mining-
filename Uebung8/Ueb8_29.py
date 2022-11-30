from main import SVC, ListedColormap, load_iris, np, pd, plt

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF']) #Hintergrund
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])  #Plottpunkte

iris = load_iris()
data = iris.data
target = iris.target
features = np.array(["sepallength","sepalwidth","petallength","petalwidth"])
df = pd.DataFrame(data, columns=features)
data = df[["petallength", "petalwidth"]]

model_poly_two = SVC(kernel='poly', degree=2)
model_poly_three = SVC(kernel='poly', degree=3)

model_poly_two.fit(data, target)
model_poly_three.fit(data, target)


x_values = np.linspace(0.9,7,100)
y_values = np.linspace(0,3,100)

x_2, y_2 = np.meshgrid(x_values, y_values)


points = np.c_[x_2.ravel(), y_2.ravel()]

prediction_poly_two = model_poly_two.predict(points)
prediction_poly_three = model_poly_three.predict(points)

prediction_poly_two = prediction_poly_two.reshape((100,100))
prediction_poly_three = prediction_poly_three.reshape((100,100)) 

image = plt.figure(num="Iris - Support Vector Machine", figsize=(12, 10))

plot1 = image.add_subplot(221)

plot1.pcolormesh(x_values, y_values, prediction_poly_two, cmap=cmap_light, shading="auto")
plot1.scatter(data.petallength, data.petalwidth, c=target, cmap=cmap_bold)
plot1.set_xlabel("Petal Length (cm)")
plot1.set_ylabel("Petal Width (cm)")
plot1.set_title("Iris with poly n=3")


plot2 = image.add_subplot(222)
plot2.pcolormesh(x_values, y_values, prediction_poly_three, cmap=cmap_light, shading="auto")
plot2.scatter(data.petallength, data.petalwidth, c=target, cmap=cmap_bold)
plot2.set_xlabel("Petal Length (cm)")
plot2.set_ylabel("Petal Width (cm)")
plot2.set_title("Iris with poly n=3")


image.tight_layout()
plt.show()