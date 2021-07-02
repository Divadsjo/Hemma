import math
import random

n = 5000 #Mängd omgångar
a = 2 #Mängd tärningskast per figurantal
b = 7 #Maxmängden figurer

best = [[3],[3,6],[5],[3,4,6],[4],[3],[3,4,6]]
worst = [[4,5,6],[4],[6],[5],[6],[6],[5]]
secondBest = [[4,5,6],[5],[3],[5],[3,5],[4,5],[5]]

diceSum = 0
sums = []
temp =[]

for x in range(n):
    tempSum = 0
    for y in range(1,b+1):
        for z in range(a):
            diceSum = 0
            for dice in range(y):
                diceSum += random.randint(1,6)
            tempResurs = best[y-1][random.randint(0,len(best[y-1])-1)]
            tempSum += tempResurs*int(diceSum/tempResurs)
    temp.append(tempSum)
sums.append(temp)
temp = []


for x in range(n):
    tempSum = 0
    for y in range(1,b+1):
        for z in range(a):
            diceSum = 0
            for dice in range(y):
                diceSum += random.randint(1,6)
            tempResurs = worst[y-1][random.randint(0,len(worst[y-1])-1)]
            tempSum += tempResurs*int(diceSum/tempResurs)
    temp.append(tempSum)
sums.append(temp)
temp = []


for x in range(n):
    tempSum = 0
    for y in range(1,b+1):
        for z in range(a):
            diceSum = 0
            for dice in range(y):
                diceSum += random.randint(1,6)
            tempResurs = secondBest[y-1][random.randint(0,len(secondBest[y-1])-1)]
            tempSum += tempResurs*int(diceSum/tempResurs)
    temp.append(tempSum)
sums.append(temp)
temp = []

for x in range(n):
    tempSum = 0
    for y in range(1,b+1):
        for z in range(a):
            diceSum = 0
            for dice in range(y):
                diceSum += random.randint(1,6)
            tempResurs = random.randint(3,6)
            tempSum += tempResurs*int(diceSum/tempResurs)
    temp.append(tempSum)
sums.append(temp)
temp = []
# print(sums)
print(sum(sums[0])/n,sum(sums[1])/n,sum(sums[2])/n,sum(sums[3])/n)
wins = [0,0]
print(len(sums[0]),len(sums[3]))
for x in range(n):
    if sums[0][x] > sums[3][x]:
        wins[0] += 1
    elif sums[0][x] < sums[3][x]:
        wins[1] += 1
print(wins)