from itertools import permutations
x = input()

print('a b c f')

for a, b, c in [[z[0], z[1], z[2]] for z in sorted(set(permutations([0, 0, 0, 1, 1, 1], 3)))]:
    print(a, b, c, int(eval(x)))
