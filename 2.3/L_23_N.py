n = int(input())

fl = 0
for i in range(2, n // 2 + 1):

    if n % i == 0:
        fl = 1
        break

print('NO' if fl == 1 or n == 1 else 'YES')
