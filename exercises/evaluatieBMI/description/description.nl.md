Je programma geeft de gebruiker de kans om eerst de naam van een patiënt in te geven en, daarna, diens BMI.  
Als de BMI kleiner is dan 20, moet de zin verschijnen: '*De BMI van xxx is te laag*' (daarbij is xxx de naam van de patiënt).  
Als de BMI groter is dan 25, moet de zin verschijnen: '*De BMI van xxx is te hoog*' (daarbij is xxx de naam van de patiënt).  
Als de BMI in het interval [20, 25] ligt, moet de zin verschijnen: '*De BMI van xxx is perfect*' (daarbij is xxx de naam van de patiënt).  
  
Denk eraan: de antwoordzin moet helemaal gelijk zijn zoals hierboven beschreven.
### Voorbeeld

```console?lang=python&prompt=>>>
>>> Herman
>>> 21
De BMI van Herman is perfect
>>> Jean-Luc
>>> 27
De BMI van Jean-Luc is te hoog
>>> Julia
>>> 18
De BMI van Julia is te laag
```
