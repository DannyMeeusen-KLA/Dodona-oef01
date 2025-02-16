# invoercontrole ballonnen
while True:
    try:
        ballonnen = int(input('Geef het aantal ballonnen: '))
        if ballonnen >= 10 and ballonnen <= 50:
            break
        else:
            print ('aantal ballonnen moet tussen 10 en 50 liggen.')
    except:
        print ('invoer aantal ballonnen niet numeriek.')
        
# invoercontrole kleuters
while True:
    try:
        kleuters = int(input('Geef het aantal kleuters: '))
        if kleuters >= 5 and kleuters <= 20:
            break
        else:
            print ('aantal kleuters moet tussen 5 en 20 liggen.')
    except:
        print ('invoer aantal kleuters niet numeriek.')

print (ballonnen%kleuters, 'ballonnen kunnen niet verdeeld worden.')        
