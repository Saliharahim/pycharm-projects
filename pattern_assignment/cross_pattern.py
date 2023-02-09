n=11
for i in range(1,n):
    for j in range(1,n):
        if (i==j or i+j==n-1):
         print(j,end=" ")
        else:
         print(' ',end=' ')
    print()