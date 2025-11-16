line = input().strip()
nums = list(map(int, line.split()))

counts = {}

for n in nums:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1

repeats = []
for number, count in counts.items():
    if count > 1:
        repeats.append(number)

repeats.sort()
print(*repeats)
