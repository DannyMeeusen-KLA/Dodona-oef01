getal = int(input('Geef de beginwaarde in: '))

while getal <= 100:
    getal = getal*3
    if getal % 2 == 0:
        getal = getal + 1
    else:
        getal = getal - 1
    
print (getal)
