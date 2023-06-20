n = int(input())
sp = dict()
q = 0

for _ in range(n):
    fam = input()
    if fam in sp:
        sp[fam] = sp[fam] + 1
    else:
        sp[fam] = 1

for key in sp:
    if sp[key] > 1:
        q += sp[key]

print(q)
