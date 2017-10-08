"""
Dette programmet leser inn en fil med informasjon om ansatte og salg per ansatt i en bedrift. 
Ved hjelp av funksjoner og prosedyrer, finner programmet ut hvem som har solgt mest, totalt antall salg og 
gjennomsnittsalg.
"""

def innlesing(filnavn):
    """
    Funksjon som leser inn en fil, splitter hver linje opp, og legger informasjonen inn i en ordbok.
    """
    innfil = open(filnavn, "r")
    linjer = innfil.readlines()
    innfil.close()

    ordbok = {}
    for linje in linjer:
        data = linje.split(" ")
        ordbok[data[0]] = int(data[1])
    return ordbok

def maanedensSalgsperson(ordbok):
    """
    Prosedyre som finner og printer ut personen med stoerst salg, samt hva salget var.
    """
    maks = 0
    ansatt = None
    for key in ordbok:
        if ordbok[key] > maks:
            maks = ordbok[key]
            ansatt = key
    print("{} er maanedens salgsperson, med {} salg.".format(ansatt, maks))

def totaltAntallSalg(ordbok):
    """
    Funksjon som returnerer totalt antall salg.
    """
    total = 0
    for key in ordbok:
        total += ordbok[key]
    return total

def gjennomsnittSalg(ordbok):
    """
    Funksjon som returnerer gjennomsnittlig salg per person.
    """
    total = totaltAntallSalg(ordbok)
    return total/len(ordbok)

def printToLinjeskift():
    """
    Prosedyre som printer to linjeskift.
    """
    print("\n\n")



def hovedprogram():
    """
    Funksjon som kjoerer selve programmet.
    """
    ansatteSalg = innlesing("salgstall.txt")
    totaltSalg = totaltAntallSalg(ansatteSalg)
    gjennomsnitt = gjennomsnittSalg(ansatteSalg)

    if totaltSalg < 100:
        print("Dere har sparken!")
    else:
        print("\nDette har vært en bra maaned, her kommer en kort oppsummering!")
        printToLinjeskift()
        maanedensSalgsperson(ansatteSalg)
        printToLinjeskift()
        print("Aktive selgere denne maaneden var: {}.".format(len(ansatteSalg)))
        printToLinjeskift()
        print("Totalt antall salg denne maaneden ble: {}.".format(totaltSalg))
        printToLinjeskift()
        print("Gjennomsnittlig salg denne maaneden ble: {}.\n".format(gjennomsnitt))


hovedprogram()         
    
