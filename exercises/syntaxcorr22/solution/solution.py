bovengrens = int(input('Geef de bovengrens van de reeks: '))

if bovengrens < 0:
    print ('Het ingebrachte getal moet positief zijn.')
else:
    som = 0
    for term in range (bovengrens+1):
        som = som + term
    print (som)