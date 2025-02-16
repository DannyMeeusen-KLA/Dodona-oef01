Een kleuterleider deelt ballonnen uit aan de kleuters in zijn klas.  
Eerst geven we het aantal ballonnen op dat hij in zijn bezit heeft, daarna geven we het aantal kleuters in zijn klas op.  
  
Druk af hoeveel ballonnen hij nog overhoudt als hij iedere kleuter evenveel ballonnen wil geven.  
Dit is een simpel programma waarbij je gebruik maakt van de '%'-operator (modulo).  
De moeilijkheid hier is de invoercontrole:  
- elke keer als de invoer van het aantal ballonnen niet numeriek is, moet de melding verschijnen '*invoer aantal ballonnen niet numeriek.*'  
- elke keer als de invoer van het aantal kleuters niet numeriek is, moet de melding verschijnen '*invoer aantal kleuters niet numeriek.*'  
- verder moet het aantal ballonnen tussen 10 en 50 liggen (grenswaarden inbegrepen). Als dat niet het geval is, moet de melding verschijnen '*aantal ballonnen moet tussen 10 en 50 liggen.*'  
- en moet het aantal kleuters tussen 5 en 20 liggen (grenswaarden ook hier inbegrepen). Als dat niet het geval is, moet de melding verschijnen '*aantal kleuters moet tussen 5 en 20 liggen.*'  

Uiteindelijk drukt het programma het aantal ballonnen af dat niet onder de kleuters verdeeld kan worden, in een volzin (zie voorbeelden).  
Gebruik voor de dubbele invoercontrole twee keer een **while True** die een **try-except**-structuur bevat.  
  
### Voorbeeld 1

```console?lang=python&prompt=>>>
>>> 54A
invoer aantal ballonnen niet numeriek.
>>> 54
aantal ballonnen moet tussen 10 en 50 liggen.
>>> 50
>>> 25
aantal kleuters moet tussen 5 en 20 liggen.
>>> 18ggddddh
invoer aantal kleuters niet numeriek.
>>> 18
14 ballonnen kunnen niet verdeeld worden.
```

### Voorbeeld 2

```console?lang=python&prompt=>>>
>>> 9
aantal ballonnen moet tussen 10 en 50 liggen.
>>> A10
invoer aantal ballonnen niet numeriek.
>>> 10
>>> gg4ddddh
invoer aantal kleuters niet numeriek.
>>> 4
aantal kleuters moet tussen 5 en 20 liggen.
>>> 7
3 ballonnen kunnen niet verdeeld worden.
```
