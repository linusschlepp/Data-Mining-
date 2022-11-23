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


x_values = np.linspace(0.9,7,100)   # erzeugt 100 x-Werte zwischen 0.9 und 7
y_values = np.linspace(0,3,100)

x_2, y_2 = np.meshgrid(x_values, y_values)


points = np.c_[x_2.ravel(), y_2.ravel()]

prediction_poly_two = model_poly_two.predict(points)
prediction_poly_three = model_poly_three.predict(points)

prediction_poly_two = prediction_poly_two.reshape((100,100))  # Rückwandeln: 10000 --> 100x100
prediction_poly_three = prediction_poly_three.reshape((100,100)) 

image = plt.figure(num="Iris - Support Vector Machine", figsize=(12, 10))

plot1 = image.add_subplot(221)
# Flächenweise Ausgabe der imagepunkte
plot1.pcolormesh(x_values, y_values, prediction_poly_two, cmap=cmap_light, shading="auto")
# Ausgabe der Irispunkte
plot1.scatter(data.petallength, data.petalwidth, c=target, cmap=cmap_bold)
plot1.set_xlabel("Petal Length (cm)")
plot1.set_ylabel("Petal Width (cm)")
plot1.set_title("Iris with poly n=3")

# Dann das image mit SVM.LinearSVC
plot2 = image.add_subplot(222)
# Flächenweise Ausgabe der imagepunkte
plot2.pcolormesh(x_values, y_values, prediction_poly_three, cmap=cmap_light, shading="auto")
# Ausgabe der Irispunkte
plot2.scatter(data.petallength, data.petalwidth, c=target, cmap=cmap_bold)
plot2.set_xlabel("Petal Length (cm)")
plot2.set_ylabel("Petal Width (cm)")
plot2.set_title("Iris with poly n=3")

# # Dann das image mit SVM.SVC poly degree=2
# plot3 = image.add_subplot(223)
# # Flächenweise Ausgabe der imagepunkte
# plot3.pcolormesh(x_values, y_values, proposal_svmpoly2, cmap=cmap_light, shading="auto")
# # Ausgabe der Irispunkte
# plot3.scatter(X.petallength, X.petalwidth, c=y, cmap=cmap_bold)
# plot3.set_xlabel("Petal Länge (cm)")
# plot3.set_ylabel("Petal Weite (cm)")
# plot3.set_title("Iris mit SVM (Polynom Grad 2)")
#
# # Dann das image mit SVM.SVC poly degree=3
# plot4 = image.add_subplot(224)
# # Flächenweise Ausgabe der imagepunkte
# plot4.pcolormesh(x_values, y_values, proposal_svmpoly3, cmap=cmap_light, shading="auto")
# # Ausgabe der Irispunkte
# plot4.scatter(X.petallength, X.petalwidth, c=y, cmap=cmap_bold)
# plot4.set_xlabel("Petal Länge (cm)")
# plot4.set_ylabel("Petal Weite (cm)")
# plot4.set_title("Iris mit SVM (Polynom Grad 3)")

image.tight_layout()       # verbessert die Ausgabe mit Abständen zwischen Subplots
plt.show()