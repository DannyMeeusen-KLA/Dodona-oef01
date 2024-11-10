Schrijf een programma waarbij de gebruiker eerst de naam van een leerling ingeeft en daarna het behaalde percentage op het eindexamen.  
Het ingevoerde percentage ligt in het interval [50, 100].

Het programma bepaalt aan de hand van het percentage het soort diploma dat de leerling krijgt.  

- als het percentage groter of gelijk aan 80 is, dan verschijnt de zin '*xxx haalde een diploma met grote onderscheiding*' (waarbij xxx de naam van de leerling is).  
- als het percentage kleiner dan 80 is, maar groter of gelijk aan 70, dan verschijnt de zin '*xxx haalde een diploma met onderscheiding*' (waarbij xxx de naam van de leerling is).  
- als het percentage kleiner dan 70 is, dan verschijnt de zin '*xxx haalde een diploma*' (waarbij xxx de naam van de leerling is).  


### Voorbeeld

```console?lang=python&prompt=>>>
>>> Andrea
>>> 82
Andrea haalde een diploma met grote onderscheiding
>>> Feline
>>> 80
Feline haalde een diploma met grote onderscheiding
>>> Juliette
>>> 78
Juliette haalde een diploma met onderscheiding
>>> Yulin
>>> 70
Yulin haalde een diploma met onderscheiding
>>> Mia
>>> 68
Mia haalde een diploma
```
