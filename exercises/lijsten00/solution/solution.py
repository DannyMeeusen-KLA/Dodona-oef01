# inlezen ondergrens
ondergrens = int(input('Geef een getal groter of gelijk aan 10 in: '))
# bepalen bovengrens
bovengrens = (ondergrens * 2) + 1

# maken lijst
lijst=[*range(ondergrens, bovengrens+1, 2)]

# derde element verdubbelen
lijst[2]=lijst[2]*2

# verwijderen element 30 indien aanwezig
if 30 in lijst:
    lijst.remove(30)

#lengte en inhoud lijst afdrukken
print (len(lijst))
print (lijst)
