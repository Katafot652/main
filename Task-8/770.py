import os

def read_lines():
    path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]

print(read_lines())
