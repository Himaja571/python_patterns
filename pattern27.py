rows=5
for i in range(1, rows + 1):
    print(chr(64 + i),end=" ")
    for j in range(i-1):
        print(i-1,end=" ")
    print()