Schrijf een programma waarbij de gebruiker twee natuurlijke getallen ingeeft:  
- Het eerste getal is de ondergrens van een rekenkundige rij.  
- Het tweede getal is groter dan het eerste en is de bovengrens van dezelfde rij.  
Als het getal 24 in de lijst zit, verwijder het dan.  
Vervolgens drukt het programma het aantal overblijvende elementen in de lijst af.   
Als de lijst 10 of meer elementen bevat, drukt het programma dat tiende element af in een volzin (zie voorbeelden).  
Als de lijst minder dan 10 elementen bevat, dan drukt het prorgamma de tekst 'Te weinig elementen!' af.

<u>Tips:</u>
- Gebruik de functie   *range(ondergrens, bovengrens, stap)  om de lijst met de rekenkundige rij te vullen.  
- Denk eraan: de range-functie stopt met elementen in de lijst te steken net voor de bovengrens!
- Gebruik de    lijst.remove(24)     -method om het element met waarde 24 uit de lijst te halen.
- Kijk eerst na of er wel een element met waarde 24 is (if 24 in lijst:) alvorens eventueel een remove uit te voeren.  
- Gebruik de functie   len(lijst)    om het aantal elementen in de lijst op te halen.  
- Het eerste element in de lijst heeft index 0. Het tiende element in de lijst zal dus index 9 hebben.  

### Voorbeeld

```console?lang=python&prompt=>>>
>>> 0 
>>> 1
2
Te weinig elementen!
>>> 12
>>> 23
12
Het tiende element is 21
>>> 18
>>> 37
19
Het tiende element is 28
>>> 20
>>> 29
9
Te weinig elementen!
```
