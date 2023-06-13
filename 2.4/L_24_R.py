n = int(input())
step = 1
x = 1

tree = list()

while x < n or x == 1:
    s = ''
    for i in range(x, x + step - 1):
        if x == n:
            break
        s = s + str(i) + ' '
        x = i + 1
    s = s + str(x)
    tree.append(s)
    step += 1
    x += 1

for x in tree:
    print(f'{x:^{len(tree[-1])}}')
