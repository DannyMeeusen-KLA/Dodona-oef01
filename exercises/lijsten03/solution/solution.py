def listsort(in_list):
    b_sort = False
    while b_sort == False:
        b_sort = True
        for tel in range(1, len(in_list)):
            if in_list[tel-1] > in_list[tel]:
                dummy = in_list[tel-1]
                in_list[tel-1] = in_list[tel]
                in_list[tel] = dummy
                b_sort = False
    return (in_list)
    
instring = input('Geef een aantal gehele getallen, gescheiden door een spatie: ')

instrlist = instring.split()
#maken en vullen listeven en listoneven
listeven = []
listoneven = []
for instr in instrlist:
    getal = int(instr)
    if getal % 2 == 0:
        listeven.append (getal)
    else:
        listoneven.append (getal)

listeven = listsort(listeven)
listoneven = listsort(listoneven)

print(listeven)
print(listoneven)
