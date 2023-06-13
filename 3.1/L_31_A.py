n = int(input())
v_fl = 1
for _ in range(n):
    s = input()
    if s[0] not in ('а', 'б', 'в'):
        v_fl = 0
        break

print('YES' if v_fl else 'NO')
