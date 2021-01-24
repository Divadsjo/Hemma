#0. Ge instruktioner på hur programet funkar
#1. ta ett ord på random sätt
#2. Gör en varibal mer original ordet och en som är tom med det man gissar.
#3. Ta in en gissning och se om den finns i original ordet
#   3a. Om den finns byt ut alla instanser av den i det tomma ordet med hjälp av
#   index som ligger i en list
#   3b. om den inte finns så lägg till en lem på gubben och räkna ner gissningarna.
#4a. om man kom på ordet så skriv nåt grattis meddelande
#4b. Om man inte kom på ordet skriv nåt meddelande och kanske repetera hela programet.  
import hangman_words
hangmanPics = ['''






''', '''






=========''','''
      +
      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def wordGenerator():
    pass
def playAgain():
    print('''
    Vill du spela igen?
    
    (1) Ja
    
    (2) Nej, avsluta spelet
    ''')
    blä = int(input(""))
    return blä


def inputBokstav():
    while True:
        bok = str(input()).lower()
        if felSvar.count(bok) != 0:
            print("Välj en ny bokstav")
            continue
        elif len(bok) > 1:
            print("Skriv en bokstav i taget")
            continue
        else:
            break
    return bok

def gissningarKvar(fel):
    print(hangmanPics[fel], "\n\n"," ".join(felSvar),'''

=========

''', "".join(gissning),"\n\nGissning:")



def continueGame():
    print("\n----------------------------------------------------\n            Continue game?\n\n(1) Play again\n\n(2) Exit game\n")
    continueAnswer = int(input(""))
    return continueAnswer

def difficultyAndWordGeneration():
    print('''
    --------------------------------------------------
    
    Välj längd på orden
    
    (1) 1-5 bokstäver
    
    (2) 6-10 bokstäver
    
    (3) 11-20 bokstäver
    ''')





print('''Välkommen till hangman

Målet med detta spel är att gissa ett ord. Spelet går i turordning där varje spelare får 
gissa på en bokstav som ordet innehåller. Om spelarna gissar fel läggs en del till på den hängda gubben
samanlagt har de max 10 stycken fel svar och om de når 10 så förlorar de. Det måste även inte bara vara ett 
ord utan de kan vara flera men spelarna får vet längde på orden med hjälp av understreck.
Exempel: ___ _____ __ 

Lycka till!
''')

while True:
    difficultyAndWordGeneration()
    ord = hangman_words.pickWord(int(input("")))
    antalFel = 0
    bokstav = ""
    gissning = []
    felSvar = []
    for x in range(len(ord)):
        if ord[x] == " ":
            gissning.append(" ")
            continue
        else:
            gissning.append("_")
    while True:
        if antalFel == 10:
            print("Slut på gissningar, du förlorar :(")
            if playAgain() == 2:
                exit()
            break
        elif gissning == ord:
            print("Wohoo du gissade på rätt ord!")
            if playAgain() == 2:
                exit()
            break
        if bokstav == "":
            gissningarKvar(antalFel)
            bokstav = inputBokstav()
        elif ord.count(bokstav) == 0:
            antalFel += 1
            felSvar.append(bokstav)
            gissningarKvar(antalFel)
            bokstav = inputBokstav()
        else:
            for y in range(len(ord)):
                if ord[y] == bokstav:
                    gissning[y] = bokstav
                else:
                    continue
            gissningarKvar(antalFel)
            bokstav = inputBokstav()
               