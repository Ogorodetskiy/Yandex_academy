ax = float(input())
bx = float(input())
cx = float(input())

if ax == 0 and bx == 0 and cx == 0:
    print("Infinite solutions")
elif ax != 0 and bx != 0 and cx == 0:
    x1 = 0
    x2 = -bx / ax
    l_x = sorted([x1, x2])
    print(f'{l_x[0]:.2f} {l_x[1]:.2f}')
elif ax != 0 and bx == 0 and cx != 0:
    if -cx / ax < 0:
        print("No solution")
    else:
        x1 = (-cx / ax) ** 0.5
        x2 = -(-cx / ax) ** 0.5
        l_x = sorted([x1, x2])
        print(f'{l_x[0]:.2f} {l_x[1]:.2f}')
elif ax == 0 and bx != 0 and cx != 0:
    x1 = -cx / bx
    print(f'{x1:.2f}')
elif ax == 0 and bx == 0 and cx != 0:
    print("No solution")
elif (ax != 0 and bx == 0 and cx == 0) or (ax == 0 and bx != 0 and cx == 0):
    x1 = 0
    print(f'{x1:.2f}')
elif ax != 0 and bx != 0 and cx != 0:
    D = bx ** 2 - (4 * ax * cx)
    if D < 0:
        print("No solution")
    elif D == 0:
        x1 = -bx / 2 * ax
        print(f'{x1:.2f}')
    elif D > 0:
        x1 = (-bx + D ** 0.5) / (2 * ax)
        x2 = (-bx - D ** 0.5) / (2 * ax)
        l_x = sorted([x1, x2])
        print(f'{l_x[0]:.2f} {l_x[1]:.2f}')
