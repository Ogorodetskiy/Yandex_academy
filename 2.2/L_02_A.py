print('Как Вас зовут?')
sname = input()
print(f'Здравствуйте, {sname}!')
print('Как дела?')
mood = input()
match mood:
    case 'хорошо':
        print('Я за вас рада!')
    case 'плохо':
        print('Всё наладится!')
