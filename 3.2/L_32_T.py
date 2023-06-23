data = sorted(map(int, input().split('; ')))
res = dict.fromkeys(data)
for i in data:
    for j in data:
        a, b = i, j
        while b:
            a, b = b, a % b
        if a == 1:
            if res[i]:
                res[i].add(j)
            else:
                res[i] = {j}
for n in res:
    if res[n]:
        print(f'{n} - {", ".join(map(str, sorted(res[n])))}')
