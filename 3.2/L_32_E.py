sp = list()

for _ in range(int(input()) + int(input())):
    sp.append(input())

print(quant if (quant := len([x for x in sp if sp.count(x) == 1])) else 'Таких нет')
