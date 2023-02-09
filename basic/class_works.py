'''1.  write a program to print characters from a string that are present at an even index number'''
# str1=input("enter the string")
# print("the string is",str1)
# l=len(str1)
# print("characters at even index number are:")
# for i in range(0,l,2):
#     print(str1[i])
#

'''2. # PYRAMID OF HORIZONTAL NUMBER TABLES'''

# rows = 7
# for i in range(1, rows + 1):  # FOR ROWS
#     for j in range(1, i + 1):  # FOR  COLUMNS
#         print(i * j, end=' ')
 #   print()

'''3. CHECK IF 2 LISTS HAVE COMMON ELEMNENTS'''
# l1=[3,2,5,4,6,7,8]
# l2=[3,2,8,9,7,6,5,4]
# print("l1 is:",l1)
# print("l2 is:",l2)
# l3=[]
# for i in range(len(l1)):
#     for j in range(len(l2)):
#         if l1[i] == l2[j]:
#             l3.append(l1[i])
# if len(l3) == 0:
#     print("no common elements")
# else:
#     print("list of common elements",l3)

''' 4.  dictionary comprehension'''
# def dollar_to_ruppee():
#     price={'laptop':10,'watch':3,'mobile':5,'keyboard':1}
#
#     convert_to_ruppee=81.38
#     n_price={i:j*convert_to_ruppee for(i,j) in price.items()}
#     return n_price
# rc=dollar_to_ruppee()
# print(rc)

''' 5.  write a program to print all number in a range divisible by a number'''
# lower=int(input("enter lower of limit"))
# upper=int(input("enter upper of limit"))
# n=int(input("enter the number to be divided"))
# for i in range(lower,upper+1):
#     if(i%n==0):
#      print(i)

''' 6. find all the words in a string that are less than 4 letters '''
# sentence=input("enter a sentence")
# words=sentence.split()
# print(words)
# r=[x for x in words if len(x)<4]
# print(r)

''' 7. Transpose of a metrix using list comprehension
Transpose of a metrix is the interchanging of rows and colomns'''
# matrix=[[1,2],
#         [3,4],
#         [5,6],
#         [7,8]]
# transpose=[[row[i] for row in matrix]for i in range(2)]
# print(transpose)

''' 8.WAP to exract number from a string by using list comprehension'''
# string='the room number 45and 33 are vaccant'
# l=[x for x in string if x.isdigit()]
# print(l)l
''' 9. WAP to print integer values in a list using list comprehension'''
# lst=[1,2,6.5,4.3,66,11,33,3.4,5.4]
# r=[x for x in lst if type(x)==int]
# print(r)

''' 10. WAP to print the strings that start with the letter 'c' and end with lletter 'b'''
# names=['chb','ydb','thd','hvd','cqjb','cjhenb']
# r=[x for x in names if x.endswith('b')and x.startswith('c')]
# print(r)

''' 11. change kilogram to pound using dictionary comprehension'''
# old_weight={'book':0.5,'milk':2.0,'tv':7.0}
# new={key:value*2.2 for (key,value) in old_weight.items()}
# print(new)

''' 12.using threading'''
# import threading
# def coder(number):
#     print("coders:",number)
#     return
# thread=[]
# for i in range(5):
#     t=threading.Thread(target=coder,args=(i,))
#     thread.append(t)
#     t.start()

'''13. create a list of square  umbers using list comprehension'''
# number=[1,2,3,4,5,6]
# s=[x*x for x in number]
# print(s)
def c():
    for i in xrange(10):
        print(i)
c()