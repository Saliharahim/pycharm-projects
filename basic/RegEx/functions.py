# findall()

import re
str='rose is a beautiful and colorful flower'
s=re.findall('ful',str)
print(s)
#
# s1=re.findall('full',str)
# print(s1)  #  empty list

# d='cat mat pat rat sat'
# a=re.findall('[scr]at',d)
# print(a)

# a=re.findall('[^scr]',d)
# print(a)

# d='cat mat pat rat sat 99234 939'
# a=re.findall('\d{3}',d)  #\d is for start with digit
# print(a)

# d='cat mat pat rat sat 992343 939 6666'
# a=re.findall('\d{1,4}',d)  #\d is for start with digit
# print(a)

# d='cat mat pat rat sat 9923 939'
# a=re.findall(r'\b\d{4}\b',d)  #r for read \b for boundry[strt,stp] ,exact 4 values
# print(a)

'''   SEARCH 
    it returns a match object if there is a match object anywhere in a string
    returns address of match'''
str='class will start at 10am'
#print(s.start())

# s=re.search('\d',str)
# #print(s)
# print(s.start())
#
# s2=re.search('python',str)
# print(s2)

# s=re.search('^class.*10am$',str)
# if s:
#     print("find")
# else:
#     print("not find")

''' split
       return list'''
# str='class will start at 10am'
# s=re.split(' ',str)
# print(s)
#
# s=re.split('a',str)
# print(s)
#
# s=re.split(' ',str,2) # 2 represent occurance
# print(s)

# full match()
# str='python is simple'
# b=re.fullmatch(str,'python is simple')  # other wise its none
# print(b)

# sub()

# s='rose is a beautiful and colorful flower'
# g=re.sub(' ',"*",s)
# print(g)
#
# g=re.sub(' ',"*",s,3)
# print(g)
#







