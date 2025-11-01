n = int(input("Введи число: "))
if n == 0:
    print(1)
else:
    k = 0
    while n > 0:
        n //= 10
        k += 1
    print(k)
