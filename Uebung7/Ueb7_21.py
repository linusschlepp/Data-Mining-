
from main import pd
'''
Antworten zu gestellten Fragen in Aufgabe 21:

    - Trennzeichen? -> Komma
    - Überschriftenzeile? -> Nein
    - Wie viele Datensätze? -> 351
    - Wie viele Features? -> 34
    - Sind features numerisch? -> Ja (Gleitkommaszahlen als auch keine Gleitkommazahlen), bis auf letztes Feature (ist ein char)
    - Erste beiden Features, Besonderheiten? -> Nur 0 und 1
    - Ausreiser? -> Bestimmte Datensätze haben -1 enthalten bzw. Zeilen, die bei der ersten Spalte 0 enthalten, können entfernt werden. 

'''


data = pd.read_csv('ionosphere.csv', sep=',')
print(data)