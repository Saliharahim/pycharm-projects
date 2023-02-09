def sum(a,b):
    return ("sum is",a+b)
def divide(a,b):
    return("divide is",a/b)
def sub(a,b):
    return("substraction is",a-b)
def mul(a,b):
    return("multiplication is",a*b)
num1=int(input("enter a number"))
num2=int(input("enter a number"))
operation=input("enter the operation +,-,/,*")
if operation=="+":
    print(sum(num1,num2))
elif operation=="-":
    print(sub(num1,num2))
elif operation=="*":
    print(mul(num1,num2))
elif operation=="/":
    print(divide(num1,num2))
else:
    print("invalid")
