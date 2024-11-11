patient = input('Geef de naam van de patiënt: ')
BMI = int(input('Geef de BMI van de patiënt: '))

if BMI < 20:
    print ("De BMI van", patient, "is te laag.")
elif BMI <= 25:
    print ("De BMI van", patient, "is perfect.")
else:
    print ("De BMI van", patient, "is te hoog.")
