nl = int(input())

n1 = nl // 100
n2 = (nl // 10) % 10
n3 = nl % 10

max1 = max(n1, n2, n3)
min1 = min(n1, n2, n3)

if (max1 == n3 and min1 == n2) or (max1 == n2 and min1 == n3):    
    print('YES' if n2 + n3 == n1 * 2 else 'NO')
elif (max1 == n1 and min1 == n3) or (max1 == n3 and min1 == n1):
    print('YES' if n1 + n3 == n2 * 2 else 'NO')
else:
    print('YES' if n1 + n2 == n3 * 2 else 'NO')
