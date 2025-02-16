def Collatz (in_getal):
    
    ret_teller = 1
    c_getal = in_getal
    while c_getal != 1:
        ret_teller += 1
        if c_getal % 2 == 0:
            c_getal = c_getal//2
        else:
            c_getal = c_getal*3 + 1 
    return ret_teller
    

onder = int(input('Geef de ondergrens in: '))
boven = int(input('Geef de bovengrens in: '))

max_lengte = 0
max_getal = 0
for getal in range (onder, boven+1):
    c_lengte = Collatz(getal)
    if c_lengte > max_lengte:
        max_lengte = c_lengte
        max_getal = getal

print (max_getal, max_lengte)
