q = 0
for _ in range(int(input())):
    p = input()
    if p == p[::-1]:
        q += 1
print(q)
