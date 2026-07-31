lijst = []
while True:
    naam = input ('Geef de naam van de bestemmeling: ')
    if naam == '':
        break
    lijst.append (naam)

if len(lijst) == 0:
    #lege lijst
    print ('Geen bestemmelingen!')
else:
    # initialisaties
    output = 'Beste '
    tel = 0
    # toevoeging namen met komma voor alle elementen behalve de laatste 2
    while tel < len(lijst) - 2:
        output = output + lijst[tel] + ', '
        tel = tel + 1
    # toevoeging naam met ' en ' voor het voorlaatste element
    while tel < len(lijst) - 1:
        output = output + lijst[tel] + ' en '
        tel = tel + 1
    # toevoeging laatste naam
    output = output + lijst[tel]

    # afdruk
    print (output)
    