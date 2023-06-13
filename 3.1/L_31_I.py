while (s := input()) != '':
    if s[0] != '#':
        print(s[:(s.index('#') if '#' in s else len(s))])
