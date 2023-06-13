n = int(input())
k = int(input())
w = len(str(n * k))
for i in range(1, n + 1):
    for j in range(i, i + n * (k - 1) + 1, n):
        if j == i + n * (k - 1):
            print(f'{j:>{w}}')
        else:
            print(f'{j:>{w}}', end=' ')
