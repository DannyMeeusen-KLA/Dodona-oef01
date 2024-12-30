tekst = input('Geef een tekst in: ')

vorige_letter = ' '
aantal_woorden = 0
for letter in tekst:
    if letter != ' ' and vorige_letter == ' ':
        aantal_woorden += 1
    vorige_letter = letter
print (aantal_woorden)