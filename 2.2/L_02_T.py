sline1 = input()
sline2 = input()
sline3 = input()

nlen = 0
current = ''

if 'зайка' in sline1:
    current = sline1
    nlen = len(sline1)

if 'зайка' in sline2:
    if current == '' or (current != '' and sline2 < current):
        current = sline2
        nlen = len(sline2)

if 'зайка' in sline3:
    if current == '' or (current != '' and sline3 < current):
        current = sline3
        nlen = len(sline3)

print(f'{current} {nlen}')
