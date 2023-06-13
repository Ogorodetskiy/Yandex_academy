nm1 = input()
nm2 = input()

ls = sorted(([nm1[0], nm1[1], nm2[0], nm2[1]]))

r1 = ls.pop(3)
r2 = (int(ls[1]) + int(ls[2])) % 10
r3 = ls[0]

print(r1 + str(r2) + r3)
