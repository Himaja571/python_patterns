rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
if rows==columns: 
    for i in range(rows):
        for j in range(columns):
            if (i+j)%2==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()