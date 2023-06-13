st = list()
while (s := input()) != 'ФИНИШ':
    for w in s.lower().split():
        for b in w:
            st.append(b)

s_set = sorted(set(st))
res = ''
q_max = 0
for sw in s_set:
    q = st.count(sw)
    if q > q_max:
        res = sw
        q_max = q

print(res)
