first = input()
second = input()
answer = input()

with open(first, encoding="UTF-8") as file_in:
    res1 = set(file_in.read().split())
with open(second, encoding="UTF-8") as file_in:
    res2 = set(file_in.read().split())
with open(answer, "w", encoding="UTF-8") as file_out:
    print(*sorted(res2.symmetric_difference(res1)), sep='\n', file=file_out)
