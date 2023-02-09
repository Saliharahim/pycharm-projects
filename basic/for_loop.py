# to print fibinocci series for with range method
# n=int(input("enter a number"))
# print("fibinocci")
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(3,n+1): #  here 'i' will not used
#     s = n1 + n2
#     print(n1)
#     n1 = n2
#     n2 = s

# prime

# n=int(input("enter a number"))
# f=0
# if n==1:
#     print("not defined")
# else:
#     for i in range(1,n+1):
#         if n%i==0:
#             f=f+1
#     if f==2:
#         print("prime")
#     else:
#         print("not prime")
# #  else after for loop
#
# for i in 'python':
#     print(i)
# else:
#     print("complete")

# break statement

# l=[10,20,30,40,50,100,60,70,80,90]
# #
# for i in l:
#     print(i)
#     if i==100:
#         break
    #print(i)
#  continue statement

l=[10,20,30,40,50,100,60,70,80,90]

for i in l:
    #print(i)
    if i==100:
        continue
    print(i)

#  pass statement

  # null

# s=[]
# c=int(input("how many elements in the list"))
# for i in range(c):
#     n=int(input("enter number"))
#     s.append(n)
# print(s)