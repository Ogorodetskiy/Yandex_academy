n = int(input())
q = 0
for _ in range(n):
    fl = 0
    n1 = int(input())
    if n1 != n:
        for i in range(2, n1 // 2 + 1):

            if n1 % i == 0:
                fl = 1
                break
        if not (fl == 1 or n == 1):
            q += 1
print(q)
