import math
import random
# 1. Skriv ett program som beräknar följande aritmetiska summa med hjälp av while-sats:
# s = 1 + 2 + 3 + . . . + 99 + 100
i = 1
s = 0
while i < 101:
    s += i
    i += 1
print(s) 

# 2. Skriv ett program som beräknar följande aritmetiska summa med hjälp av while-sats:
# s = 1 + 3 + 5 + . . . + 99

i = 1
s = 0
while i < 100:
    s += i
    i += 2
print(s) 

# 3. Skriv ett program som beräknar följande geometriska summa med hjälp av while-sats:
# Testa olika värden på n och dra slutsats vad summan konvergerar mot.
n = int(input("n = "))
i = 0
s = 0
while i <= n:
    s += 1/(2**i)
    i += 1
print(s) 

# 4. Skriv ett program som skriver ut värden på f(x) = x

# 2 − 3x för −2 ≤ x ≤ −2 med intervall på
# 0.1. Använd en while-sats.
i = float(-2)
while i <= 2 or i == 2:
    print((i**2)-3*i)
    i += 0.1

# 5. Skriv ett program som implementerar följande flödesschema:

tal = int(math.floor(random.random()*100))
print(tal)
gissning = int(0)
print("Gissa tal mellan 0 och 100")
while True:
    gissning = int(input("Gissning = "))
    if gissning == tal:
        print("Bra jobbat du gissade rätt!")
        break
    else:
        print("Talet är mellan", tal-int(random.random()*10), "och", tal+int(random.random()*10))