n = int(input())
n1 = str(n // 100)
n2 = str((n // 10) % 10)
n3 = str(n % 10)
nmax = max(int(n1 + n2), int(n1 + n3), int(n2 + n3), int(n2 + n1), int(n3 + n1), int(n3 + n2))
if int(n1 + n2) > 9:
    r1 = int(n1 + n2)
else:
    r1 = 100
if int(n1 + n3) > 9:
    r2 = int(n1 + n3)
else:
    r2 = 100
if int(n2 + n3) > 9:
    r3 = int(n2 + n3)
else:
    r3 = 100
if int(n2 + n1) > 9:
    r4 = int(n2 + n1)
else:
    r4 = 100
if int(n3 + n1) > 9:
    r5 = int(n3 + n1)
else:
    r5 = 100
if int(n3 + n2) > 9:
    r6 = int(n3 + n2)
else:
    r6 = 100
print(min(r1, r2, r3, r4, r5, r6), nmax)

