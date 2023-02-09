n=int(input("enter a number"))
a=round(n/2)
for i in range(2,a):
    print(" "*(a-i-1)+"*"*(2*i+1)+"  "*(a-i)+"*"*(2*i+1))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))