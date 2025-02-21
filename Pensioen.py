# Functie om het pensioenbedrag te berekenen
def bereken_pensioen(leeftijd, werkstatuut):
    """
    Berekent het wekelijkse pensioenbedrag op basis van leeftijd en werkstatuut.
    Geeft een bericht terug als de gebruiker nog niet pensioengerechtigd is.
    """
    
    # Dictionary met pensioenbedragen per werkstatuut
    # Elke waarde is een lijst: [basisbedrag, extra bedrag vanaf 70 jaar]
    pensioen_bedragen = {
        "medewerker": [350, 20],
        "zelfstandige": [300, 15],
        "ambtenaar": [370, 25]
    }

    # Als de gebruiker nog niet met pensioen mag
    if leeftijd < 65:
        return f"Van werken word je gelukkig, je mag nog {65 - leeftijd} jaar genieten van je baan."
    
    # Basis pensioenbedrag
    bedrag = pensioen_bedragen[werkstatuut][0]

    # Extra toeslag vanaf 70 jaar
    if leeftijd >= 70:
        bedrag += pensioen_bedragen[werkstatuut][1]
    
    return f"Je krijgt €{bedrag} per week."

# Invoer vragen aan de gebruiker
leeftijd = int(input("Wat is je leeftijd?\nVoer het aantal jaren in: "))
werkstatuut = input("Wat is je werkstatuut?\nVoer in: medewerker, zelfstandige of ambtenaar: ").strip().lower()

# Uitvoer van het resultaat
print(bereken_pensioen(leeftijd, werkstatuut))