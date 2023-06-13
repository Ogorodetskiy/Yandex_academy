n = int(input())
x1 = int(input())
for _ in range(n - 1):
    xt = int(input())
    while xt:
        x1, xt = xt, x1 % xt
print(x1)
