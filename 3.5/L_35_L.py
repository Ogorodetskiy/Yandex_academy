numbers = input()
even = input()
odd = input()
eq = input()

with (
    open(numbers, "r", encoding="UTF-8") as file_in,
    open(even, "w", encoding="UTF-8") as f_out_even,
    open(odd, "w", encoding="UTF-8") as f_out_odd,
    open(eq, "w", encoding="UTF-8") as f_out_eq,
):

    for line in file_in.readlines():
        v_even = []
        v_odd = []
        v_eq = []

        for n in line.split():
            q = 0

            for x in n:
                if int(x) % 2 == 0:
                    q += 1

            if q > len(n) - q:
                v_even.append(n)
            elif q < len(n) - q:
                v_odd.append(n)
            else:
                v_eq.append(n)

        print(*v_even, file=f_out_even)
        print(*v_odd, file=f_out_odd)
        print(*v_eq, file=f_out_eq)
