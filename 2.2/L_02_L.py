side1 = int(input())
side2 = int(input())
side3 = int(input())

print('YES' if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2 else 'NO')
