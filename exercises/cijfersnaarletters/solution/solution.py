def cNaarw (in_cijfer, in_plaats):

    if in_cijfer == 0:
        return ""
    elif in_cijfer == 1:
        if in_plaats = "H":
            return "honderd"
        elif in_plaats = "T"
            return "tien"
        else:
            return "eenen"
    elif in_cijfer == 2:
        if in_plaats = "H":
            return "tweehonderd"
        elif in_plaats = "T"
            return "twintig"
        else:
            return "tweeen"
    elif in_cijfer == 3:
        if in_plaats = "H":
            return "driehonderd"
        elif in_plaats = "T"
            return "dertig"
        else:
            return "drieen"
    elif in_cijfer == 4:
        if in_plaats = "H":
            return "vierhonderd"
        elif in_plaats = "T"
            return "veertig"
        else:
            return "vieren"
    elif in_cijfer == 5:
        if in_plaats = "H":
            return "vijfhonderd"
        elif in_plaats = "T"
            return "vijftig"
        else:
            return "vijfen"
    elif in_cijfer == 6:
        if in_plaats = "H":
            return "zeshonderd"
        elif in_plaats = "T"
            return "zestig"
        else:
            return "zesen"
    elif in_cijfer == 7:
        if in_plaats = "H":
            return "zevenhonderd"
        elif in_plaats = "T"
            return "zeventig"
        else:
            return "zevenen"
    elif in_cijfer == 8:
        if in_plaats = "H":
            return "achthonderd"
        elif in_plaats = "T"
            return "tachtig"
        else:
            return "achten"
    elif in_cijfer == 9:
        if in_plaats = "H":
            return "negenhonderd"
        elif in_plaats = "T"
            return "negentig"
        else:
            return "negenen"
    elif

getal = int(input('Geef een getal in: '))
honderdtal = getal//100
tiental = (getal%100)//10
eenheid = getal%10

#uitzondering voor 11 t.e.m. 19
whonderd = cNaarw(honderdtal, "H")
if tiental == 1:
    if eenheid == 0:
        wtieneenheid = "tien"
    elif eenheid == 1:
        wtieneenheid = "elf"
    elif eenheid == 2:
        wtieneenheid = "twaalf"
    elif eenheid == 3:
        wtieneenheid = "dertien"
    elif eenheid == 4:
        wtieneenheid = "veertien"
    elif eenheid == 5:
        wtieneenheid = "vijftien"
    elif eenheid == 6:
        wtieneenheid = "zestien"
    elif eenheid == 7:
        wtieneenheid = "zeventien"
    elif eenheid == 8:
        wtieneenheid = "achttien"
    else:
        wtieneenheid = "negentien"
else:
    wtieneenheid = cNaarw(eenheid, "E")+cNaarw(tiental, "T")

print (whonderd+wtieneenheid)

