from itertools import product, permutations

suits_ro = sorted(["бубен", "пик", "треф", "червей"])
nominal = sorted(["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"])

suit, exception, situation = input(), input(), input()
best_suit = [s for s in suits_ro if s.startswith(suit[0])][0]

nominal.remove(exception)
comb = permutations(product(nominal, suits_ro), 3)
y = sorted(set([', '.join(' '.join(j) for j in sorted(i)) for i in comb]))
triads = [i for i in y if best_suit in i]
for ind, triad in enumerate(triads):
    if triad == situation:
        print(triads[ind + 1])
        break