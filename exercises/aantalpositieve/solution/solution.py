getal1 = int(input('Geef het eerste getal: '))
getal2 = int(input('Geef het tweede getal: '))
getal3 = int(input('Geef het derde getal: '))

aantal_pos = 0
if getal1 > 0:
    aantal_pos += 1
if getal2 > 0:
    aantal_pos += 1
if getal3 > 0:
    aantal_pos += 1

print (aantal_pos)
