n = int(input())

res = 1

for i in range(n):
    print(res)
    if res == n:
        break
    res += 1
    for x in range(i + 1):
        if res == n:
            break
        print(res, sep=' ', end=' ')

        res += 1
