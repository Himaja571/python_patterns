n=int(input("n:"))
for i in range(0,2*n-1):
    for j in range(0,2*n-1):
        top=i
        down=j
        right=(2*n-2)-j
        left=(2*n-2)-i
        print(n-min(min(top,down),min(left,right)),end=" ")
    print()