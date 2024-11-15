instring = input('Geef een aantal gehele getallen, gescheiden door een spatie: ')
instrlist = instring.split()

uniekelijst = []
for instr in instrlist:
    getal = int(instr)
    if getal not in uniekelijst:
        uniekelijst.append (getal)

print(uniekelijst)