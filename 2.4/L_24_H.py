n = int(input())
s_tek = 0
pob = ''
name = ''
for i in range(1, n + 1):
    name = input()
    x = input()
    s = 0
    for j in x:
        s += int(j)
    if s >= s_tek:
        pob = name
        s_tek = s

print(pob)
