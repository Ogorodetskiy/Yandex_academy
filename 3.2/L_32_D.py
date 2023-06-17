n = int(input())
m = int(input())

man = set()
ovs = set()

for _ in range(n):
    man.add(input())

for _ in range(m):
    ovs.add(input())

print('Таких нет' if (q := len(man & ovs)) == 0 else q)
