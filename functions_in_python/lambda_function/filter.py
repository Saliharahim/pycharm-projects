""" syntax

    filter(function,iterable)      returns object

    we can use only one iterarable at a filter function
"""
# ages=[34,23,56,12,11]
# def myfunct(x):
#     if(x<18):
#         return False
#     else:
#         return True
# adult=filter(myfunct,ages)
# # for x in adult:
# #     print(x)
# print(list(adult))
# 2.

a=[1,2,3,4,5,6,7]
b=[1,2,7,8,9,10]
f=filter(lambda x:x>2 ,a,b)  #here we can see filter function only accept 2 arg
print(list(f))

l1=[1,2,34,4,5]

f=filter(lambda  n:n%2==1 ,l1)
print(list(f))
