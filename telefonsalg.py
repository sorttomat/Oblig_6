def innlesing(filnavn):
    innfil = open(filnavn, "r")
    linjer = innfil.readlines()
    innfil.close()

    ordbok = {}
    for linje in linjer:
        data = linje.split(" ")
        ordbok[data[0]] = int(data[1])
    return ordbok

def maanedensSalgsperson(ordbok):
    maks = 0
    ansatt = None
    for key in ordbok:
        if ordbok[key] > maks:
            maks = ordbok[key]
            ansatt = key
    print("{} er maanedens salgsperson, med {} salg.".format(ansatt, maks))

def totaltAntallSalg(ordbok):
    total = 0
    for key in ordbok:
        total += ordbok[key]
    return total

def gjennomsnittSalg(ordbok):
    total = totaltAntallSalg(ordbok)
    return total/len(ordbok)

def hovedprogram():
    ansatteSalg = innlesing("salgstall.txt")
    totaltSalg = totaltAntallSalg(ansatteSalg)
    gjennomsnitt = gjennomsnittSalg(ansatteSalg)

    if totaltSalg < 100:
        print("Dere har sparken!")
    else:
        print("\nDette har vært en bra maaned, her kommer en kort oppsummering!")
        print()
        print()
        maanedensSalgsperson(ansatteSalg)
        print()
        print()
        print("Aktive selgere denne maaneden var: {}.".format(len(ansatteSalg)))
        print()
        print()
        print("Totalt antall salg denne maaneden ble: {}.".format(totaltSalg))
        print()
        print()
        print("Gjennomsnittlig salg denne maaneden ble: {}.\n".format(gjennomsnitt))


hovedprogram()         
    
