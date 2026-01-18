Schrijf een programma waarbij de gebruiker twee getallen ingeeft, op twee verschillende lijnen (dus met twee input-instructies).   
Vervolgens wordt eerst het kleinste getal aan een lege lijst toegevoegd, dan het grootste getal.  
Druk de lijst (met twee elementen) af.  

<u>Werkwijze:</u>
- Lees de twee getallen in met twee input-instructies (let op: we gaan er mee rekenen!)
- Maak een lege lijst aan
- Kijk na welk getal van de twee het kleinst is (met een if)
- Voeg dat getal als eerste toe aan de lijst, voeg het andere getal daarna toe (met de append-method)
- Druk de lijst af


### Voorbeeld

```console?lang=python&prompt=>>>
>>> 0 
>>> 1
[0, 1]
>>> 1
>>> 0
[0, 1]
>>> 8
>>> -4
[-4, 8]
>>> 100
>>> 26
[26, 100]
```
