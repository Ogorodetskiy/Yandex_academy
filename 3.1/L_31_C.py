L = int(input())
N = int(input())
s = list()

for _ in range(N):
    w = input()
    s.append(w)

for zag in s:
    print(zag[:L - 3] + '...' if len(zag) > L else zag)
