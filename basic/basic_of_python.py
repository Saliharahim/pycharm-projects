# swapping without third variable

# a,b=int(input("enter a value")),int(input("enter a value"))
# a,b=b,a
# print("a=",a)
# print("b=",b)
'''
# type casting methods
 int float  str
 list(),dict(),tuple(),set()
'''

#list

# write progam  to check whethr the given num is positive ,negative or zero

# a=int(input("enter a number"))
# if a>0:
#     print("a is positive")
# elif a<0:
#     print("a is negative")
# else:
#     print("a is zero")
# largest of 3 numbers using nested if

# a=int(input("enter a number a:"))
# b=int(input("enter a number b:"))
# c=int(input("enter a number c:"))
# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
#
# elif b>c:
#     print("b is greater")
# else:
#     print("c is greater")

# while loop

# reverse of a number using while

n=123
rev=0
p=1
s=0
while (n>0):#12>0,1>0
    r=n%10# 3,2,1
    rev=rev*10+r# 3,32,321
    p=p*r
    s=s+r
    n=n//10#12,1
print("reverse is",rev)
print("product",p)
print("sum is",s)

