yyyy = int(input())

if (yyyy % 4 == 0 and yyyy % 100 != 0) or yyyy % 400 == 0:
    print('YES')
else:
    print('NO')
