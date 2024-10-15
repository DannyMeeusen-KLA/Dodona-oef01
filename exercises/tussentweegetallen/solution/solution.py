onder = int(input('Geef de ondergrens van je interval: '))
boven = int(input('Geef de bovengrens van je interval: '))
getal = int(input('Geef het te onderzoeken getal: '))

if getal >= onder and getal <= boven:
    print ('TUSSEN')
else:
    print ('NIET TUSSEN')
     