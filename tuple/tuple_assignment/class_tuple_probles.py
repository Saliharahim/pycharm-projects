#REVERSE A NUMBER

# tup=(1,2,3,4,5)
# x=tup[::-1]
#print(x)

        #ACCESS VALUE 20 FROM THE TUPLE
# tupl=(1,3,65,20,45,45)
# tupl1=(1,2,40,[10,2,3],(30,20,10),40)
        #remove repeated elements from this
# lst=list(tupl1)
# for i in lst:
#     x=lst.count(i)
#     if x>1:
#         lst.remove(i)
    #or
# a=[]
# for i in tupl:
#     if i not in a:
#         a.append(i)

# print(a)
# print(lst)
# x=tupl[3]
# y=tupl1[4][1]
# print(x)
# print(y)

         #CHECK IF ALL ITEMS IN tuple ARE SAME
# a=(1,2,3,4)
# #a=(1,1,1,1)
# f=1
# for i in a:
#     for j in range(i,len(a)-i):
#         if a[i]!=a[j+1]:
#             f=0
#             break
# if f==1:
#     print("same")
# else:
#     print("not same")
#
      #or
# a=set(a)
# if len(a)==1:
#     print("same")
# else:
#     print("not same")
#

       #COPY SPECIFIC ELEMENT FROM ONE TUPLE TO A NEW TUPLE
# c=(1,2,3,4,5,6,7)
# p=list()
# x=c[2:5]
# p.append(tuple(x))
# print(p)

#        SWAP TWO TUPLES IN PYTHON
# a=(1,2,3)
# b=(4,5,6)
# t=a
# a=b
# b=t
# print("a",a)
# print("b",b)

