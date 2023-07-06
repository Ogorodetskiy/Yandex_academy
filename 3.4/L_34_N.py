from itertools import permutations
sp = []

for _ in range(int(input())):
    sp.append(input())

for x in sorted(permutations(sp, 3)):
    print(*x, sep=', ')
