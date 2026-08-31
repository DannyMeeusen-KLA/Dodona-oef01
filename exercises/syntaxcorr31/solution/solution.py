# Opgave 1:
# Iemand spaart elke maand een bepaald bedrag tot een bepaald spaardoel is bereikt.
# Lees het maandelijks gespaarde bedrag en het te bereiken bedrag in en bereken via een while het aantal benodigde maanden
# (we weten allemaal dat dit op een andere manier simpeler kan)

perMaand = int(input('Het maandelijks gespaarde bedrag: '))
doel = int(input ('Het te bereiken bedrag: '))

gespaard = 0
aantalMaanden = 0

while gespaard < doel:
    gespaard = gespaard + permaand
    aantalMaanden = aantalMaanden + 1

print (aantalMaanden)


# Opgave 2:
# Vraag de gebruiker om een positief decimaal getal in te brengen.
# Het programma halveert vervolgens telkens dit getal tot het kleiner dan 1 wordt.
# Druk het aantal stappen af vooraleer dit gebeurt.

getal = float(input('Geef een positief decimaal getal: '))

aantalStappen = 0
while getal >= 1:
    getal = getal / 2
    aantalStappen = aantalStappen + 1

print (aantalStappen)


# Opgave 3:
# Lees woorden in tot de gebruiker het woord 'stop' typt.
# Het programma telt het aantal woorden vooraleer 'stop' werd ingetikt en drukt dit aantal af.

aantalKeer = 0
while True:
    woord = input ('Tik een woord: ')
    if woord == 'stop':
        break
    aantalKeer = aantalKeer + 1

print (aantalKeer)