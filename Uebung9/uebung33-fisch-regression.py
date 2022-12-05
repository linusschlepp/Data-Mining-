# Übung 33 zur Vorlesung DDMI:
# Untersuchung von allen Fischmaßen im Vergleich zum Fischgewicht
# Edwin Schicker

import matplotlib.pyplot as plt  
import numpy as np               
import pandas as pd
import seaborn as sns; sns.set()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

daten = pd.read_csv("Fish.csv")       # Standard: Begrenzung ist Komma, Überschriftenzeile
print(daten) 

# Untersuchung zu Zusammenhang mit weight
print("Ein Zusammenhang zwischen Fischmaßen und weight wird untersucht")
X = daten.iloc[:,2:]                                     # Alle Längen- und Höhenangaben
y = daten.iloc[:,1]                                      # Gewicht

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.3,
                                                    random_state = 13)     # 70% der Daten für das Training

print(" ----- Lineare Regressionsanalyse ------- ")
model = LinearRegression()                             # instanziieren der Klasse
model.fit(X_train, y_train)                            # trainieren

print("------ Auswertung der linearen Regression -----")
print("R2 der Trainingsdaten: {:.2f}".format(model.score(X_train, y_train)))
print("R2 der Testdaten: {:.2f}".format(model.score(X_test, y_test)))
input("Bitte RETURN klicken")

# Polynomiale Regressionsanalyse
print(" ----- Polynomiale Regressionsanalyse ------- ")
print("Beste Ergebnisse mit Polynomgrad 3")

poly = PolynomialFeatures(degree = 3)   # Basis für die Transformation poly-->linear
X_train2 = poly.fit_transform(X_train)  # Transformieren der Parameter
X_test2 = poly.fit_transform(X_test)

model2 = LinearRegression()             # auf lineares Modell anwenden
model2.fit(X_train2, y_train)

print("------ Auswertung der polynomialen Regression -----")
print("R2 der Trainingsdaten: {:.2f}".format(model2.score(X_train2, y_train)))
print("R2 der Testdaten: {:.2f}".format(model2.score(X_test2, y_test)))

print("Die Überprüfung aller Messdaten liefert die besten Ergebnisse. Polynomgrad 2 und 3 sind optimal.")
print("Höhere Polynomegrade entarten")
