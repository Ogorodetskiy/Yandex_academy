from sys import stdin

lines = stdin.readlines()

for txt in lines:

    if txt.find("#") == -1:
        print(txt, end="")
    elif txt.find("#") != 0:
        print(txt[: txt.find("#")])
