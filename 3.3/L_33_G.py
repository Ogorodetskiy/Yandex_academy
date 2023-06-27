numbers = {1, 2, 3, 4, 5}
print({number: [i for i in range(1, number + 1) if not number % i] for number in numbers})
