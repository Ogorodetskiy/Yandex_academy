from sys import stdin
import json

file_1 = input()


with open(file_1, encoding="UTF-8") as file_in:
    records = json.load(file_in)

lines = stdin.readlines()

for line in lines:
    if line:
        key = line.split('==')[0].strip()
        value = line.split('==')[1].strip()
        records[key] = value.strip()

with open(file_1, "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, sort_keys=False, indent=4, ensure_ascii=False)
