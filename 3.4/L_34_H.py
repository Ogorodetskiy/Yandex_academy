from itertools import islice

q = int(input())
spis = list()

for _ in range(q):
    spis.append(input())

n = int(input())

print(*islice(spis * (n // q + 1), 0, n, 1), sep='\n')
