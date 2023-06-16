st = list()
for _ in range(int(input())):
    st.extend(input().split())
print(*set(st), sep='\n')
