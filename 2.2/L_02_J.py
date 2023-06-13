npass = int(input())
s1 = (npass // 10) % 10 + npass % 10
s2 = npass // 100 + (npass // 10) % 10
print(int(str(s1) + str(s2)) if s2 < s1 else int(str(s2) + str(s1)))
