#Spel som går ut på att gissa på nummer. Antal gissningar som
#krävdes för att gissa rätt visas i slutet av spelet. Felaktiga
#värden som matas in kommer inte räknas som gissningar.

import random

#Skriver ut en intro-text
def intro():
    print("Välkommen till spelet \"Gissa talet\"")
    print("Du ska gissa vilket heltal jag tänker på")
    print("Det är ett heltal mellan 1 och 100")

#Hanterar gissningar och ser till att endast heltal accepteras    
def gissa():
    try:
        gissning = int(input("Gissa på ett heltal: "))
    except ValueError:
        print("Du måste ange ett heltal!")
        gissning = gissa()
    return gissning

def main():

    intro()
    
    #Genererar talet som ska gissas
    numret = random.randint(1,100)
    
    gissning = gissa()
    antal_forsok = 1
    
    #Loopar tills korrekt tal har gissats, variabeln med antal gissningar räknas upp varje varv
    while gissning != numret:
        if gissning > numret:
            print("Lägre...")
        else:
            print("Högre...")
        
        gissning = gissa()
        antal_forsok += 1

    print("Grattis, du hade rätt!")
    print("Det tog ", antal_forsok, " försök")
    
main();
