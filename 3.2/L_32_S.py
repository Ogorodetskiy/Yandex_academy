data = []
for _ in range(int(input())):
    k = list(map(lambda x: x.rstrip(','), input().split()))
    data.extend(set(k[1:]))

data = sorted(toy for toy in data if data.count(toy) == 1)

for res in data:
    print(res)
