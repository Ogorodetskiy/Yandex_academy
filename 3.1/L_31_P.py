length, line = int(input()), []
for _ in range(int(input())):
    line.append(input())
for i in line:
    if length > 3:
        print(i[:length - 3] + "..." if len(i) >= length - 3 else (i + "..." if length == 4 else i))
        length -= len(i)
