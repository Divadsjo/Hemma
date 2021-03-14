import math
import random
import matplotlib.pyplot as plt
# 1. Skriv ett program som simulerar 10 tärningskast, lägger in i en lista och :
# (a) sortera den från minsta talet till största (*)

s = []
for x in range(11):
    s.append(random.randint(1,6))
s.sort()
print(s)

# (b) sortera den från största talet till minsta (*)

s = []
for x in range(11):
    s.append(random.randint(1,6))
s.sort()
s.reverse()
print(s)
# 2. Använd list comprehension för att skapa en lista med kvadrater från -10 till 10,
# dvs 100, 81, . . . , 81, 100. Rita därefter dess graf. (*)

x = [i for i in range(-10, 11)]
kvadrat = [i**2 for i in range(-10, 11)]
print(kvadrat)
plt.plot(x, kvadrat)
plt.xlabel("x - axel")
plt.ylabel("y - axel")
plt.title("Gaming")
plt.show()
# 3. Använd en 2D lista för att skapa koordinaterna för ett schackbräde. (*)

cords = [[bokstav+str(siffra) for bokstav in "ABCDEFGH"] for siffra in range(1,9)]
print(cords)

# 4. Skapa en 2D lista med dimensionerna 10x10 som ska representera en spelplan och fyll med nollor.
# Slumpmässigt placera ut 30 ettor som ska representera bomber i spelplanen.
# (a) Låt användaren mata in koordinater (x,y), 0 ≤ x < 10, 0 ≤ y < 10 tills dess att man träffar
# en etta. (**)

n = 0
cords = [[0 for x in range(10)] for y in range(10)]
while n < 30:
    ranx = random.randint(0,9)
    rany = random.randint(0,9)
    if cords[rany][ranx] == 1:
        continue
    else:
        cords[rany][ranx] = 1
        n += 1
liv = 3
miss = 10
while liv != 0:
    x = int(input("x = "))
    y = int(input("y = "))
    if cords[y][x] == 1:
        liv -= 1
        print("Du träffade en etta, du har", liv, "liv kvar")
    else:
        miss -= 1
        print("Du behöver missa", miss, "gånger till")
    if miss == 0:
        print("Du vann!")
        break
# (b) Låt användaren ha 3 liv. Varje gång hen träffar en bomb ska ett liv tas bort, klarar hen 10
# omgångar utan att träffa någon bomb har hen vunnit spelet. (**)
# (c) Ge förslag på hur man kan utveckla vidare programmet och ge det ett försök.