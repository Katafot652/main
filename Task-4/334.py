n = int(input("Введіть число пінгвінів від 1 до 9: "))

# Рядки шаблону пінгвіна
row1 =     "   _~_    "
row2 =   "  (o o)   "
row3 =   " /  V  \\  "
row4_template = "/(  {}  )\\ "
row5 =    "  ^^ ^^   "

row1_all = ""
row2_all = ""
row3_all = ""
row4_all = ""
row5_all = ""

for i in range(1, n + 1):
    row1_all += row1 + " "
    row2_all += row2 + " "
    row3_all += row3 + " "
    row4_all += row4_template.format(i) + " "
    row5_all += row5 + " "

# Виводимо пінгвінів рядок за рядком
print(row1_all)
print(row2_all)
print(row3_all)
print(row4_all)
print(row5_all)
