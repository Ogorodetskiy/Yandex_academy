n_min = 0
n_max = 1001

for i in range(10):    

    n = (n_min + n_max) // 2
    print(n)
    ans = input()
    if ans == 'Меньше':
        n_max = n
    elif ans == 'Больше':
        n_min = n
    else:
        break
