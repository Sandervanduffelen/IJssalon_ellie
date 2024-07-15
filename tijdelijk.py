from helper import decoreer

#Hier wordt een aangemaakte functie met dictionary weergegeven
def print_aanbieding():
    prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5,
}
# Met deze code geef je korting aan vannile-ijs
    aanbieding = prijzen["vanille"] * 0.8

# Met deze code maak je en string dat de aanbieding van vanille-ijs geeft, de f geeft aan dat je tussen de { } een variabele kan plaatsen
    reclame_tekst = (f"Vaandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}")

# Hiermee zorg je ervoor dat alles in hoofdletters wordt geplaatst
    reclame_tekst3 = reclame_tekst.upper()

# Door split maak je er een list van ipv. een dictionary
    reclame_tekst4 = reclame_tekst3.split(" ")

# Deze code plaatst alles onder elkaar en zorgt ervoor dat de woorden met 5 of meer letters in hoofdletters komen en de rest in kleine letters
    for el in reclame_tekst4:
        if len(el) >= 5:
            print(el.upper())
        else:
            print(el.lower())

#Hiermee zorg je voor de titel aanbieding vanuit decoreer
decoreer("Aanbieding")
print_aanbieding()