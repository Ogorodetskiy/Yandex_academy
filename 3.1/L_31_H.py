n = int(input())

for _ in range(n):
    s = input()
    print(s.index('зайка') + 1 if 'зайка' in s else 'Заек нет =(')

# for _ in range(int(input())):
#     if "зайка" in (place := input()):
#         print(place.index("зайка") + 1)
#     else:
#         print("Заек нет =(")
