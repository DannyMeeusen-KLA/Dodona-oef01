De gebruiker geeft een vrij stuk tekst in.  
Het programma telt het aantal woorden in de tekst. Twee woorden worden van elkaar gescheiden door een spatie.  
Toch is het aantal spaties niet gelijk aan het aantal woorden:  
- er kunnen meerdere spaties tussen twee woorden staan.
- er kunnen vooraan of achteraan spaties staan zonder dat deze het aantal wooren beïnvloeden  
  
Tip: maak gebruik van een variabele *vorige_letter* waarin je telkens de waarde van de vorige letter bewaart.  
Elke keer als een letter verschilt van een spatie, terwijl de vorige letter wel een spatie was, hebben we te maken met een nieuw woord.  
Vraag je af wat de beginwaarde van *vorige_letter* moet zijn.  

### Voorbeeld

```console?lang=python&prompt=>>>
>>> Het KLA is een school van het Gemeenschapsonderwijs.
8
>>> De Olympische Spelen in Parijs waren een succes.
8
>>> Het vak Informaticawetenschappen is best lastig.
6
>>> Honden zijn geen fan van vuurwerk.
6
>>> De EU heeft haar hoofdzetel in Brussel.
7
```
