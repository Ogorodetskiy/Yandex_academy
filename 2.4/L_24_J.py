n = int(input())
print('А', 'Б', 'В')
for a in range(1, n - 1):
    for b in range(1, n - a):
        print(a, b, n - a - b)
