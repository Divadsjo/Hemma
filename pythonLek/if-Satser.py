import math

# 1. Skriv ett program som låter användaren mata in ett tal och skriv ut om talet är positivt negativt
# eller noll.

n = int(input("tal = "))
if n == 0:
    print("Talet är noll")
elif n < 0:
    print("Talet är negativt")
elif n > 0:
    print("Talet är positivt")

# 2. Skriv ett program som låter användaren mata in ett tal och skriv ut om talet är jämnt, udda
# eller delbart med 5.

n = int(input("tal =  "))
if n % 5 == 0:
    print("Talet är delbart med 5")
elif n % 2 == 0:
    print("Talet är jämnt")
else:
    print("Talet är udda")

# 3. Skriv ett program som låter användaren mata in två tal och skriv därefter ut det största talet.

tal1 = int(input("tal1 = "))
tal2 = int(input("tal2 = "))
if tal1 > tal2:
    print(tal1)
elif tal1 < tal2:
    print(tal2)
else:
    print(tal1, tal2)

# 4. Skriv ett program som låter användaren mata in en vinkel och skriv ut om vinkeln är:
# • spetsig
# • rät
# • trubbig
# • rak
# • konvex
# • hel

v = int(input("Skriv din vinkel i grader: "))
if v < 90 and v > 0:
    print("Din vinkel är spetsig")
elif v == 90:
    print("Din vinkel är rät") 
elif v > 90 and v < 180:
    print("Din vinkel är trubbig")
elif v == 180:
    print("Din vinkel är rak")
elif v > 180:
    print("Din vinkel är konvex")
elif v == 360:
    print("Din vinkel är hel")

# 5. Skriv ett program som låter användaren mata in en radie och därefter beräknar cirkelns omkrets
# och area om radien är positiv. Om radien är negativ ska ett felmeddelande skrivas ut.

r = int(input("Radie = "))
if r <= 0:
    print("Error, din radie är negativ")
else:
    print("Omkrets =", 2*r*math.pi, "\nArea = ", math.pi*(r**2))

# 6. Skriv ett program som låter användaren mata in tre vinklar på en triangel. Avgör om triangeln
# har en rät vinkel.

v1 = int(input("Vinkel 1 = ")) 
v2 = int(input("Vinkel 2 = "))
v3 = int(input("Vinkel 3 = "))
if v1 == 90 or v2 == 90 or v3 == 90:
    print("Triangeln är rätvinklig")

# 7. Skriv ett program där användaren matar in x-koordinaten för en punkt och y-koordinaten för
# punkten. Programmet ska därefter avgöra vilken kvadrant punkten ligger i.

x = int(input("x-kordinat = "))
y = int(input("y-kordinat = "))
if x > 0 and y > 0:
    print("Punkten ligger i kvadrant 1")
elif x < 0 and y > 0:
    print("Punkten ligger i kvadrant 2")
elif x < 0 and y < 0:
    print("Punkten ligger i kvadrant 3")
elif x > 0 and y < 0:
    print("Punkten ligger i kvadrant 4")
else:
    print("Punkten ligger i origo")

# 8. I SAS är reglerna för handbaggagestorlek följande:
# • max vikt: 8kg
# • max dimension: 55cm x 40cm x 23cm (längd x bredd x höjd)
# Skriv ett program som låter användaren mata in vikten, bredden, längden och höjden på ett
# bagage. Programmet ska avgöra om bagaget är godkänt eller inte.

m = int(input("Vikt = "))
dim = str(input("Dimensioner i cm(t.ex 34*21*5) =")).split("*")
dim.sort()
if int(dim[0]) <= 55 and int(dim[1]) <= 40 and int(dim[2]) <= 23 and m <= 8:
    print("Bagaget är godkänt")
else: 
    print("Bagaget godkänts inte")

# 9. Skriv ett program som låter användaren mata in ett tal. Programmet ska skriva vad absolutbe-
# loppet av talet är. |x| =


# x, x ≥ 0
# −x, x < 0

n = int(input("Tal som ska bli absolutbelop = "))
if n < 0:
    n = -n
print(n)

# 10. En andragradsfunktion kan generellt beskrivas med f(x) = ax2 +bx+c, där a, b, c är konstanter,
# a 6= 0. Skriv ett program som löser f(x) = 0, där:
# (a)
# a = 1
# b = −1
# c = −2

# Tips: kvadratkomplettera och lös algebraiskt ut x, alternativt PQ-formeln. Analysera dis-
# kriminanten mha if-satser. (**)

# (b) användaren matar in värden på a, b, c. Testa olika värden för a,b,c och reflektera kring när
# du får två, en, respektive inga reella lösningar.

print("f(x) = ax^2 + bx + c")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
#pq-formeln 
b = b/a
c = c/a
a = 1
undersqrt = (b/2)**2 - c
if undersqrt < 0:
    print("Saknar reella röter")
else:
    x1 = -(b/2)+math.sqrt(undersqrt)
    x2 = -(b/2)-math.sqrt(undersqrt)
    if x1 == x2:
        print("x1 = x2 = ",x1)
    else:
        print("x1 = ", x1,"\nx2 = ", x2)

# 11. Skriv ett program som låter användaren mata in en punkt (x1, y1) och låt programmet avgöra
# om punkten ligger på linjen som beskrivs av funktionen f(x) = 3x + 5.

x = int(input("x = "))
y = int(input("y = "))
if x*3+5 == y:
    print("Punkten ligger på linjen")
else:
    print("Punkten ligger inte på linjen"+)