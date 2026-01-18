getal1 = int(input('Geef het eerste getal: '))
getal2 = int(input('Geef het tweede getal: '))

lijst=[]
if getal1 < getal2:
    lijst.append (getal1)
    lijst.append (getal2)
else:
    lijst.append (getal2)
    lijst.append (getal1)

print (lijst)
