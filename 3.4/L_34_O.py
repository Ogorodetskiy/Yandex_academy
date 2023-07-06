from itertools import permutations
sp = []

for _ in range(int(input())):
    sp.extend(input().split(', '))

for x in sorted(permutations(sp, 3)):
    print(*x)

