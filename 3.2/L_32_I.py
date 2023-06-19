slv = dict()
while (txt := input()) != '':
    for b in txt.split():
        if b not in slv:
            slv[b] = 1
        else:
            slv[b] = slv[b] + 1

for x in slv.keys():
    print(x, slv[x])  # key, value
