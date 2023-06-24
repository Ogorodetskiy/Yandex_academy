numbers = [1, 2, 3, 4, 5]

print({x for x in numbers if x ** 0.5 == int(x ** 0.5)})

# print({number for number in numbers if number in [i ** 2 for i in range(1, int(max(numbers) ** 0.5 + 1))]})
