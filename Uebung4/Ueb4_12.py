from main import *


# facttab = pd.read_csv("facttab.csv", sep=";", usecols=["PSID","CSID"])
# product = pd.read_csv("product.csv", sep=";", header=0, usecols=["PSID","artid","prodgrid"])
# customer = pd.read_csv("customer.csv", sep=";", header=0, usecols=["CSID","custid","name"])


X = pd.merge(left=fact_data, right=product_data, on="PSID")
X = pd.merge(left=X, right=customer_data, on="CSID")
print(X)
X.to_csv('test.csv')

X=X[["custid","name","artid","prodgroup"]]
# Eine neue Spalte anzahl hinzufügen, um dort die gruppierten Werte abzulegen
X["anzahl"] = 0

# Gruppieren und sortieren (aufsteigend nach name, absteigend nach Anzahl):
X = X.groupby(["custid", "name","artid", "prodgrid"]).count().reset_index()
X = X.sort_values(["custid","anzahl"], ascending=[True,False])

# In Schleife nur die drei best verkauften prodgride je name wählen und in neuer Tabelle erg sammeln:
erg = pd.DataFrame(columns=X.columns)            # leere Tabelle erzeugen

for custid in customer.custid.values:
    hilf = X[X.custid == custid].iloc[:3]    # 3 besten prodgride des namen custid
    erg = erg.append(hilf, ignore_index=True)      # der Erg-Tabelle hinzufügen

print(erg)