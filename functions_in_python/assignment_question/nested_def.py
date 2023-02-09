def outer(a,b):
    def inner():
        c=a+b
        return c
    return inner()+5
print(outer(2,4))

# def palindrome(str1):
#     a=str1
#     b=str1[::-1]
#     if a==b:
#         #print("pali")
#         return True
#     else:
#        # print("not")
#         return False
#print(palindrome('Hello World'))

# def sum(a):
#     return a+25
# sum(5)
# print(sum)

