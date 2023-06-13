n = int(input())
m = int(input())

width = len(str(n * m))
for i in range(1, n + 1):
    for j in range(m):
        if not j % 2 and j != m - 1:
            print(f'{i + 2 * n * (j // 2):>{width}}', end=' ')
        elif not j % 2 and j == m - 1:
            print(f'{i + 2 * n * (j // 2):>{width}}', ' ')
        elif j % 2 and j != m - 1:
            print(f'{2 * n * (j // 2 + 1) - (i - 1):>{width}}', end=' ')
        else:
            print(f'{2 * n * (j // 2 + 1) - (i - 1):>{width}}')
