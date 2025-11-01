s = input().strip()

result = ""
for ch in s:
    if not ch.isdigit():
        continue
    digit = int(ch)
    if digit > 5:
        digit = digit // 2
        if digit % 2 != 0:
            result += str(digit)

print(result)
