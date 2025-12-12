def sum_three(a, b, c):
    if a == b or a == c or b == c:
        return 0
    return a + b + c


a, b, c = map(int, input().split())
print(sum_three(a, b, c))
