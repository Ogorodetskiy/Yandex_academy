date = list()
for _ in range((int(input())) + 1):
    date.append((input()))

for s in range(len(date)-1):
    if date[-1].lower() in date[s].lower():
        print(date[s])
