"""
Dette programmet importerer klassen Hund, 
oppretter et Hund-objekt og tester ut de ulike metodene i klassen.
"""

from hund import Hund

def hovedprogram():
    trofast = Hund(12, 40)
    print(trofast.hentVekt())
    trofast.spring()
    trofast.spring()
    trofast.spring()
    trofast.spring()
    trofast.spring()
    trofast.spring()
    trofast.spring()
    trofast.spring()
    trofast.spring()
    print(trofast.hentVekt())
    trofast.spis(10)
    trofast.spis(10)
    print(trofast.hentVekt())

hovedprogram()

