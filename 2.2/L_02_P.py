pet = int(input())
vas = int(input())
tol = int(input())

win1 = ''
win2 = ''
win3 = ''


if pet > vas and pet > tol:
    win1 = 'Петя'
    if vas > tol:
        win2 = 'Вася'
        win3 = 'Толя'
    else:
        win2 = 'Толя'
        win3 = 'Вася'

elif vas > pet and vas > tol:
    win1 = 'Вася'
    if pet > tol:
        win2 = 'Петя'
        win3 = 'Толя'
    else:
        win2 = 'Толя'
        win3 = 'Петя'
else:
    win1 = 'Толя'
    if pet > vas:
        win2 = 'Петя'
        win3 = 'Вася'
    else:
        win2 = 'Вася'
        win3 = 'Петя'

print(f'{" " * 8}{f"{win1}":^8}')
print(f'{f"{win2}":^8}')
print(f'{" " * 16}{f"{win3}":^8}')
print(f'{f"II":^8}{f"I":^8}{f"III":^8}')
