n = int(input())
s_min = input()

for i in range(n - 1):
    s = input()
    if s < s_min:
        s_min = s

print(s_min)
