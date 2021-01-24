status = ""
inp = str(input())
a = 0
for x in range(1, 4):
    status = inp[0]
    r = x
    for x in range(1, len(inp)):
        if inp[x] != status:
            a += 1
            status = inp[x]
        if r == 1 and status == "U":
            status = "D"
            a += 1
        elif r == 2 and status == "D":
            status = "U"
            a += 1
    print(a)
    a = 0