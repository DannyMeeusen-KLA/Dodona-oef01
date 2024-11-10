leerling = input('Geef de naam van de leerling: ')
percent = int(input('Geef het percentage op het eindexamen: '))

if percent >= 80:
    print (leerling, 'haalde een diploma met grote onderscheiding')
elif percent >= 70:
    print (leerling, 'haalde een diploma met onderscheiding')
else:
    print (leerling, 'haalde een diploma')
