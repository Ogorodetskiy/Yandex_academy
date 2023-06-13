n = int(input())
m = int(input())

width = len(str(n * m))
for i in range(1, n + 1):
    if i % 2:
        for j in range(m * (i - 1) + 1, m * i + 1):
            if j == m * i:
                print(f'{j:>{width}}')
            else:
                print(f'{j:>{width}}', end=' ')
    else:
        for j in range(m * i, m * (i - 1), -1):
            if j == m * (i - 1) + 1:
                print(f'{j:>{width}}')
            else:
                print(f'{j:>{width}}', end=' ')
