# tple=(1,2,3,4,"saliha",1.3)
# print(tple)
# print(type(tple))
# #use tuple keyword for change list to tuple
#
# #NESTED TUPLE
# x=(1,2,3,("saliha","duaa"),(21.34))
# print(x)
# #WE CAN USE INDEXING
# print(x[3])
# #SLICING POSSIBLE
# print(x[-1])#     NEGETIVE INDEXING
# print(x[1:3])     #POSITIVE SLICING
# print(x[::-1])
# print(x[:-4])
# print(x[-4:-1])

#UPDATING
# x=(1,2,3,("saliha","duaa"),(21.34))
# y=list(x)
# y[0]=10
# x=tuple(y)
# print("updating=",x)

#APPEND
# x = (1, 2, 3, ("saliha", "duaa"), (21.34))
# y=list(x)
# y.append("shamnas")
# x=tuple(y)
# print("append=",x)
#
# #ADDING ANOTHER values IN A TUPLE
# x = (1, 2, 3, ("saliha", "duaa"), (21.34))
# # y=list(x)
# a=(7,8,9)
# x+=a
# #x=tuple(y)
#print("addition",x)

#removing
#y=list(x)
#y.remove(7)
#x=tuple(y)
# print(x)
# #DELETING
# b=(2,3,4,5)
# print(b)
# del b
# print(b)

#COUNTING
a=(1,2,3,4,5,6)
# print(len(a))
# print(all(a))
# print(max(a))
# print(min(a))
# print(sorted(a))
# print(sum(a))

#enumerate

b=("python","saliha",2)
# y=enumerate(b)
# print(tuple(y))
#
for i,(a,b)in enumerate(zip(a,b)):
    print(i,a,b)
#
letter=[('a','A'),('b','B')]
for i,letter in enumerate(letter):
    print("letter %d is %s/%s" %(i,letter[0],letter[1]))

# #MAP
l=["saliha","duaa","python"]
test=list(map(set,l))
print(test)
