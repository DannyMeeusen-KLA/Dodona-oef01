We onderzoeken in dit programma welk natuurlijk getal uit een gegeven interval de langste Collatz-cycle heeft.  
Als je niet weet wat het vermoeden van Collatz is, zoek dit dan eerst op op het internet.  
  
Een Collatz-cycle is de rij getallen die ontstaat door het Collatz-algoritme toe te passen:  
- als het getal even is, dan is het volgende getal de helft ervan  
- als het getal oneven is, dan is het volgende getal het drievoud ervan plus 1  

Geef in dit programma twee natuurlijke getallen in: een ondergrens en een bovengrens van een gesloten interval.  
Onderzoek voor elk van de natuurlijke getallen in dit interval hoeveel getallen er in de Collatz-cycle zitten.  

Druk het getal af dat de langste cykel heeft, gevolgd door de lengte van de cykel. (Na dit laatste cijfer volgt géén spatie)  
Als twee of meer getallen uit het interval een gelijke, langste cyclelengte hebben, druk dan het kleinste van deze getallen af.

<u>Opmerking</u>: wie het principe van functies in een programma al kent, kan hier zeker overwegen om een functie te schrijven die van  
een gegeven getal de lengte van de bijhorende cycle berekent. Daarna kan deze functie voor elk getal in het gegeven interval aangeroepen worden.  

### Voorbeeld 1

```console?lang=python&prompt=>>>
>>> 1
>>> 10
9 20                                 (de cycle van 9 telt deze 20 elementen: 9 - 28 - 14 - 7 - 22 - 11 - 34 - 17 - 52 - 26 - 13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1)
```

### Voorbeeld 2

```console?lang=python&prompt=>>>
>>> 10
>>> 100
97 119
```

### Voorbeeld 3

```console?lang=python&prompt=>>>
>>> 10000
>>> 100000
77031 351
```
