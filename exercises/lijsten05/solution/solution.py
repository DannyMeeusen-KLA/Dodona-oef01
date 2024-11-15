instring = input('Geef een aantal gehele getallen, gescheiden door een spatie: ')
instrlist = instring.split()

uniekelijst = []
dubbellijst = []
for instr in instrlist:
    getal = int(instr)
    if getal not in dubbellijst:
        if getal in uniekelijst:
            dubbellijst.append (getal)
            uniekelijst.remove (getal)
        else:
            uniekelijst.append (getal)

print(uniekelijst)
