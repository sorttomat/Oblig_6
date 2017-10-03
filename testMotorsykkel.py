from motorsykkel import Motorsykkel

def hovedprogram():
    sykkel1 = Motorsykkel("Audi", "ABC123", 0)
    sykkel2 = Motorsykkel("BMW", "DEF456", 250)
    sykkel3 = Motorsykkel("Aprilia", "GHI789", 1000)
    
    sykkel1.skrivUt()
    sykkel2.skrivUt()
    sykkel3.skrivUt()

    sykkel3.kjor(10)
    print(sykkel3.hentKilometerstand())

hovedprogram()

