Schrijf een programma waarbij de gebruiker in één string een onbeperkt aantal gehele getallen kan ingeven, gescheiden door een spatie.   
Het programma drukt twee lijsten af:  
- een lijst met alle ingegeven even cijfers, gesorteerd van klein naar groot  
- een lijst met alle ingegeven oneven cijfers, gesorteerd van klein naar groot  

Het is verboden om de sort-method van een list te gebruiken.

Tip om een bestaande lijst oplopend te sorteren:  
- wandel door de lijst en vergelijk elk element met het voorgaande element;  
- als een element kleiner is dan zijn voorgaande, verwissel ze dan van plaats;  
- herhaal bovenstaande tot je geen enkele keer nog twee getallen van plaats hebt moeten wisselen;  

### Voorbeeld

```console?lang=python&prompt=>>>
>>> 5 7 4 6 9 1 2 8 3 10
[2, 4, 6, 8, 10]
[1, 3, 5, 7, 9]
>>> 5 -5 6 -6 -12 13 2 3 0 4 3 -3
[-12, -6, 0, 2, 4, 6]
[-5, -3, 3, 3, 5, 13]
```
