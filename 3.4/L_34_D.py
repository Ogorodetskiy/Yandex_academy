from itertools import accumulate

for value in accumulate(map(lambda x: ' ' + x, input().split())):
    print(value[1:])
