n=int(input("n:"))
for i in range(0,n+1):
    for j in range(n-i):
        print("*",end=" ")
    for j in range(2*i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()