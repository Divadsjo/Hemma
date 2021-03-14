import math

# 1. En rätvinklig triangel har en katet som är 3cm, och en hypotenusa som är 5cm. Skriv ett program som beräknar den andra katetens längd.

# a^2 + b^2 = c^2
# 3^2 + b^2 = 5^2

b = math.sqrt(25-9)
print(b)

# 2. Skriv ett program som låter användaren mata in basen och höjden av en triangel. Programmet
# ska räkna ut triangelns area.

B = int(input("bas: "))
h = int(input("höjd: "))
A = (B*h)/2
print(A)

# 3. pH-värdet är ett logaritmiskt mått på surheten och definierat som: pH = − lg{H+}, där {H+} är
# aktiviteten av vätejoner H+. Skriv ett program som beräknar pH-värdet för vätejonsaktiviteten
# 1 · 10−7

pH = -math.log10(10**-7)
print(pH)

# 4. Avståndsformeln (x1, x2) d = ((x2 − x1)^2 + (y2 − y1)^2)^0,5 är en tillämpning av Pythagoras sats
# och kan användas för att räkna avståndet mellan två punkter (x1, y1) och (x2, y2) i ett koordi-
# natsystem. Skriv ett program som:
# a)

d = math.sqrt((2+2)**2+(3-2)**2)
print(d)

# b)

d = math.sqrt((2-1)**2+(0-1)**2)
print(d)

# c)
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
d = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(d)