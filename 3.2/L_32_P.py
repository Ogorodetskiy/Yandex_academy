res = set()
while st := input().split():
    for ind, zn in enumerate(st):

        if zn == 'зайка':
            if ind == 0:
                res.add(st[ind + 1])
            elif ind == len(st) - 1:
                res.add(st[ind - 1])
            else:
                res.add(st[ind + 1])
                res.add(st[ind - 1])

print(*(x for x in res), sep='\n')
