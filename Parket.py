inp = input()
inp = inp.split(" ")
R = int(inp[0])
B = int(inp[1])
S = R + B
faktor = []
resultat = []
for x in range(1, int(S/2)):
    if S % x == 0:
        faktor.append(x)
for x in faktor:
    for y in faktor:
        if x*y == S and (x-2)*(y-2) == B and x*y-(x-2)*(y-2) == R:
            resultat.append(x)
            resultat.append(y)
if len(resultat) == 4:
    resultat.pop(2)
    resultat.pop(2)
resultat.sort()
print(resultat[1], resultat[0])


