n = int(input())
q = 0
for _ in range(n):
    fl = 0

    while (m := input()) != 'ВСЁ':
        if m == 'зайка' and fl == 0:
            q += 1
            fl = 1

print(q)
