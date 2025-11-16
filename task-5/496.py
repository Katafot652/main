arr = list(map(int, input().split()))
x = int(input())

positions = []

for i in range(len(arr)):
    if arr[i] == x:
        positions.append(i + 1)  # +1 бо позиції з 1

if positions:
    print(*positions)
else:
    print("None")
