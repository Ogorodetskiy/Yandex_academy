n1 = int(input())
n2 = int(input())

for i in range(n1, n2 + (1 if n1 < n2 else -1), 1 if n1 < n2 else -1):
    print(i, end=' ')
