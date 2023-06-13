side1 = float(input())
side2 = float(input())
side3 = float(input())

if side1 >= side2 and side1 >= side3:
    if side1 * side1 < side2 * side2 + side3 * side3:
        print('крайне мала')
    elif side1 * side1 > side2 * side2 + side3 * side3:
        print('велика')
    else:
        print('100%')
elif side2 >= side1 and side2 >= side3:
    if side2 * side2 < side1 * side1 + side3 * side3:
        print('крайне мала')
    elif side2 * side2 > side1 * side1 + side3 * side3:
        print('велика')
    else:
        print('100%')
else:
    if side3 * side3 < side1 * side1 + side2 * side2:
        print('крайне мала')
    elif side3 * side3 > side1 * side1 + side2 * side2:
        print('велика')
    else:
        print('100%')
