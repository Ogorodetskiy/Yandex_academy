import json

file_i = input()
file_o = input()

txt = []

with open(file_i, encoding="UTF-8") as file_in:
    for line in file_in:
        txt += map(int, line.split())

res = {'count': len(txt), 'positive_count': len([i for i in txt if i > 0]),
       'min': min(txt) if len(txt) != 0 else 0,
       'max': max(txt) if len(txt) != 0 else 0,
       'sum': sum(txt),
       'average': round(sum(txt) / len(txt), 2) if len(txt) != 0 else 0}

with open(file_o, "w", encoding="UTF-8") as file_out:
    json.dump(res, file_out, ensure_ascii=False, indent=4)
