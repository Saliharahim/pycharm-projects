# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# f=fact(5)
# print("factorial :",f)

''' 5*4!--24*5=120
4*3!--6*4=24
3*2!--2*3=6
2*1!--2*1=2

here datas are store in stack[ first in first out]'''
n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()