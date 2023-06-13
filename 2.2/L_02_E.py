pet = 7
vas = 6
pet -= 3
vas += 3
pet += 2
vas += 3

n = int(input())
m = int(input())

pet += n
vas += m

if pet > vas:
    print('Петя')
else:
    print('Вася')
