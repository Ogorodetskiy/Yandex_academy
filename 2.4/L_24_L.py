n = int(input())
k = int(input())
w = len(str(n * k))
for i in range(1, n + 1):
    for j in range(k * (i - 1) + 1, k * i + 1):
        if j == k * i:
            print(f'{j:>{w}}')
        else:
            print(f'{j:>{w}}', end=' ')
