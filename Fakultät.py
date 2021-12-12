def calcIte (zahl):
    counter = zahl -1
    while counter > 0:
        zahl=zahl*counter
        counter = counter -1
    print(zahl)

calcIte(5)

def calcRek (zahl):
    if zahl == 1:
        return 1
    else:
        return zahl*calcRek(zahl-1)

print(calcRek(5))

