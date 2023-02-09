n=int(input("enter a limit"))
for i in range(n):
    for s in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("* ",end=" ")
    print()
for i in range(n):
    for s in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print(" *",end=" ")
    print()