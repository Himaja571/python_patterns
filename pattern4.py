n = int(input("Enter the number of rows: "))

# Upper half
for i in range(1, n + 1):
    # Print spaces
    for j in range(1, n - i + 1):
        print(" ", end="")

    # Print stars
    for j in range(1, 2 * i):
        print("*", end="")

    print()

# Lower half
for i in range(n - 1, 0, -1):
    # Print spaces
    for j in range(1, n - i + 1):
        print(" ", end="")

    # Print stars
    for j in range(1, 2 * i):
        print("*", end="")

    print()