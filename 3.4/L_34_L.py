n = int(input())
res = []
for _ in range(n):
    res = res + input().split(', ')

res.sort()

for x, y in enumerate(res, start=1):
    print(f'{x}. {y}', sep='\n')