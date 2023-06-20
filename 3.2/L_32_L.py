import operator

n = int(input())
sp = dict()
q = 0

for _ in range(n):
    fam = input()
    if fam in sp:
        sp[fam] = sp[fam] + 1
    else:
        sp[fam] = 1

if max(sp.items(), key=operator.itemgetter(1))[1] == 1:
    print('Однофамильцев нет')
else:

    for key in sorted(sp):
        if sp[key] > 1:

            print(f'{key} - {sp[key]}')
