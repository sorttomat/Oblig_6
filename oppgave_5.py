class Person():
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        self.hobbyer = []
    
    def leggTilHobby(self, hobby):
        """
        Metode som legger til en hobby i listen med hobbyer.
        """
        self.hobbyer.append(hobby)
    
    def skrivHobbyer(self):
        """
        Metode som skriver ut alle hobbyene i listen paa en linje.
        """
        hobbyerString = "Hobbyer: "
        for hobby in self.hobbyer: #Gaar gjennom listen med hobbyer.
            hobbyerString += hobby #Legger til hobbyen i stringen.
            hobbyerString += " " #For aa faa mellomrom mellom hobbyene, legges det til et mellomrom.
        print(hobbyerString)
    
    def skrivUt(self):
        """
        Metode som printer ut informasjon om Person-objektet.
        """
        print(self.navn, self.alder)
        self.skrivHobbyer()

        