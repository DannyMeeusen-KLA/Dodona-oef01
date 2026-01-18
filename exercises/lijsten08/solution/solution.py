onder = int(input('Geef de ondergrens: '))
boven = int(input('Geef de bovengrens: '))

lijst = [*range(onder, boven, 1)]

if 24 in lijst:
    lijst.remove(24)

aantal = len(lijst)
print (aantal)
if aantal < 10:
    print ('Te weinig elementen!')
else:
    print (lijst[9])
