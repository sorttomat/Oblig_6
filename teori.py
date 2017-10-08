"""
1. Innkapsling er aa sorge for at klassens variabler og instans-variabler forblir lokale (altsaa inne i klassen).
For eksempel det at brukeren ikke skal kunne ved et uhell endre paa en av disse variablene. Derfor er det vanlig
aa ha metoder for aa hente ut variablene (hvis man hadde en self.teller = *noe*, vil man ofte ha en metode hentTeller() som 
henter telleren ut til brukeren.). Paa denne maaten er variablene trygge for uforsvarlig paavirkning. 

2. Grensesnittet til en klasse, er klassens metoder. Det er den delen av klassen som kan kalles paa utenifra,
og er det eneste man som bruker egentlig skal kunne røre. 
Implementasjonen til en klasse er det som brukeren ikke ser. Hvilke variabler som finnes i klassen, og hvordan metodene er bygget opp. 

3. En instansmetode brukes naar man skal opprette et objekt av en klasse. Den inneholder noen instansvariabler som er forhaandsbestemt. 
Brukeren maa oppgi verdier for disse for aa kunne opprette objektet. 
Den forste forskjellen jeg ser, er at disse metodene kun definerer variabler. De returnerer ingenting, og printer ingenting. 
De inneholder ogsaa et parameter brukeren ikke ser, nemlig "self". "self" brukes for aa koble variablene til selve objektet, og paa den maaten gjore 
dem utigjengelige for brukeren. 
"""