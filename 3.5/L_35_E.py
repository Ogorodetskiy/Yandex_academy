from sys import stdin

lines = []
dest = set()

for line in stdin:
    lines.append(line.rstrip("\n"))

print(lines)
for txt in lines:

    if txt.upper() == txt.upper()[::-1]:
        print(txt)
