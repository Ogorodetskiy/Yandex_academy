d = {}
for _ in range(int(input())):
    p = input().split()

    if not (z := f'{p[0][:-1]}-{p[1][:-1]}') in d:
        d[z] = 1
    else:
        d[z] += 1

print(max(d.values()))
