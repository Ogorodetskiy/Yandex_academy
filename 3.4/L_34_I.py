from itertools import product

n = int(input())

sp = range(1, n + 1)
for i in sp:
    print(*map(lambda x: x[0] * x[1], product(sp, [i])))
