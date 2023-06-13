n1 = int(input())
n2 = int(input())

if n1 > n2:
    g = n1
else:
    g = n2
while True:
    if g % n1 == 0 and g % n2 == 0:
        nok = g
        break
    g += 1

print(nok)
