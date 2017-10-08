class Hund():
    def __init__(self, alder, vekt):
        self.alder = alder
        self.vekt = vekt
        self.metthet = 10
    
    def hentAlder(self):
        """
        Metode som returnerer alderen til hund-objektet.
        """
        return self.alder

    def hentVekt(self):
        """
        Metode som returnerer vekten til hund-objektet.
        """
        return self.vekt

    def spring(self):
        """
        Metode som simulerer at hunden springer, 
        noe som minsker mettheten og eventuelt vekten til hund-objektet.
        """
        self.metthet -= 1
        if self.metthet < 5:
            self.vekt -= 1
        
    def spis(self, mengde):
        """
        Metode som simulerer at hunden spiser.
        Mettheten og eventuelt vekten oeker.
        """
        self.metthet += mengde
        if self.metthet > 7:
            self.vekt += 1
    
    