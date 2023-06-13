ind = 0
n = int(input())

for _ in range(n):
    s = input().split()

    for w in s:
        if w == 'зайка':
            ind += 1
print(ind)


# counter = 0
# for _ in range(int(input())):
#     counter += input().count("зайка")
# print(counter)
