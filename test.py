def fakultet(n):
    sum = 1
    for x in range(1,n+1):
        sum *= x
    return sum

# print(fakultet(int(input("n = "))))

# (b) och beräknar följande summa s = 1 + 1 +

def inverteradFakultet(n):
    return sum([1/fakultet(i) for i in range(n+1)])

# print(inverteradFakultet(int(input("n = "))))


# (**)

# (c) och beräknar följande summa s = 1 −

def inverteradOjämnt(n):
    return sum([((-1)**(i+1))/(2*i-1) for i in range(1,n+1)])
while True:
    print(inverteradOjämnt(int(input("n = "))))