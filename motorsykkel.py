class Motorsykkel():
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self.merke = merke
        self.registreringsnummer = registreringsnummer
        self.kilometerstand = kilometerstand
    
    def kjor(self, km):
        self.kilometerstand += km
    
    def hentKilometerstand(self):
        return self.kilometerstand

    def skrivUt(self):
        print(self.merke, self.registreringsnummer, self.kilometerstand)
    
    