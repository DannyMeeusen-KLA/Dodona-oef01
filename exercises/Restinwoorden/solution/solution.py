deeltal = int(input('Geef het deeltal: '))
deler = int(input('Geef de deler: '))

if deler < 1 or deler > 10:
    print ('De deler is niet correct.') 
else:
    restlijst = ['nul', 'een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen']
    rest = deeltal % deler
    print ('De rest bij deling van', deeltal, 'door', deler, 'is', restlijst[rest], '.')

