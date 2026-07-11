n = int(input("Enter the number of rows: "))

for i in range(n):
    num = 1

    # Print leading spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Print Pascal's Triangle numbers
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()