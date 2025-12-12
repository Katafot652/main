def contains_number(lst, n):
    return n in lst

numbers = list(map(int, input().split()))
n = int(input())

print(contains_number(numbers, n))
