#   newlist = [expression for item in iterable if condition == True]

#  List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


#1, we can write this
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

#print(newlist)

# instead of writing

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)


#  2.
newlist = [x for x in fruits if x != "apple"]
print(newlist)
#3
h_letter=[letter for letter in 'human']
print(h_letter)
#4.

even=[evenl for evenl in range(0,100) if evenl%2==0]
print(even)

odd=[oddl for oddl in range(0,100) if oddl%2==1]
print(odd)

#5.

num=[y for y in range(100) if y%2==0  if y%5==0]
print(num)

# sum of n natural numbers

print(sum([s for s in range(11) ]))

#usinng expression
print([(n*(n+1)/2) for n in range(1 ,(int(input ("enter the range"))+1))])   # here we get a list of sum

