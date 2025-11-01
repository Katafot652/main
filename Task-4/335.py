s1 = input("Введіть перший рядок: ")
s2 = input("Введіть другий рядок: ")

digits1 = ""
digits2 = ""

for ch in s1:
    if ch.isdigit():
        digits1 += ch

for ch in s2:
    if ch.isdigit():
        digits2 += ch

print(digits1)
print(digits2)
