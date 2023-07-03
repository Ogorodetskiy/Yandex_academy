from itertools import product

n = int(input())

print('А Б В')
for i in product(range(1, n - 1), range(1, n - 1)):
    if i[0] + i[1] < n:
        print(f'{i[0]} {i[1]} {n - i[0] - i[1]}')
