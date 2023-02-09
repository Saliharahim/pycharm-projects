num1=int(input("enter a number"))
num2=int(input("enter a number"))
def square(a,b):
    l=[]
    for i in range(a,b+1):
        l.append(i**2)
    print(l)
square(num1,num2)