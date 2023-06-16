def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


data = list(input().split())
res = [int(data[0])]
for i in data[1:]:
    if i.isdigit():
        res.append(int(i))
    elif i == "/":
        a = res.pop()
        res[-1] //= a
    elif i == "~":
        res[-1] = -res[-1]
    elif i == "#":
        res.append(res[-1])
    elif i == "!":
        res[-1] = factorial(res[-1])
    elif i == "@":
        res.append(res.pop(-3))
    else:
        a = res.pop()
        exec("res[-1] " + i + "= a")

print(res[0])
