# def upper(fun):
#     def wrapper(name):
#         result=fun(name)
#         return result.upper()
#     return wrapper
#
# @upper
# def hello(name):
#     return "hello "+name
# #f=upper(hello)
# print(hello("saliha"))





# def upper_case(fun):  #higher order functio
#       def wrapper():
#         result=fun()
#         return result.upper()
#     return wrapper
# @upper_case
# def hello():
#     return "hello"
# f=hello
# print(f())


# another example
def triple_decor(fun):
    def wrapper(n):
        f=fun(n)
        return [item*3 for item in f]
    return wrapper



@triple_decor
def reversel(l):
    return l[::-1]
@triple_decor
def upperl(l):
    return [item.upper() for item in l]
@triple_decor
def fibinocci(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result

print(reversel([1,2,3,4]))
print(upperl(['a','d','f','s']))
print(fibinocci(6))







