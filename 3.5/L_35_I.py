first = input()
second = input()

res = ''

with open(first, encoding="UTF-8") as file_in:
    txt = file_in.read().strip()
    txt = "\n".join(line for line in txt.splitlines() if line.strip())

    for x in txt.splitlines():
        res += " ".join(x.split()) + '\n'

with open(second, "w", encoding="UTF-8") as file_out:
    print(res[:-1], file=file_out)
