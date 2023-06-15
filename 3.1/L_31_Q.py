line = ''.join(input().lower().split())
print('YES' if line == line[::-1] else 'NO')
