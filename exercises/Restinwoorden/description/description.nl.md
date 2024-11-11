Schrijf een programma waarbij de gebruiker een deeltal en een deler kan ingeven.  
Het programma kijkt eerst na of de deler een strikt natuurlijk getal is dat kleiner of gelijk is aan 10. Als dat niet het geval is,
wordt de melding *De deler is niet correct.* afgedrukt.  
Als de deler correct is, wordt de rest berekend en de volgende zin afgedrukt:  
*De rest bij deling van **deeltal** door **deler** is **rest-in-letters** .  
  
Daarbij zijn **deeltal** en **deler** vervangen door de ingevoerde getallen, en is **rest-in-letters** vervangen door de gehele rest van de deling in lettervorm.
Bekijk de voorbeelden.  

Je bent verplicht om de mogelijke rest uit een lijst op te halen met als elementen ['nul', 'een', 'twee', 'drie', ...]

### Voorbeeld

```console?lang=python&prompt=>>>
>>> 15
>>> -1
De deler is niet correct.
>>> 8
>>> 0
De deler is niet correct.
>>> -5
>>> 11
De deler is niet correct.
>>> 24
>>> 6
De rest bij deling van 24 door 6 is nul .
>>> 26
>>> 5
De rest bij deling van 26 door 6 is een .
>>> 26
>>> 6
De rest bij deling van 26 door 6 is twee .
>>> 21
>>> 6
De rest bij deling van 21 door 6 is drie .
>>> 17
>>> 9
De rest bij deling van 17 door 9 is acht .
>>> 19
>>> 10
De rest bij deling van 19 door 10 is negen .
```
