res = []
for i in list(map(lambda x: bin(int(x))[2:], input().split())):
    res.append({"digits": len(i), "units": i.count('1'), "zeros": i.count('0')})
print(res)
