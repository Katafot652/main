n = int(input())
rows = [input().strip() for _ in range(n)]

max_len = max(len(r) for r in rows)

for i, r in enumerate(rows, start=1):
    if len(r) == max_len:
        print(i)
