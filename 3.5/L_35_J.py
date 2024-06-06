some_file = input()
n = int(input())

with open(some_file, "r", encoding="UTF-8") as file_in:

    for txt in list(file_in)[-n:]:
        print(txt.strip())
