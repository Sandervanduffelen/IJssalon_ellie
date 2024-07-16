# Hier wordt mijn_functie_2 geïmporteerd
from algemene_functies import mijn_functie_2

# Hier is een functie aangemaakt met verschillende parameters in een string
def aanbieding_1(smaak, prijs, korting):
    reclame = (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro, voor {korting} euro.")
    return reclame

#Hier worden de argumenten voor de parameters opgeroepen en uitgeprint
print(aanbieding_1("aardbei", 4, 3.60))

# Hier is een functie met de som van alle inkomsten en het btw bedrag in euro's over de inkomsten 
def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 34], 0.09))

# Hier wordt doormiddel van max() en min() alleen het meeste en het minste bedrag uitgeprint
def laag_en_hoog(mijn_lijst):
    hoogste_bedrag = max(mijn_lijst)
    Laagste_bedrag = min(mijn_lijst)
    return hoogste_bedrag, Laagste_bedrag

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 34]))

# Hier wordt het gemiddelde op een dag berekent doormiddel van de sum() en len() functies
def gemiddelde(mijn_lijst):
    gem = sum(mijn_lijst) / len(mijn_lijst)
    return (f"De gemiddelde inkomsten deze week zijn {gem} euro.")

print(gemiddelde([220, 430, 125, 160, 205, 90, 34]))

# Dit is een ingewikkelde, waar ik wel even over heb gedaan, maar hier voer je de laag_en_hoog functie toe aan de functie meervoudig.
# Daarna zorg je met het if-statement ervoor dat de list tussen de 5 en 10 getallen moet hebben en dit return je dus met de laag_en_hoog functie gevolgd door de invoer_lijst functie
# De else functie zorgt er samen met return ervoor dat er anders de string komt te staan
def meervoudig(invoer_lijst):
    global laag_en_hoog
    if len(invoer_lijst) > 5 and len(invoer_lijst) < 10:
        return laag_en_hoog(invoer_lijst)
    else:
        return ("De list is niet tussen de 5 en 10")
    
print(meervoudig([10,5,3,2,7,8]))

def combinatie(invoer_lijst_2):
    global meervoudig
    korte_lijst = meervoudig(invoer_lijst_2)
    global mijn_functie_2
    return mijn_functie_2(korte_lijst)

print(mijn_functie_2)





