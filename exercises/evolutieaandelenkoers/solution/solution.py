aandeel = input('Geef de naam van het aandeel: ')
koersgisteren = int(input('Geef de koers van gisteren: '))
koersvandaag = int(input('Geef de koers van vandaag: '))

if koersgisteren < koersvandaag:
    print ('De koers van het aandeel', aandeel, 'is gestegen')
elif koersgisteren == koersvandaag:
    print ('De koers van het aandeel', aandeel, 'is gedaald')
else:
    print ('De koers van het aandeel', aandeel, 'is ongewijzigd')

