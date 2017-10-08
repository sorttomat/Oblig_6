class Motorsykkel():
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self.merke = merke
        self.registreringsnummer = registreringsnummer
        self.kilometerstand = kilometerstand
    
    def kjor(self, km):
        """
        Metode som simulerer at motorsykkelen kjoerer.
        Kilometerstanden oeker med et visst antall kilometer.
        """
        self.kilometerstand += km
    
    def hentKilometerstand(self):
        """
        Metode som returnerer objektets kilometerstand.
        """
        return self.kilometerstand

    def skrivUt(self):
        """
        Metode som printer ut informasjon om objektet.
        """
        print(self.merke, self.registreringsnummer, self.kilometerstand)
    
    