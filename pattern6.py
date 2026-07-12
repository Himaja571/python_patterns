n = int(input("Enter the number of rows: "))

# Upper half
for i in range(1, n + 1):
    # Left stars
    for j in range(i):
        print("*", end="")

    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end="")

    # Right stars
    for j in range(i):
        print("*", end="")

    print()

# Lower half
for i in range(n - 1, 0, -1):
    # Left stars
    for j in range(i):
        print("*", end="")

    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end="")

    # Right stars
    for j in range(i):
        print("*", end="")

    print()