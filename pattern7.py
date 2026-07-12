n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    print()