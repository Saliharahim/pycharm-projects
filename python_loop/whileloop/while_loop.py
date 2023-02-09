# 1. PRINT 1 TO 10
# i=1
# while(i<=10):
#     print(i)
#     i=i+1

# 2. PRINT MULTIPLICATION TABLE
# i=1
# n=int(input("enter a number"))
# while(i<=10):
#     print("%d*%d=%d \n"%(n,i,n*i))
#     i=i+1
#     #SUM OF N NATURAL NUMBERS
i=1
n=int(input("enter a number"))
s=0
while(i<=n):
    s=s+i
    i=i+1

print("sum is",s)
