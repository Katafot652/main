a = list(map(int, input().split()))
b = list(map(int, input().split()))

set_a = set(a)
set_b = set(b)

common = set_a & set_b

print(len(common))
