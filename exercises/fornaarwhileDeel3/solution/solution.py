# invoer
zin = input('Schrijf een zin met minstens 2 woorden: ')

# zin converteren naar een lijst van woorden
woordenlijst = zin.split()

# index van de lijst op 0 initialiseren
tel = 0

# door de lijst wandelen van 0 t.e.m. lengte - 1 en elk element afdrukken
while tel < len(woordenlijst):
    print (woordenlijst[tel])
    tel = tel+1
