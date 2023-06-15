n = list(map(int, input().split()))
a = n[0]
while len(n) > 1:
    b = n[1]
    while b:
        a, b = b, a % b
    n.pop(1)
print(a)
