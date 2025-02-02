Een leerkracht gaat op uitstap met zijn leerlingen.  
Hij moet aan het secretariaat van de school doorgeven:  
- welke dag van de week hij op uitstap gaat. Geldige waarden zijn **ma**, **di**, **wo**, **do**, **vr** .  
- hoeveel leerlingen er meegaan: minimaal **1**, maximaal **24**.  
  
Schrijf een programma dat beide gegevens opvraagt, met invoercontrole:  
- eerst wordt naar de dag van de week gevraagd. Als de invoer niet één van de bovenstaande 5 waarden is, dan verschijnt de foutmelding **Foutieve dag, probeer opnieuw.** en wordt de invoer van de weekdag opnieuw gevraagd;  
- daarna wordt naar het aantal leerlingen gevraagd. Als dit aantal niet tussen 1 en 24 ligt, dan verschijnt de foutmelding **Foutief aantal, probeer opnieuw.** en wordt een nieuw aantal gevraagd;  
- uiteindelijk verschijnt de zin **Uitstap op *dag* met *aantal* leerlingen.** In deze zin worden *dag* en *aantal* uiteraard vervangen door de correct ingebrachte waarden.  
Bekijk de voorbeelden!  
  
Let op: de foutmeldingen en de uiteindelijke uitvoertekst moeten exact overeenkomen met hetgeen hierboven getoond wordt.

  
### Voorbeeld 1

```console?lang=python&prompt=>>>
>>> don
Foutieve dag, probeer opnieuw.
>>> donderdag
Foutieve dag, probeer opnieuw.
>>> do
>>> 25
Foutief aantal, probeer opnieuw.
>>> 22
Uitstap op donderdag met 22 leerlingen.
```

### Voorbeeld 2

```console?lang=python&prompt=>>>
>>> ma
>>> 0
Foutief aantal, probeer opnieuw.
>>> 20
Uitstap op maandag met 20 leerlingen.
```
