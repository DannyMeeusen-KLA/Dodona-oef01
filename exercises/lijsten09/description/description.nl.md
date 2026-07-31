We willen een brief sturen naar meerdere bestemmelingen.  
De voornamen van de bestemmelingen worden, lijn per lijn, ingegeven. Beëindig de lijst met een lege input.  
Druk vervolgens de aanspreking van de brief als volgt af:  
- Druk een komma en een spatie af tussen twee opeenvolgende bestemmelingen, maar ...  
- Tussen de voorlaatste en laatste naam dient geen komma afgedrukt te worden, wel het woord 'en'.   
- Als er slechts één naam wordt ingegeven, dient er uiteraard geen komma of 'en' getoond te worden.  
- Als er geen namen worden ingegeven, dient de melding 'Geen bestemmelingen!' afgedrukt te worden.  

Bekijk de voorbeelden.  
  
<u>Tips:</u>
- Lees de namen in met een *while* en steek ze in een lijst.  
- Geef de uitvoerstring een beginwaarde:  
  - 'Geen bestemmelingen!' als de lijst met namen leeg is.  
  - 'Beste ' als de lijst minstens één naam bevat.  
- Wandel door de lijst vanaf het eerste tot en met het op twee na laatste element en voeg deze achteraan toe aan de uitvoerstring, gevolgd door een komma en een spatie.  
- Voeg het voorlaatste element (als dat er is!) achteraan toe aan de uitvoerstring, gevolgd door ' en '.  
- Voeg het laatste element (als dat er is!) achteraan toe aan de uitvoerstring.  
  
  
### Voorbeeld

```console?lang=python&prompt=>>>
>>> Anna 
>>> Bert 
>>> Cathy 
>>> Dorien 
>>> 
Beste Anna, Bert, Cathy en Dorien

>>> Anna 
>>> Bert 
>>> Cathy 
>>> 
Beste Anna, Bert en Cathy

>>> Anna 
>>> Bert 
>>> 
Beste Anna en Bert

>>> Anna 
>>> 
Beste Anna

>>> 
Geen bestemmelingen!
```