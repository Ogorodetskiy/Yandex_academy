n = int(input())

for i in range(n):
    for j in range(n):
        d = str(min(i, j, n - i - 1, n - j - 1) + 1)
        print(f'{d:>{len(str((n + 1) // 2))}}', end=' ' if j < n - 1 else '\n')
