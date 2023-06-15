data = list(input().split())
res = [int(data[0])]
for i in data[1:]:
    if i.isdigit():
        res.append(int(i))
    else:
        a = res.pop()
        exec("res[-1] " + i + "= a")
print(res[0])
