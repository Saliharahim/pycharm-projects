#oops
#class-object
# class emp:
#     x=100
#     def display(self):
#         print("simple function")
#     def disp():
#         print("without self parameters")
#
#     def sum(self):
#         print("sum is",30+20)
#     def product(se,a,b):
#         print("product is",a*b)
#
# obj=emp()
# obj.display()
# print("value of x is",obj.x )
# obj.sum()
# obj.product(3,4)
# ob=emp  # here we should take a separate object ,nbecause its function not have self parameter
# ob.disp()
# #obj.disp()


#  SELF PARAMETERS

class emp:
    def read(self,a,b):
        self.x=a  # or we can write as self.a=a - it also have the same meaning, both a's are differnt,first a will store the value,and it is a clss obj
        self.y=b  # or we can write as self.b=b
    def sum(self):
        print("sum is",self.x+self.y)  # here we can self.a
    def product(c):
        print("product is",c.x*c.y)
    def s( ):
        print("hloo")
obj=emp()
obj.read(20,30)
obj.sum()
obj.product()
# ob=emp

