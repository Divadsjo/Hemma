n = int(input("Antal: "))
list = []
a = []
b = 0
for x in range(n):
    list.append(int(input("pris: ")))
list.sort()
for x in range(1, int(n/3)+1):
    list.pop(-2*x-1)
for x in range(len(list)):
    b += list[x]
print(b)