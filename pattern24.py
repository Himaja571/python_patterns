n=int(input("n:"))
for i in range(1,n+1):
    for j in range(i):
        ch=chr(ord('E')-(i-1))
        print(ch,end='')
        
    print()