def cNaarw (in_cijfer, in_plaats):

    if in_cijfer == 0:
        return ""
    elif in_cijfer == 1:
        if in_plaats == "H":
            return "honderd"
        elif in_plaats == "T":
            return "tien"
        else:
            return "een"
    elif in_cijfer == 2:
        if in_plaats == "H":
            return "tweehonderd"
        elif in_plaats == "T":
            return "twintig"
        else:
            return "twee"
    elif in_cijfer == 3:
        if in_plaats == "H":
            return "driehonderd"
        elif in_plaats == "T":
            return "dertig"
        else:
            return "drie"
    elif in_cijfer == 4:
        if in_plaats == "H":
            return "vierhonderd"
        elif in_plaats == "T":
            return "veertig"
        else:
            return "vier"
    elif in_cijfer == 5:
        if in_plaats == "H":
            return "vijfhonderd"
        elif in_plaats == "T":
            return "vijftig"
        else:
            return "vijf"
    elif in_cijfer == 6:
        if in_plaats == "H":
            return "zeshonderd"
        elif in_plaats == "T":
            return "zestig"
        else:
            return "zes"
    elif in_cijfer == 7:
        if in_plaats == "H":
            return "zevenhonderd"
        elif in_plaats == "T":
            return "zeventig"
        else:
            return "zeven"
    elif in_cijfer == 8:
        if in_plaats == "H":
            return "achthonderd"
        elif in_plaats == "T":
            return "tachtig"
        else:
            return "acht"
    elif in_cijfer == 9:
        if in_plaats == "H":
            return "negenhonderd"
        elif in_plaats == "T":
            return "negentig"
        else:
            return "negen"


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
    else:
        wtieneenheid = cNaarw(eenheid, "E")+"tien"
else:
    wtieneenheid = cNaarw(eenheid, "E")+"en"+cNaarw(tiental, "T")

print (whonderd+wtieneenheid)
