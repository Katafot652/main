n = int(input("Введи n: "))
a = []
k = 1

while len(a) < n:
    a += [k] * k
    k += 1

print(*a[:n])
