# 1. Skriv ett program med hjälp av for-sats som:
# (a) skriver ut talen 1, 2, . . . , 10 (*)
s = ""
for x in range(1,11):
    s += str(x)
print(s)
# (b) skriver ut talen −10, −9, . . . , 9, 10 (*)
s = ""
for x in range(-10,11):
    s += str(x)
print(s)
# (c) skriver ut talen 10, 9, . . . , 1, 0
s = ""
for x in range(10,0,-1):
    s += str(x)
print(s)

# 2. Skriv ett program som skriver ut alla primtal från 1 till 100 med hjälp av en for-sats.

s = "2 "
state = False
for x in range(1,101,):
    for y in range(2,x):
        state = False
        if x%y == 0:
            break
        state = True
    if state == True:
        s += str(x)
        s += " "
print(s)

# 3. Skriv ett program som beräknar följande aritmetiska summa med hjälp av for-sats:
# s = 1 + 2 + 3 + . . . + 99 + 100
s = int(0)
for x in range(101):
    s += x
print(s)

# 4. Skriv ett program som beräknar följande aritmetiska summa med hjälp av for-sats:
# s = 1 + 3 + 5 + . . . + 99

s = int(0)
for x in range(1, 100, 2):
    s += x
print(s)

# 5. Skriv ett program som:
# (a) Skriver ut femmans multiplikationstabell från 0 till 10 (*)
for x in range(11):
    print("5*",x, " = ",x*5)
# (b) Låter användaren mata in vilken tabell, start- och slut för tabellen. (*)
tabell = int(input("Vilken tabell = "))
start = int(input("Start = "))
slut = int(input("Slut = "))
for x in range(start, slut+1):
    print(tabell,"*",x, " = ",x*tabell)
# (c) Skriver ut hela multiplikationstabellen från 0 till 10. Tips: använd dig av nästlade for-satser
# och följande print: print(f”{tal :< 4}” , end = ” ”)
for x in range(1,11):
    for y in range(1,11):
        print(x*y, end = " ")
    print(" ")

# 6. Skriv ett program som beräknar följande geometriska summa med hjälp av for-sats:

# Testa olika värden på n och dra slutsats vad summan konvergerar mot.
s = float(0)
n = int(input("n = "))
for x in range(n+1):
    s += 1/(2**x)
print(s)

# 7. Skriv ett program som beräknar n! (n-fakultet), dvs .
# n! = 1 · 2 · 3 · . . . · (n − 1) · n
# Låt användaren mata in ett heltal n.

s = int(1)
n = int(input("n = "))
for x in range(1, n+1):
    s *= x
print(s)

# 8. Skriv ett program som beräknar följande summa med hjälp av for-sats.

# Testa olika värden på n och dra slutsats vad summan konvergerar mot.
s = float(0)
nominator = 1
n = int(input("n = "))
for x in range(n+1):
    for y in range(1, x+1):
        nominator *= y
    s += 1/nominator
    nominator = 1
print(s)