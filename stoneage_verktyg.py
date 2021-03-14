
d6 = [] 
temp = []
for n in range(1,8):
    for a in range(1,7):
        if n == 7:
            temp.append(a)
        for b in range(1,7):
            if n > 6:
                continue
            if n == 6:
                temp.append(a+b)
            for c in range(1,7):
                if n > 5:
                    continue
                if n == 5:
                    temp.append(a+b+c)
                for d in range(1,7):
                    if n > 4:
                        continue
                    if n == 4:
                        temp.append(a+b+c+d)
                    for e in range(1,7):
                        if n > 3:
                            continue
                        if n == 3:
                            temp.append(a+b+c+d+e)
                        for f in range(1,7):
                            if n > 2:
                                continue
                            if n == 2:
                                temp.append(a+b+c+d+e+f)
                            for g in range(1,7):
                                if n > 1:
                                    continue
                                if n == 1:
                                    temp.append(a+b+c+d+e+f+g)
    d6.append(temp)
    temp = []
d6.reverse()
tempDif = []
averageT = []
averageL = []
averageS = []
averageG = []
for x in range(1,8):
    print(len(d6[x-1]))
    print(6**(x))
for resurs in range(3,7):
    for x in range(7):
        for y in d6[x]:
            for z in range(1,15):
                if y <= resurs*z:
                    tempDif.append(resurs*z-y)
                    break
                # elif y == resurs*z:
                #     break
        if resurs == 3:
            averageT.append(sum(tempDif)/len(tempDif))
        if resurs == 4:
            averageL.append(sum(tempDif)/len(tempDif))
        if resurs == 5:
            averageS.append(sum(tempDif)/len(tempDif))
        if resurs == 6:
            averageG.append(sum(tempDif)/len(tempDif))
        tempDif = []
print(averageT,averageL,averageS,averageG) 