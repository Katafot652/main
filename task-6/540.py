a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

result = [key for key in a if key not in b]

print(*result)
