import math

deeltal = int(input('Geef een getal: '))

priem = True

for deler in range (2, int(math.sqrt(deeltal))+1):
    if deeltal % deler == 0:
        priem = False
        break

if priem:
    print ("PRIEMGETAL")
else:
    print ("GEEN PRIEMGETAL")