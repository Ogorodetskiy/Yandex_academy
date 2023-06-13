r = int(input())
w = int(input())

for i in range(1, r + 1):
    if i > 1:
        print(((r * w) + (r - 1)) * '-')
    for j in range(1, r + 1):

        print(f'{i * j:^{w}}', '|' if j < r else '', sep='', end='' if j < r else '\n')
