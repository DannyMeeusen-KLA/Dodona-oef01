stijd = int(input('Geef het starttijdstip in hhmm-formaat: '))
afstand = int(input('Geef de af te leggen afstand: '))

shh = stijd//100        # startuur
smm = stijd % 100       # startminuten

sdmm = (shh * 60) + smm  # aantal minuten na middernacht dat er vertrokken wordt

admm = (sdmm + (afstand * 5)) % 1440    # aantal minuten na middernacht dat er aangekomen wordt

ahh = admm//60          # aankomstuur
amm = admm % 60         # aankomstminuten

atijd = (ahh*100)+amm
print(atijd)