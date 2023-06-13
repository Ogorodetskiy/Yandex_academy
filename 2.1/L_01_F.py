nomen = input()
price = int(input())
weight = int(input())
summa = int(input())
print('Чек', '\n',
      f'{nomen} - {weight}кг - {price}руб/кг', '\n',
      f'Итого: {price * weight}руб', '\n',
      f'Внесено: {summa}руб' '\n',
      f'Сдача: {summa - price * weight}руб', sep='')
