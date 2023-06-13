sp = list()
while (s := input()) != '':

    if s[-3:] != '@@@':
        if s[:2] == '##':
            s = s[2:]
        sp.append(s)

for w in sp:
    print(w)
