# 1. Skriv ett program som låter användaren mata in sitt namn och programmet skriver ut antalet
# bokstäver i namnet. (*)

namn = input("Namn = ")
print(len(namn))

# 2. Skriv ett program som räknar antalet ord i denna mening: ”En bild säger mer än tusen ord, en
# matematisk formel säger mer än tusen bilder” (*)

mening = "En bild säger mer än tusen ord, en matematisk formel säger mer än tusen bilder"
print(len(mening))

# 3. Ett palindrom är en följd av tecken som är densamma när man läser framlänges som baklänges
# (man räknar inte med skiljetecken och mellanslag). Exempel på palindrom är ”Anna”, ”Ni talar
# bra latin” och ”bjkjb”.
# (a) Skriv ett program som låter användaren mata in en följd av tecken utan mellanslag och
# skiljetecken och skriv ut om följden är ett palindrom. (*)

mening = str(input("Möjligt palindrom = "))
mening = list(mening)
for x in range(mening.count(" ")):
    mening.remove(" ")
for x in range(mening.count("-")):
    mening.remove("-")
reverseMening = mening
reverseMening.reverse()
print(mening)
print(reverseMening)
if reverseMening == mening:
    print("Din mening är ett palindrom!")
else:
    print("Din mening är inte ett palindrom :(")
# (b) Skriv ett program som låter användaren skriva in en följd av tecken inklusive mellanslag
# och skiljetecken och skriv ut om följden är ett palindrom. (*)


# 4. Skriv ett program som räknar antalet vokaler i detta citat: ”Do not worry about your difficulties
# in Mathematics. I can assure you mine are still greater.” (**)

vokaler = "aeoiuyåäö"
vokaler = list(vokaler)
n = int(0)
citat = "Do not worry about your difficulties in Mathematics. I can assure you mine are still greater."
citat = list(citat.lower())
for x in vokaler:
    for y in citat:
        if x == y:
            n += 1
print(n)


# 5. Skriv ett program som låter användaren mata in ett ord.
# (a) Kryptera därefter meddelandet genom att ersätta varje bokstav med nästa bokstav. Är
# bokstaven Ö ska den ersättas med A. Exempel: ”höjd” → ”iake” (**)

# Har redan gjort i början av prog 1

# (b) Dekryptera nu meddelandet. Exempel ”lösmfl” → ”kärlek” (**)



# (c) Låt användaren skriva in ett meddelande, välja kryptera/dekryptera och utför kryptering-
# en/dekrypteringen.