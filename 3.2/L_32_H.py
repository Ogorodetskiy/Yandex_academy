sp = dict()
lis = list()
for i in range(int(input())):

    lis = [x for x in input().split()]
    for f in lis[1:]:
        sp[f] = sp.get(f, []) + [lis[0]]

porridge = input()

print(*sorted(sp.get(porridge, ['Таких нет'])), sep='\n')
