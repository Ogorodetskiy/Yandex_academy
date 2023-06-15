line = input()
tek, q = line[0], 1
for i in line[1:]:
    if i == tek:
        q += 1
    else:
        print(tek, q)
        tek, q = i, 1
print(tek, q)
