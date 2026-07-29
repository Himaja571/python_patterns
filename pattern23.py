n = int(input("n: "))

for i in range(n):
    # spaces
    for j in range(n - i - 1):
        print(" ", end=" ")

    ch = 'A'
    breakpoint = i

    for j in range(2 * i + 1):
        print(ch, end=" ")

        if j < breakpoint:
            ch = chr(ord(ch) + 1)
        else:
            ch = chr(ord(ch) - 1)

    print()