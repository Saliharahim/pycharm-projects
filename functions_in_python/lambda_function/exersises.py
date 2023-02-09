# create a funct that takes one arg and that arg will be mult with an unknwon given number

# def new(n):
#     return lambda a:a*n
# s=new(4)
# print(s(2))

# write a prgm to filter a list a integers using lambda

num=[1,2,3,4,5,6,7,8]
even=list(filter(lambda num:num%2==0,num))
print(even)

# print odd numbers
# odd=list(filter(lambda num:num%2!=0,num))
# print(odd)
#
# # lambda with if else conditions
#
# max=lambda a,b:a if(a>b) else b
# print(max(3,4))
#
#
# max_3=lambda  a,b,c:a if(a>b and a>c) else b if(b>a) and (b>c) else c
# print(max_3(2,3,4))


