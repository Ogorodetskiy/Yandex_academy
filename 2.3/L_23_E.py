nsum = 0
while (n := float(input())) != 0:
    nsum += n if n < 500 else n * 0.9
print(nsum)
