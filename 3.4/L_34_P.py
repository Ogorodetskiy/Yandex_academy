from itertools import product, permutations

suits_ro = ["бубен", "пик", "треф", "червей"]
nominal = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

suit, exception = input(), input()

best_suit = [s for s in suits_ro if s.startswith(suit[0])][0]

nominal.remove(exception)
comb = permutations(product(sorted(nominal), sorted(suits_ro)), 3)

y = [', '.join(' '.join(j) for j in sorted(i)) for i in comb]
triads = [i for i in y if best_suit in i][:10]
for triad in triads:
    print(triad)
