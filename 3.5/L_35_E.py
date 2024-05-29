from sys import stdin

dest = set()

lines = stdin.read().split()

for txt in lines:
    if txt.upper() == txt.upper()[::-1]:
        dest.add(txt)

print(*sorted(dest), sep='\n')
