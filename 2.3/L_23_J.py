x = 0
y = 0

while (sw := input()) != 'СТОП':
    n = int(input())
    if sw == 'СЕВЕР':
        y += n
    elif sw == 'ВОСТОК':
        x += n
    elif sw == 'ЮГ':
        y += -n
    else:
        x -= n

print(f'{y}\n{x}')
