aanwezig = int(input('Hoeveel personen zijn er aanwezig: '))
stoelenpertafel = int(input('Hoeveel stoelen staan er per tafel: '))

tafelsnodig = ((aanwezig-1)//stoelenpertafel)+1
print (tafelsnodig)