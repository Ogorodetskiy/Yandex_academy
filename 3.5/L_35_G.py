file = input()
txt = []
with open(file, encoding="UTF-8") as file_in:
    for line in file_in:
        txt += map(int, line.split())

print(
    len(txt),
    len([i for i in txt if i > 0]),
    min(txt) if len(txt) != 0 else 0,
    max(txt) if len(txt) != 0 else 0,
    sum(txt),
    round(sum(txt) / len(txt), 2) if len(txt) != 0 else 0,
    sep="\n",
)
