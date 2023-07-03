from itertools import product

suit = ['пик', 'треф', 'бубен', 'червей']
nom = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']

suit.remove(input())

for card in product(nom, suit):
    print(card[0], card[1])
