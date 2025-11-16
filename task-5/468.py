s = input().strip().split()
lst = [int(x) for x in s]

k = 3  

while len(lst) > 0:
    print(lst)
    idx = (k - 1) % len(lst)  
    lst.pop(idx)

print(lst) 