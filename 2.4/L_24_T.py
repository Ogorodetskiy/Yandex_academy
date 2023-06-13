def dex2base(number, base):
    dig = '0123456789'
    if base > len(dig):
        return None
    result = ''
    while number > 0:
        result = dig[number % base] + result
        number //= base
    return result


n = int(input())
m = res = 0

for i in range(2, 11):
    s = 0
    for x in str(dex2base(n, i)):
        s += int(x)
    if s > m:
        m = s
        res = i
print(res)
