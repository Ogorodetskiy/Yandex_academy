n = int(input())
m = int(input())
t = int(input())

print(f'{(n + (m + t) //60) %24:02}:{(m + t) % 60:02}')
