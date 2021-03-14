import random
while True:
    sums = 0
    for x in range(int(input("Antal kast = "))):
        sums += random.randint(1,6)
    print(sums/x)