"""
Dette programmet importerer klassen Person, oppretter et Person-objekt, spoer om hobbyer,
og bruker klassens metoder til aa legge til og skrive ut disse.
"""
from oppgave_5 import Person

def hovedprogram():
    person = Person("Christine", 23)
    svar = input("Skriv inn en hobby (for aa avslutte, tast x):\n> ")
    while svar != "x":
        person.leggTilHobby(svar)
        svar = input("Skriv inn en hobby (for aa avslutte, tast x):\n> ")
    
    person.skrivUt()

hovedprogram()
