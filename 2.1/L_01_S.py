goods = input()
price = int(input())
weight = int(input())
total = int(input())
print(16 * '=' + 'Чек' + 16 * '=')
print(f'Товар:{goods:>29}')
print(f'Цена:{f"{weight}кг * {price}руб/кг":>30}')
print(f'Итого:{f"{weight * price}руб":>29}')
print(f'Внесено: {f"{total}руб":>26}')
print(f'Сдача: {f"{total - weight * price}руб":>28}')
print(35 * '=')
