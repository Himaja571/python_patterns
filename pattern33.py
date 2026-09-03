rows=5
for i in range(1,rows+1):
    for j in range(i):
        if (i+j) % 2!=0:
            print(i,end=" ")
        else:
            print("*",end=" ")
    print()