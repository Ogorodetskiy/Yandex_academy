d = {
    'А': 'A', 'Б': 'B', 'В': 'V',
    'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
    'И': 'I', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
    'Я': 'IA', 'Ь': '', 'Ъ': '',
}

res = ''

with open("cyrillic.txt", encoding="UTF-8") as file_in:

    for line in file_in:
        trans = line.rstrip("\n")
        for i in trans:
            if i.upper() in d:
                res += d[i.upper()].lower().capitalize() if i == i.upper() else d[i.upper()].lower()
            else:
                res += i
        res += '\n'

with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    file_out.write(res)
