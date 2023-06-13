pet = int(input())
vas = int(input())
tol = int(input())
if pet > vas and pet > tol:
    print('Петя')
elif vas > pet and vas > tol:
    print('Вася')
else:
    print('Толя')
