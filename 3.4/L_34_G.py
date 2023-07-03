from itertools import combinations

spis = list()

for _ in range(int(input())):
    spis.append(input())

for par in combinations(spis, 2):
    print(f'{par[0]} - {par[1]}')
