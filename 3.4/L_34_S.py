from itertools import permutations

x = input()
args = sorted({i for i in x if i.isupper()})

print(*args, 'F', sep=' ')

for val in sorted(set(permutations([0, 1]*len(args), len(args)))):
    exec(', '.join(args) + " = map(int, val)")
    print(*val, int(eval(x)))

