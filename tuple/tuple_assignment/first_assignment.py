#CONVERT STRING TO TUPLE
# a="python"
# x=tuple(a)
# print(x)
# #
# #CONVERT LIST TO TUPLE
# b=[1,2,3,4,5]
# y=tuple(b)
# print(y)

#FIND REPEATED ITEMS FROM A TUPLE
tup=("a","p","p","l","e")
for i in tup:
    c=tup.count(i)
    print(c)
#     or
c=set()
for i in tup:
    if tup.count(i)>1:
        c.add(i)
print(tuple(c))
#or
# c=set(tup)
# print(c)
# for i in tup:
#     if i in c:
#         print("non repeated",i)
#print("repeated",i)