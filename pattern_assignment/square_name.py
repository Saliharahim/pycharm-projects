str=input("enter the name")
st = len(str)
a=str.upper()
for i in range(st+2):
    for j in range(st):
         if i==0 or i==st+1:
             print(a[j],end="  ")
         elif j==0 or j==st-1:
             print(a[i-1],end="  ")
         else:
            print(" ",end="  ")
    print()

# n=5
# for i in range(1,n):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print( )