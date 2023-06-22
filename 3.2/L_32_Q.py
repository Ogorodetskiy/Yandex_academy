res = {}
while x := input().split():
    if x[0] not in res:
        res[x[0]] = {x[1]}
    else:
        res[x[0]].add(x[1])
    if x[1] not in res:
        res[x[1]] = {x[0]}
    else:
        res[x[1]].add(x[0])

friends_2 = dict.fromkeys(res, set())
for friend in res:
    for n in res[friend]:
        friends_2[friend] = friends_2[friend].union(res[n])
    friends_2[friend].discard(friend)
    for z in res[friend]:
        friends_2[friend].discard(z)

data = []
for friend in friends_2:
    data.append(f'{friend}: {", ".join(sorted(friends_2[friend]))}')
data.sort()
for st in data:
    print(st)
