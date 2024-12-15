import math

# inlezen coëfficiënten
coeffa = int(input('Geef de waarde van a: '))
coeffb = int(input('Geef de waarde van b: '))
coeffc = int(input('Geef de waarde van c: '))

# berekenen van D
discr = (coeffb**2)-(4*coeffa*coeffc)

# evalueer het teken van D
if discr < 0:
    print ('/')
elif discr == 0:
    x1 = coeffb * (-1) / (2*coeffa)
    x1 = round(x1, 2)
    print (x1)
else:
    x1 = (coeffb * (-1) + math.sqrt(discr))/ (2*coeffa)
    x1 = round(x1, 2)
    x2 = (coeffb * (-1) - math.sqrt(discr))/ (2*coeffa)
    x2 = round(x2, 2)
    if x1 < x2:
        print (x1)
        print (x2)
    else:
        print (x2)
        print (x1)

