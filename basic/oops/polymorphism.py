''' polymorphism-- one in many forms
 two types-- 1. compile time .eg=function overloading
2. runtime time.eg=function overriding'''
# function overloading example

# class a:
#     def sum(self,a):
#         print("sum is:",a+a)
#
#     def sum(self,a,b):
#         print("sum is:",a + b)
#
# obj=a()
# #obj.sum(10)
# obj.sum(2,3)
# OR
# class a:
#     def display(self,name=None):
#         if name is None:
#             print("hello")
#         else:
#             print("hello "+name)
# obj=a()
# #obj.display()
# obj.display("anu")

# overriding

class rectangle:
    def area(self,l,b):
        print("area of rectangle:",l*b)
class square(rectangle):
    def area(self,l,b):
        print("area of squre:",l*b)
obj=square()
obj.area(10,20)