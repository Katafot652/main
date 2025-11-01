t = int(input("Enter hours: "))
cells = 1

for i in range(t // 3):
    cells *= 2

print(cells)