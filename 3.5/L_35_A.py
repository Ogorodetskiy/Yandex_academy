from sys import stdin

lines = []

for line in stdin:
    lines += map(int, line.rstrip('\n').split(' '))

print(sum(lines))
