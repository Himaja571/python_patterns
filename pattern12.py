n=int(input("n:"))
for i in range(0,n+1):
    for j in range(1,n-i+2):
        print("*",end=" ")
    print()
