status = ""
inp = str(input())
a = 0
for x in range(3):
    status = inp[0]
    r = x
    for x in range(1, len(inp)):
        if inp[x] == status:
            print("hej")
            continue
        else:
            print("då")
            a += 1
            status = inp[x]
            if r == 1:
                status = "D"
            elif r == 2:
                status = "U"
    print(a)
    a = 0