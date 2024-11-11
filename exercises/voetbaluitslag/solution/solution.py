naamthuis = input('Geef de naam van de thuisploeg: ')
doelthuis = int(input('Geef het aantal doelpunten van de thuisploeg: '))
naamuit = input('Geef de naam van de uitploeg: ')
doeluit = int(input('Geef het aantal doelpunten van de uitploeg: '))

if doelthuis > doeluit:
    print (naamthuis, 'wint de wedstrijd.')
elif doelthuis == doeluit:
    print (naamthuis, 'en', naamuit, 'spelen gelijk.')
else:
    print (naamuit, 'wint de wedstrijd.')

