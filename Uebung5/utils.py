import pandas as pd

def train(X, feature, df_train):
    werte = X[feature].unique()                     # alle auftretenden Werte merken
    vorhersagen = pd.Series(index=werte, dtype=int) # Feld für Vorhersagen
    fehler = 0
    # in Schleife alle Vorhersagen und Fehler ermitteln
    for i in werte:
        iris, fehl = train_feature_wert(X, feature, i, df_train)
        vorhersagen[i] = iris
        fehler += fehl
    return vorhersagen, fehler

# für alle drei Iris-Typen (von 0 bis 2) die Anzahl der Treffer ermitteln, abhängig von feature und wert
def train_feature_wert(X, feature, wert, df_train):
    df_help = df_train[df_train[feature] == wert]        #nur Zeilen, deren Feature den Wert enthält
    iris_zaehler = df_help.iris.value_counts()           #zählt alle Iris Vorkommnisse
    imax = iris_zaehler.idxmax()         #häufigste Iris
    fehler = iris_zaehler.sum() - iris_zaehler.max()    #Anzahl der falschen Angaben: alle - max
    return imax, fehler