sp_menu = set()
sp_week = set()

for _ in range(int(input())):
    sp_menu.add(input())

for _ in range(int(input())):
    for _ in range(int(input())):
        sp_week.add(input())

print(*sorted(sp_menu ^ sp_week) if len(sp_menu ^ sp_week) != 0 else ['Готовить нечего'], sep='\n')
