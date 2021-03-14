import math

# # 1. Formeln för aritmetisk summa är:

# # (a) Skriv en funktion som beräknar aritmetisk summa. Funktionen ska heta aritmetisk_summa
# # och ha parametrarna n, a1, an. (*)



# # (b) Använd din funktion för att beräkna summan s100 = 1 + 2 + 3 + · · · + 100 (*)
# # (c) Låt användaren mata in a1, an, n och programmet ska anropa funktionen aritmetisk_summa
# # och därefter skriva ut resultatet på ett snyggt formaterat sätt.

def aritmetisk_summa(n, a1, an):
    s = (n*(a1+an))/2
    return s


s100 = aritmetisk_summa(100, 1, 100)
print(s100)

aritmetisk_summa(int(input("n = ")),int(input("a1 = ")),int(input("a2 = ")))

# 2. Gör en funktion som beräknar summan:
# s = 1 + 3 + 5 + · · · + (2n + 1)

def oddSum(n):
    return sum([i for i in range(1,2*n+2,2)])

def oddSumStartValue(n, start):
    return sum([i for i in range(start, 2*n+2,2)])

# (a) Låt användaren mata in ett n och programmet ska skriva ut resultatet på ett snyggt for-
# materat sätt (*)

print(oddSum(int(input("n = "))))

# (b) Gör om funktionen så att användaren kan mata in ett startvärde och ett n. Funktionen ska
# ge resultatet på ett snyggt formaterat sätt. (*)


print(oddSumStartValue(int(input("n = ")), int(input("start = "))))
# 3. Punkterna P1 och P2 är markerade i koordinatsystemet.

def punktDis(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

print(punktDis(int(input("x1 = ")),int(input("y1 = ")),int(input("x2 = ")),int(input("y2 = "))))
# (a) Beräkna avståndet mellan dessa punkter (*)
# (b) Skriv en funktion som tar in två punkter som inparametrar och som returnerar avståndet. (*)
# (c) Låt användaren mata in två punkter och använd funktionen för att beräkna avståndet
# mellan dessa punkter. (*)
# 4. Skapa en funktion som tar in en summa pengar som inparameter. Den ska skriva ut lämpliga

# sedlar/mynt som representerar denna summa. Ex 5839 ska skriva ut: 5 tusenlappar, 4 tvåhund-
# ralappar, 1 tjugolapp, 1 tia, 1 femokrona och 4 enkronor. (*)

def convertMoney(money):
    tusen = 0
    tvåhundra = 0
    etthundra = 0
    tjugo = 0
    tio = 0
    fem = 0
    en = 0
    while money >= 1000:
        money -= 1000
        tusen += 1
    while money >= 200:
        money -= 200
        tvåhundra += 1    
    while money >= 100:
        money -= 100
        etthundra += 1
    while money >= 20:
        money -= 20
        tjugo += 1
    while money >= 10:
        money -= 10
        tio += 1
    while money >= 5:
        money -= 5
        fem += 1
    while money >= 1:
        money -= 1
        en += 1
    print(tusen, "Tusenlappar", tvåhundra, "Tvåhundralappar",etthundra,"Hundralapp",tjugo,"Tjugolappar,",tio,"Tia",fem,"Femma",en,"Enkronor")

convertMoney(int(input("Money = ")))
# 5. Skapa följande funktioner som tar in ett heltal n som parameter:
# (a) och returnerar n! (n-fakultet). n! = n · (n − 1)(n − 2). . . 2 · 1 (*)

def fakultet(n):
    sum = 1
    for x in range(1,n+1):
        sum *= x
    return sum

print(fakultet(7))

# (b) och beräknar följande summa s = 1 + 1 +

def inverteradFakultet(n):
    return sum([1/fakultet(i) for i in range(n+1)])

print(inverteradFakultet(7))


# (**)

# (c) och beräknar följande summa s = 1 −

def inverteradOjämnt(n):
    return sum([((-1)**(i+1))/(2*i-1) for i in range(1,n+1)])

print(inverteradOjämnt(5))

# Testa dina funktioner med olika värden på n och se vilka resultat du få