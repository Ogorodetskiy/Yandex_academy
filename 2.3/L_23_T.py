res = -1
h_bef = 0
for i in range(int(input())):
    b = int(input())
    h = b % 256
    r = (b // 256) % 256
    m = b // 256 ** 2
   
    if ((m + r + h_bef) * 37) % 256 != h or h > 99:
        res = i
        break
    h_bef = h
    
print(res)
