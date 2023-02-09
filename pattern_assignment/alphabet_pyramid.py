n=5
k=(65)
for i in range(n):
    for s in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()
