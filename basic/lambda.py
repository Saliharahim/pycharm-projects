#using def

# def sum(a,b):
#     return a+b
# print(sum(1,2))
#
# # using lambda

# sum=lambda a,b:a+b
# print(sum(3,4))

# x=lambda a:a*4
# print(x([1,2,3]))
#
# largest=lambda a,b:a if (a>b) else b
# print(largest(2,4))
#
# max_3=lambda  a,b,c:a if(a>b and a>c) else b if (b>a) and (b>c) else c
# print(max_3(6,4,3))

# filter
l=[1,3,5,6,7,8]
lst=list(filter(lambda x:x%2==0,l))
print(lst)

# # map
#
# l=[34,26,12,4,7,6,3]
# lst1=list(map(lambda x:x*2,l))
# print(lst1)
#
# l=[34,26,12,4,7,6,3]
# lst1=list(map(lambda x:x>10,l))
# print(lst1)

# reduce

# from functools import reduce
# l1=[1,2,3,4,5]
# p=reduce(lambda x,y:x*y,l1)
# print(p)
#
# l2=[3,4,5,6]

''' list comprehension 
syntax:   newlist = [expression for item in iterable if condition == True]

express return the output '''

# l=[x*3 for x in [1,2,3]]
# print(l)
#
# l1=[x+3 for x in [1,22,3,4,6,7] if x%2==0]
# print(l1)
#
# l3=[x for x in range(0,25) if x%2==0]
# print(l3)

# s=input("enter a string")
# l4=[x for x in s if x in ["a","e","i","o","u","A","E","I","O","U"]]
# print(str(l4))

# s=input("enter a string")
# splt=s.split(' ')
# print(splt)
# l5=[x[0] for x in splt]
# print(l5)

# colors=['red','white','green','pink']
# l6=[x for x in colors if 'e' in x]
# print(l6)
#
# colors=['red','white','green','pink']
# l6=[x for x in colors if x!='green']
# print(l6)
#
# colors=['red','white','green','pink']
# l6=[x.upper() for x in colors]
# print(l6)
#
# colors=['red','white','green','pink']
# l6=['hello' for x in colors]
# print(l6)
#
''' in case of else condition'''
colors=['red','white','green','pink']
l6=[x  if x!='pink' else 'blue' for x in colors]  # here  we write if condition first and then for loop,but for loop will execute first
print(l6)
