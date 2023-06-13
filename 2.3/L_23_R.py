n = int(input())
step = 2

res = ''

while n > 1:

    if n % step:
        step += 1
    else:
        res = res + str(step) + ' * '
        n = n / step

print(res[0:-3])
