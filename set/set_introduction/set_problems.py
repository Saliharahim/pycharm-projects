#1.add a list of elements to a set
#a={2,8,7,0}
# b=[1,2,3,4,5,6]
# a.update(b)
#print(a)
# print(type(a))

#2.get only unique items from two sets
# a={1,2,3,4,5,5,3}
# b={6,5,9,8,4,}
# print(a|b)

#3.check if 2 sets have any elements in common. if yes ,display the common elements
# a={1,2,3,4,5,3,4}
# b={2,3,8,7,4,9,1}
# if a.isdisjoint(b):
#     print("no items in common")
# else:
#     print("it have common elements")
#     print(a&b)

#4. remove items from set1 that are not common to both set1 and set2
set1={1,2,4,3,7,6}
set2={2,5,6,3,7,1}
#print(set1&set2)
print(set1.intersection(set2))
