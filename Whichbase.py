n = int(input("Antal: "))
inp = []
a = 0
c = 0
for x in range(n):
    inp.append(str(input("Tal: ")))
for x in range(n):
    nmr = str(inp[x])
    for x in range(len(nmr)):
        if int(nmr[x])== 9:
            a = 0
        else:
            a += int(nmr[-x-1])*8**(x)
        b = nmr
        c += int(nmr[-x-1])*16**x
    print(n, a, b, c)
    a = 0
    c = 0