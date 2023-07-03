gr1 = input().split(', ')
gr2 = input().split(', ')

for i in range(min(len(gr1), len(gr2))):
    print(f'{gr1[i]} - {gr2[i]}')
