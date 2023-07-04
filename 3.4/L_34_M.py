from itertools import permutations
sp = []

for _ in range(int(input())):
    sp.append(input())

for x in sorted(permutations(sp)):
    print(*x, sep=', ')
