leerling = input('Geef de naam van de leerling: ')
percent = int(input('Geef het percentage op het eindexamen: '))

if percent >= 80:
    print (leerling, 'behaalde een diploma met grote onderscheiding.')
elif percent >= 70:
    print (leerling, 'behaalde een diploma met onderscheiding.')
else:
    print (leerling, 'behaalde een diploma.')
