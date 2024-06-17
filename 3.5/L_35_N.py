import json

json_name = input()
json_update = input()

with open(json_name) as file:
    source = json.load(file)
with open(json_update) as file:
    updates = json.load(file)

name_key = 'name'
new_dict = {}

for data in source:
    name = data.pop(name_key)
    new_dict[name] = data

for data in updates:
    name = data.pop(name_key)
    if name not in new_dict:  # на случай,если исходный словарь не содержал такого имени
        new_dict[name] = {}
    for key in data.keys():
        if new_dict[name].get(key, '') < data[key]:
            new_dict[name][key] = data[key]

with open(json_name, 'w') as file:
    json.dump(new_dict, file, sort_keys=False, indent=4, ensure_ascii=False)
