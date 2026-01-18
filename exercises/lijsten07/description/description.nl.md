Schrijf een programma waarbij de gebruiker twee getallen ingeeft, op twee verschillende lijnen (dus met twee input-instructies).   
Vervolgens wordt eerst het kleinste getal aan een lege lijst toegevoegd, dan het grootste getal.  
Als beide getallen gelijk zijn aan elkaar, dan wordt het getal slechts één keer toegevoegd aan de lijst.  
Druk de lijst (met één of twee elementen) af.  

<u>Werkwijze:</u>
- Lees de twee getallen in met twee input-instructies (let op: we gaan er mee rekenen!)
- Maak een lege lijst aan.
- Kijk na of de getallen gelijk zijn aan elkaar (met een if). Voeg in dat geval het getal in kwestie toe aan de lijst.
- Zoniet: kijk na welk getal van de twee het kleinst is (met een elif). 
  Voeg dat getal als eerste toe aan de lijst, voeg het andere getal daarna toe (met de append-method).
- Zoniet (met een else): voeg beide getallen in omgekeerde volgorde toe aan de lijst.
- Druk de lijst af


### Voorbeeld

```console?lang=python&prompt=>>>
>>> 0 
>>> 1
[0, 1]
>>> 1
>>> 1
[1]
>>> 8
>>> -4
[-4, 8]
>>> 26
>>> 26
[26]
```
