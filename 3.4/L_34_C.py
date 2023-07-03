from itertools import count
start, stop, step = map(float, input().split())

for i in count(start, step):
    if i <= stop:
        print(f'{i:.2f}')
    else:
        break
