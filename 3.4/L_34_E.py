res = sorted(input().split(', ') + input().split(', ') + input().split(', '))
for x, y in enumerate(res, start=1):
    print(f'{x}. {y}', sep='\n')
