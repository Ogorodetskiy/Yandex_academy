from sys import stdin

lines = []

for line in stdin:
    lines.append(line.rstrip("\n"))

dest = lines[-1].upper()

for txt in lines[:-1]:

    if txt.upper().find(dest) != -1:
        print(txt)
