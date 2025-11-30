numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

seen = set()

for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num) 
