sp = list()

for _ in range(int(input()) + int(input())):
    sp.append(input())

fm = sorted([x for x in sp if sp.count(x) == 1])

if len(fm) > 0:
    print(*fm, sep='\n')
else:
    print('Таких нет')
