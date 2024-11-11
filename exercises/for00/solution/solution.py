woord = input('Geef een willekeurig woord in: ')
grondtal = int(input('Geef een natuurlijk getal in: '))

provincies = ['Antwerpen', 'Limburg', 'Oost-Vlaanderen', 'Vlaams-Brabant', 'West-Vlaanderen']

for prov in provincies:
    print(prov)

for letter in woord:
    print(letter)

for teller in range (0, grondtal, 1):
    print (teller**2)
