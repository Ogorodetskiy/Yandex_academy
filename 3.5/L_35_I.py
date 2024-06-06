first = input()
second = input()

res = []

with open(first, "r", encoding="UTF-8") as file_in:
    for txt in file_in:
        res.append((txt.strip().replace('\t', '').split()))
res = [x for x in res if any(x)]

with open(second, "w", encoding="UTF-8") as file_out:
    for txt in res:
        print(" ".join(txt), file=file_out)
