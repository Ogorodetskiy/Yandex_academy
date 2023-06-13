n = int(input())

res = 0

for _ in range(n):
    x = input()
    for i in x:
        res += int(i)
print(res)
