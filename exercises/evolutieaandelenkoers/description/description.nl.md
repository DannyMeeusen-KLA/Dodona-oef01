Schrijf een programma waarbij de gebruiker  
- eerst de naam van een beursaandeel ingeeft,  
- daarna de aandelenkoers van gisteren ingeeft en  
- ten slotte de koers van vandaag ingeeft.  

Het programma vergelijkt vervolgens de koers van gisteren met die van vandaag.  

- als de koers van gisteren lager is dan die van vandaag, dan verschijnt de zin '*De koers van het aandeel xxx is gestegen.*' (waarbij xxx de naam van het aandeel is).  
- als de koers van gisteren hoger is dan die van vandaag, dan verschijnt de zin '*De koers van het aandeel xxx is gedaald.*' (waarbij xxx de naam van het aandeel is).  
- als de koers van gisteren gelijk is aan die van vandaag, dan verschijnt de zin '*De koers van het aandeel xxx is ongewijzigd.*' (waarbij xxx de naam van het aandeel is).  


### Voorbeeld

```console?lang=python&prompt=>>>
>>> AB-Inbev
>>> 67
>>> 68
De koers van het aandeel AB-Inbev is gestegen.
>>> Elia
>>> 32
>>> 31
De koers van het aandeel Elia is gedaald.
>>> KBC
>>> 41
>>> 41
De koers van het aandeel KBC is ongewijzigd.
```
