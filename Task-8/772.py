import os

os.chdir(os.path.dirname(__file__))

for name in ["f1.py", "input.txt", "14.py"]:
    if not os.path.isfile(name):
        raise TypeError("not file")
    print(f"{name} {os.path.getsize(name)} Bytes")
