grondtal = int(input('Geef het grondtal'))

# om te vermijden dat we in een oneindige lus terecht komen
if grondtal == 0:
    print (1)
elif grondtal < 0:
    print ('/')
else:
    fac = 1
    for tel in range (2, grondtal+1):
        fac = fac * tel 
    print (fac)