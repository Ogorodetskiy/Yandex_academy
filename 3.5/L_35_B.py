from sys import stdin

lines = []
delta1 = 0
delta2 = 0
n = 0

for line in stdin:
    lines = line.rstrip('\n').split(' ')
    n += 1
    delta1 += int(lines[1])
    delta2 += int(lines[2])

print(round((delta2 - delta1) / n))
