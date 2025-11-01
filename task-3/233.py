n = int(input("Скільки чисел ви введете? "))

total = 0
for i in range(n):
    num = int(input("Введіть число : "))
    total += num

print("сумма чисел:", total)