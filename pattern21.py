n=int(input("n:"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" " ,end=" ")
    ch='A'
    for j in range(2*i+1):
        print(ch,end=" ")
        
    
    for j in range(0,n-i-1):
        print(" " ,end=" ")
    print()