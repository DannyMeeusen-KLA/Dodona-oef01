tekst = input('Geef een tekst in: ')

aantal_klinkers = 0
for letter in tekst:
    if letter in 'aeiouAEIOU':
        aantal_klinkers += 1

print (aantal_klinkers)
