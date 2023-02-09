# 1.

# def sum():
#     a,b=10,20
#     s=a+b
#     return s  # or return a+b
# # s=sum()
# # print('sum is ',s)
#   OR

#print("sum is ",sum())

#parameters

# def sum(a,b):
#     s=a+b
#     return s  # or return a+b
# s=sum(100,200)
# print('sum is ',s)

# FACTORIAL

# n=int(input('enter a number'))
# def fact(a):
#     p=1
#     for i in range(1,a+1):
#         p=p*i
#     return p
# print("factorial is",fact(n))

# arbitary = save as tuple
# def col(x,*r):
#     #print(r[0])
#     print('normal arg:',x)
#     for i in r:
#         print(i)
# col('red','white','yellow')

'''keyword argument  ===save as dictionary'''
# def stud(str1,str2,str3):
#     print("first:",str1)
#     print("second:", str2)
#     print("third:", str3)
# stud(str2='anu',str1='sree',str3='sara')

# arbitary keyword argument===save as dictionary

# def stud(**a):
#     for i,j in a.items():
#         print('%s=>%s'%(i,j))
# stud(str2='anu',str1='sree',str3='sara')
#
#

# def student(x,*arg,**ar):
#     print("simple:",x)
#     for i in arg:
#         print(i)
#     for i,j in ar.items():
#         print(i,j)
# student('saliha','dona',"duaa",str2='anu', str1='sree', str3='sara')


# default parameter

# def display(place='india'):
#     print(" iam from :",place)
# display()
# display("china")
#




# tup=("50")
# print(tup)
# print(type(tup))
#

# tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
# print(tuple1)


aTuple = (100,)
print(aTuple * 2)

# tuple1 = (1120, 'a')
# print(max(tuple1))

# aTuple = (100, 200, 300, 400, 500)
# aTuple.pop(2)
# print(aTuple)

aTuple = (100, 200, 300, 400, 500)
print(aTuple[-2])
print(aTuple[-4:-1])
