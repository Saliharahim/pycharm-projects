"""
1. write a python function to find the max of three numbers
2. write a python function to sum all the numbers in a list
3. write a python function to multiply all the numbers in a list
"""

# def max(a,b,c):
#     if(a>=b) and (a>=c):
#         largest=a
#     elif(b>=a) and (b>=c):
#         largest=b
#     else:
#         largest=c
#         return largest
# print(max(2,4,5))


# def sum(lst):
#     s=0
#     for i in lst:
#         s=s+i
#     return s
# print(sum((1,2,3,4,5)))
#

def mul(lst):
    m=1
    for i in lst:
        m=m*i
    return m
print(mul((1,2)))





