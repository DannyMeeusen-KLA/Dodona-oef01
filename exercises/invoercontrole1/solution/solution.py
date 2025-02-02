while True:
    dag = input('Welke dag wordt de uitstap georganiseerd (ma/di/wo/do/vr) : ')
    if dag in ('ma', 'di', 'wo', 'do', 'vr'):
        break
    print ('Foutieve dag, probeer opnieuw.')
    
while True:
    lln = int(input('Hoeveel leerlingen nemen deel aan de uitstap? '))
    if lln > 0 and lln < 25:
        break
    print ('Foutief aantal, probeer opnieuw.')
    
if dag == 'ma':
    print ('Uitstap op maandag met', lln, 'leerlingen.')
elif dag == 'di':
    print ('Uitstap op dinsdag met', lln, 'leerlingen.')
elif dag == 'wo':
    print ('Uitstap op woensdag met', lln, 'leerlingen.')
elif dag == 'do':
    print ('Uitstap op donderdag met', lln, 'leerlingen.')
else:
    print ('Uitstap op vrijdag met', lln, 'leerlingen.')
