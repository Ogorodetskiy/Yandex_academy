prod = list()
dishes = set()

for _ in range(int(input())):
    prod.append(input())
for _ in range(int(input())):
    dishes.add(st := input())
    for _ in range(int(input())):
        if input() not in prod:
            dishes.discard(st)

if dishes:
    for res in sorted(dishes):
        print(res)
else:
    print('Готовить нечего')
